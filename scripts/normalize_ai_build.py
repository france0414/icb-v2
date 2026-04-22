#!/usr/bin/env python3
"""
Normalize AI-built website XML/SCSS for Odoo 15 compatibility.

Usage:
  python3 scripts/normalize_ai_build.py outputs/page.xml outputs/page.scss
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup


SECTION_CLASS_BASE = ["s_text_block", "o_colored_level"]


def _dedupe(seq: list[str]) -> list[str]:
    out: list[str] = []
    for item in seq:
        if item and item not in out:
            out.append(item)
    return out


def _map_tailwind_token(token: str) -> list[str]:
    fixed = {
        "w-full": ["w-100"],
        "h-full": ["h-100"],
        "flex": ["d-flex"],
        "inline-flex": ["d-inline-flex"],
        "flex-col": ["flex-column"],
        "flex-row": ["flex-row"],
        "items-center": ["align-items-center"],
        "items-start": ["align-items-start"],
        "items-end": ["align-items-end"],
        "justify-center": ["justify-content-center"],
        "justify-between": ["justify-content-between"],
        "justify-start": ["justify-content-start"],
        "justify-end": ["justify-content-end"],
        "relative": ["position-relative"],
        "absolute": ["position-absolute"],
        "fixed": ["position-fixed"],
        "static": ["position-static"],
        "sticky": ["position-sticky"],
        "rounded-2xl": ["rounded-2xl"],
        "rounded-xl": ["rounded-xl"],
        "rounded-full": ["rounded-full"],
    }
    if token in fixed:
        return fixed[token]

    m_order = re.fullmatch(r"(sm|md|lg|xl):order-(\d)", token)
    if m_order:
        return [f"order-{m_order.group(1)}-{m_order.group(2)}"]

    m_col = re.fullmatch(r"(sm|md|lg|xl):col-span-(\d+)", token)
    if m_col:
        return [f"col-{m_col.group(1)}-{m_col.group(2)}"]

    m_simple = re.fullmatch(r"col-span-(\d+)", token)
    if m_simple:
        return [f"col-{m_simple.group(1)}"]

    if token.startswith(("lg:", "md:", "sm:", "xl:")):
        return []

    return [token]


def normalize_xml(xml_path: Path) -> tuple[str, list[str]]:
    raw = xml_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")
    changes: list[str] = []

    # 1) class token mapping and cleanups
    for el in soup.find_all(True):
        classes = list(el.get("class", []))
        if not classes:
            continue

        mapped: list[str] = []
        for token in classes:
            mapped.extend(_map_tailwind_token(token))
        mapped = _dedupe(mapped)

        # Section must not keep horizontal padding utility
        if el.name == "section":
            mapped = [c for c in mapped if not c.startswith(("px-", "pl-", "pr-"))]

        # remove inline hidden carousel controls
        if ("carousel-control-prev" in mapped or "carousel-control-next" in mapped) and el.has_attr("style"):
            style = el.get("style", "")
            style = re.sub(r"display\s*:\s*none\s*;?", "", style, flags=re.I).strip()
            if style:
                el["style"] = style
            elif "style" in el.attrs:
                del el.attrs["style"]
            changes.append("Removed display:none from carousel controls")

        # inner classes should avoid s_custom_ prefix
        if el.name != "section":
            cleaned_inner: list[str] = []
            for c in mapped:
                if c.startswith("s_custom_"):
                    cleaned_inner.append(c.replace("s_custom_", "", 1))
                    changes.append("Converted inner s_custom_* class to plain class")
                else:
                    cleaned_inner.append(c)
            mapped = _dedupe(cleaned_inner)

        el["class"] = mapped

    # 2) SEO heading jump guard: convert h4/h5 under sections already headed by h2
    for section in soup.find_all("section"):
        has_h2 = bool(section.find("h2"))
        if not has_h2:
            continue
        for h in section.find_all(["h4", "h5", "h6"]):
            p = soup.new_tag("p")
            cls = h.get("class", [])
            h_tag = h.name
            if h_tag not in cls:
                cls = [h_tag] + cls
            p["class"] = _dedupe(cls)
            p.string = h.get_text(strip=True)
            h.replace_with(p)
            changes.append(f"Converted {h_tag} to p.{h_tag} for heading hierarchy")

    # 3) text-xs labels -> small
    for p in soup.find_all("p"):
        cls = p.get("class", [])
        if "text-xs" in cls:
            small = soup.new_tag("small")
            small["class"] = _dedupe(["d-block" if c == "text-xs" else c for c in cls if c != "text-xs"])
            small.string = p.get_text(strip=True)
            p.replace_with(small)
            changes.append("Converted p.text-xs to <small>")

    pretty = soup.prettify()
    pretty = pretty.replace("<html>\n <body>\n", "").replace("\n </body>\n</html>\n", "\n")
    xml_path.write_text(pretty, encoding="utf-8")
    return pretty, changes


def ensure_scss_rules(scss_path: Path, xml_text: str) -> list[str]:
    existing = scss_path.read_text(encoding="utf-8") if scss_path.exists() else ""
    additions: list[str] = []

    def append_if_missing(marker: str, block: str) -> None:
        nonlocal existing
        if marker in existing:
            return
        existing = existing.rstrip() + "\n\n" + block.rstrip() + "\n"
        additions.append(marker)

    if "rounded-full" in xml_text:
        append_if_missing(
            ".rounded-full",
            ".rounded-full {\n  border-radius: 0.75rem;\n}",
        )

    if "rounded-xl" in xml_text:
        append_if_missing(
            ".rounded-xl",
            ".rounded-xl {\n  border-radius: 0.5rem;\n}",
        )

    if "object-cover" in xml_text:
        append_if_missing(
            ".object-cover",
            ".object-cover {\n  object-fit: cover;\n}",
        )

    if "w-100" in xml_text and "h-100" in xml_text:
        append_if_missing(
            "#wrapwrap .object-cover",
            "#wrapwrap .object-cover {\n  width: 100% !important;\n  height: 100% !important;\n}",
        )

    if additions:
        scss_path.write_text(existing, encoding="utf-8")
    return additions


def write_report(xml_path: Path, changes: list[str], scss_additions: list[str]) -> Path:
    report = xml_path.with_suffix(".normalize.report.md")
    lines = [
        "# Normalize Report",
        "",
        f"- Target XML: `{xml_path.name}`",
        f"- XML fixes: {len(changes)}",
        f"- SCSS additions: {len(scss_additions)}",
        "",
        "## XML Fixes",
    ]
    if changes:
        lines.extend([f"- {c}" for c in changes])
    else:
        lines.append("- None")
    lines.extend(["", "## SCSS Additions"])
    if scss_additions:
        lines.extend([f"- {a}" for a in scss_additions])
    else:
        lines.append("- None")

    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize AI-built XML/SCSS for Odoo")
    parser.add_argument("xml", help="Path to XML file")
    parser.add_argument("scss", help="Path to SCSS file")
    args = parser.parse_args()

    xml_path = Path(args.xml)
    scss_path = Path(args.scss)

    if not xml_path.exists():
        raise SystemExit(f"XML not found: {xml_path}")

    xml_text, changes = normalize_xml(xml_path)
    scss_additions = ensure_scss_rules(scss_path, xml_text)
    report = write_report(xml_path, changes, scss_additions)

    print(f"Normalized XML: {xml_path}")
    print(f"Updated SCSS: {scss_path}")
    print(f"Report: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
