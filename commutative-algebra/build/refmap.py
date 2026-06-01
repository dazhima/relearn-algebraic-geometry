from __future__ import annotations

import json
from pathlib import Path


DISPLAY_NAMES = {
    "definition": "Definition",
    "theorem": "Theorem",
    "lemma": "Lemma",
    "proposition": "Proposition",
    "corollary": "Corollary",
}


def build_refmap(documents: list[dict], cache_dir: Path) -> dict:
    refmap: dict[str, dict] = {}
    duplicates: dict[str, int] = {}
    for document in documents:
        if document["kind"] != "lecture":
            continue
        for block in document["blocks"]:
            display = DISPLAY_NAMES.get(block["type"])
            number = block.get("number")
            anchor = block.get("anchor_id")
            if not display or not number or not anchor:
                continue
            key = f"{display} {number}"
            if key in refmap:
                duplicates[key] = duplicates.get(key, 1) + 1
                continue
            refmap[key] = {
                "lecture_id": document["document_id"],
                "anchor_id": anchor,
                "title": document["title"],
            }
    payload = {"refs": refmap, "duplicates": duplicates}
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / "refmap.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[refmap] {len(refmap)} refs, {len(duplicates)} ambiguous labels skipped after first occurrence")
    return payload
