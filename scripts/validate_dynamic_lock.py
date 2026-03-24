import argparse
import glob
import os
import sys
import xml.etree.ElementTree as ET


BASE_TEMPLATES = [
    "templates/base-dynamic-products.xml",
    "templates/base-dynamic-news.xml",
]


def iter_dynamic_sections(root):
    for section in root.iter():
        if section.tag != "section":
            continue
        template_key = section.attrib.get("data-template-key")
        if not template_key:
            continue
        yield template_key, section


def normalize_section(section):
    attrib = dict(section.attrib)
    attrib.pop("class", None)
    attrib.pop("data-custom-name", None)

    def clone_elem(elem):
        new_elem = ET.Element(elem.tag, attrib=dict(elem.attrib))
        new_elem.text = elem.text
        new_elem.tail = elem.tail
        for child in elem:
            new_elem.append(clone_elem(child))
        return new_elem

    cloned = clone_elem(section)
    cloned.attrib = attrib
    return cloned


def canonical_xml(elem):
    return ET.tostring(elem, encoding="utf-8").decode("utf-8")


def load_base_map():
    base_map = {}
    for path in BASE_TEMPLATES:
        if not os.path.exists(path):
            continue
        tree = ET.parse(path)
        root = tree.getroot()
        for template_key, section in iter_dynamic_sections(root):
            canon = canonical_xml(normalize_section(section))
            base_map.setdefault(template_key, set()).add(canon)
    return base_map


def find_xml_files(paths):
    files = []
    for path in paths:
        if os.path.isdir(path):
            files.extend(glob.glob(os.path.join(path, "*.xml")))
        else:
            files.append(path)
    return [f for f in files if os.path.exists(f)]


def is_dynamic_output(path):
    name = os.path.basename(path).lower()
    return name.startswith("dynamic-") or "-dynamic-" in name


def has_xpath(root):
    return any(elem.tag == "xpath" for elem in root.iter())


def has_footer(root):
    for elem in root.iter():
        if elem.tag == "footer":
            return True
        if elem.attrib.get("id") == "footer":
            return True
    return False


def has_header(root):
    for elem in root.iter():
        if elem.tag == "header":
            return True
        if elem.attrib.get("id") in {"top", "top_menu_container", "top_menu"}:
            return True
    return False


def has_qweb_wrapper(root):
    if root.tag != "t":
        return False
    has_call = any(
        elem.tag == "t" and elem.attrib.get("t-call") == "website.layout"
        for elem in root.iter()
    )
    has_wrap = any(
        elem.tag == "div" and elem.attrib.get("id") == "wrap"
        for elem in root.iter()
    )
    return has_call and has_wrap


def has_inline_style_tag(root):
    return any(elem.tag == "style" for elem in root.iter())


def validate_file(
    path,
    base_map,
    check_header=True,
    check_footer=True,
    check_qweb=True,
    check_style_tag=True,
):
    errors = []
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except ET.ParseError as exc:
        return [f"{path}: XML parse error: {exc}"]

    for template_key, section in iter_dynamic_sections(root):
        if template_key not in base_map:
            continue
        expected_set = base_map[template_key]
        actual = canonical_xml(normalize_section(section))
        if actual not in expected_set:
            errors.append(
                f"{path}: structure mismatch for data-template-key={template_key}"
            )

    if check_header and has_header(root):
        errors.append(f"{path}: header XML detected (SCSS-only policy)")

    if check_footer and has_footer(root) and not has_xpath(root):
        errors.append(f"{path}: footer change without xpath (XPath required)")

    if check_qweb and not has_qweb_wrapper(root):
        errors.append(f"{path}: missing QWeb wrapper")

    if check_style_tag and has_inline_style_tag(root):
        errors.append(f"{path}: inline <style> tag detected")
    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate locked dynamic sections and basic header/footer rules."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="XML file(s) or directories containing XML outputs",
    )
    parser.add_argument(
        "--no-header-check",
        dest="check_header",
        action="store_false",
        default=True,
        help="Disable header XML check",
    )
    parser.add_argument(
        "--no-footer-check",
        dest="check_footer",
        action="store_false",
        default=True,
        help="Disable footer XPath check",
    )
    parser.add_argument(
        "--no-qweb-check",
        dest="check_qweb",
        action="store_false",
        default=True,
        help="Disable QWeb wrapper check",
    )
    parser.add_argument(
        "--no-style-tag-check",
        dest="check_style_tag",
        action="store_false",
        default=True,
        help="Disable inline <style> tag check",
    )
    parser.add_argument(
        "--all",
        dest="check_all",
        action="store_true",
        default=False,
        help="Validate all XML files, not only dynamic outputs",
    )
    args = parser.parse_args()

    base_map = load_base_map()
    if not base_map:
        print("No base templates found for validation.", file=sys.stderr)
        return 2

    files = find_xml_files(args.paths)
    if not args.check_all:
        files = [f for f in files if is_dynamic_output(f)]
    if not files:
        print("No XML files found.", file=sys.stderr)
        return 2

    errors = []
    for path in files:
        errors.extend(
            validate_file(
                path,
                base_map,
                check_header=args.check_header,
                check_footer=args.check_footer,
                check_qweb=args.check_qweb,
                check_style_tag=args.check_style_tag,
            )
        )

    if errors:
        for err in errors:
            print(err)
        return 1

    print("Dynamic lock validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
