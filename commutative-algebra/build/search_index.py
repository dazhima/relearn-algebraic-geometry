from __future__ import annotations

import json
from pathlib import Path


SEARCHABLE_TYPES = {
    "definition",
    "theorem",
    "lemma",
    "proposition",
    "corollary",
    "proof",
    "example",
    "remark",
    "section_heading",
    "body",
    "exercise",
}


def build_search_documents(documents: list[dict], out_dir: Path) -> list[dict]:
    docs: list[dict] = []
    for document in documents:
        page = "homework.html" if document["kind"] == "homework" else f"{document['document_id']}.html"
        for i, block in enumerate(document["blocks"], start=1):
            if block["type"] not in SEARCHABLE_TYPES:
                continue
            anchor = block.get("anchor_id") or f"block-{i}"
            href_anchor = f"{document['document_id']}-{anchor}" if document["kind"] == "homework" else anchor
            number = block.get("number")
            label = block.get("label") or block.get("number") or document["title"]
            docs.append(
                {
                    "id": f"{document['document_id']}#{anchor}",
                    "href": f"{page}#{href_anchor}",
                    "lecture": document["document_id"],
                    "title": document["title"],
                    "type": block["type"],
                    "number": number,
                    "label": label,
                    "body": block.get("text", ""),
                }
            )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "search-index.json").write_text(json.dumps(docs, ensure_ascii=False), encoding="utf-8")
    print(f"[search] {len(docs)} searchable blocks")
    return docs
