#!/usr/bin/env python3
"""Build resources search index (L2 RAG).

讀 sources/resources_index.json，驗證每個 file 存在、keywords/triggers 非空，
產出 .agent/skills/icb_page_generator/resources/indexes/search_index.json
供 AI 在 knowledge_map 找不到對應項時快速查表。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "sources" / "resources_index.json"
TARGET = ROOT / ".agent" / "skills" / "icb_page_generator" / "resources" / "indexes" / "search_index.json"


def main() -> int:
    if not SOURCE.exists():
        print(f"[ERR] source missing: {SOURCE}", file=sys.stderr)
        return 1

    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    if not entries:
        print("[ERR] no entries", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen: set[str] = set()
    for i, e in enumerate(entries):
        fp = e.get("file")
        if not fp:
            errors.append(f"[{i}] missing 'file'")
            continue
        if fp in seen:
            errors.append(f"[{i}] duplicate file: {fp}")
        seen.add(fp)

        abs_path = ROOT / fp
        if not abs_path.exists():
            errors.append(f"[{i}] file not found: {fp}")

        for field in ("summary", "keywords", "triggers"):
            val = e.get(field)
            if not val:
                errors.append(f"[{i}] {fp} missing '{field}'")

    if errors:
        print("Validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    out = {
        "version": data.get("$version", 1),
        "usage": data.get("$usage", ""),
        "entry_count": len(entries),
        "entries": [
            {k: v for k, v in e.items() if not k.startswith("$")}
            for e in entries
        ],
    }

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"OK: {len(entries)} entries -> {TARGET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
