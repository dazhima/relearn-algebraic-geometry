from __future__ import annotations

import json
import re
from pathlib import Path


TYPE_ABBREV = {
    "definition": "def",
    "theorem": "thm",
    "lemma": "lem",
    "proposition": "prop",
    "corollary": "cor",
    "example": "ex",
    "remark": "rem",
    "exercise": "exr",
}

RESULT_RE = re.compile(
    r"^(Definition|Theorem|Lemma|Proposition|Corollary|Example|Remark|Exercise)"
    r"\s*(\d+(?:\.\d+)*)?\s*\.?\s*(?:\(([^)]*)\))?\s*\.?\s*(.*)$",
    re.IGNORECASE,
)
PROOF_RE = re.compile(r"^Proof(?:\s+of\b[^.]*)?\.", re.IGNORECASE)
SECTION_RE = re.compile(r"^(?:§\s*)?(\d+(?:\.\d+)*)\.\s+(.+)$")
HOMEWORK_SECTION_RE = re.compile(r"^(\d+)\.\s+([A-Z][A-Za-z0-9 ,:;()/'-]{3,120})$")


def parse_document(raw: dict, cache_dir: Path) -> dict:
    blocks: list[dict] = []
    current: dict | None = None

    for page in raw["pages"]:
        page_num = page["page_num"]
        for line in page["text"].splitlines():
            stripped = line.strip()
            if not stripped:
                if current and current["text"]:
                    current["text"] += "\n"
                continue
            starter = classify_line(stripped, raw["kind"])
            if starter:
                if current:
                    blocks.append(finalize_block(current))
                current = starter
                current["page_start"] = page_num
                current["page_end"] = page_num
            else:
                if current is None:
                    current = new_block("body", None, None, stripped, None)
                    current["page_start"] = page_num
                else:
                    current["text"] += ("\n" if current["text"] else "") + stripped
                current["page_end"] = page_num

            if current and current["type"] == "proof" and proof_ended(current["text"]):
                blocks.append(finalize_block(current))
                current = None

    if current:
        blocks.append(finalize_block(current))

    structured = {
        **raw,
        "blocks": assign_fallback_anchors(blocks, raw["document_id"]),
    }
    structured.pop("pages", None)
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / f"{raw['document_id']}.json").write_text(
        json.dumps(structured, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return structured


def classify_line(line: str, kind: str) -> dict | None:
    result = RESULT_RE.match(line)
    if result:
        raw_type, number, label, rest = result.groups()
        block_type = raw_type.lower()
        anchor = anchor_for(block_type, number)
        return new_block(block_type, number, clean_label(label), rest.strip(), anchor)

    if PROOF_RE.match(line):
        text = PROOF_RE.sub("", line, count=1).strip()
        return new_block("proof", None, None, text, None)

    section = SECTION_RE.match(line)
    if section and looks_like_section_heading(section.group(2)):
        number, title = section.groups()
        anchor = "sec-" + slugify(f"{number}-{title}")
        return new_block("section_heading", number, title.strip(), "", anchor)

    if kind == "homework" and line.startswith("(") and re.match(r"^\(\d+\)\s+", line):
        number = re.match(r"^\((\d+)\)", line).group(1)  # type: ignore[union-attr]
        return new_block("exercise", number, None, line, f"exr-{number}")

    if kind == "homework":
        hw_section = HOMEWORK_SECTION_RE.match(line)
        if hw_section:
            number, title = hw_section.groups()
            return new_block("section_heading", number, title.strip(), "", f"hw-sec-{number}")

    return None


def looks_like_section_heading(title: str) -> bool:
    if len(title) > 130:
        return False
    if title[:1].islower():
        return False
    if title.endswith(".") and len(title.split()) > 8:
        return False
    return True


def new_block(block_type: str, number: str | None, label: str | None, text: str, anchor_id: str | None) -> dict:
    return {
        "type": block_type,
        "number": number,
        "label": label,
        "text": text,
        "anchor_id": anchor_id,
    }


def finalize_block(block: dict) -> dict:
    block["text"] = trim_blank_lines(block["text"])
    return block


def trim_blank_lines(text: str) -> str:
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def clean_label(label: str | None) -> str | None:
    if not label:
        return None
    return re.sub(r"\s+", " ", label).strip()


def anchor_for(block_type: str, number: str | None) -> str | None:
    if not number:
        return None
    abbrev = TYPE_ABBREV.get(block_type)
    if not abbrev:
        return None
    return f"{abbrev}-{number.replace('.', '-')}"


def assign_fallback_anchors(blocks: list[dict], document_id: str) -> list[dict]:
    seen: set[str] = set()
    counters: dict[str, int] = {}
    for block in blocks:
        anchor = block.get("anchor_id")
        if not anchor:
            if block["type"] in {"section_heading", "example", "remark", "exercise"}:
                counters[block["type"]] = counters.get(block["type"], 0) + 1
                anchor = f"{TYPE_ABBREV.get(block['type'], 'blk')}-{counters[block['type']]}"
        if anchor:
            original = anchor
            suffix = 2
            while anchor in seen:
                anchor = f"{original}-{suffix}"
                suffix += 1
            seen.add(anchor)
            block["anchor_id"] = anchor
    return blocks


def proof_ended(text: str) -> bool:
    normalized = text.strip()
    return normalized.endswith("□") or normalized.endswith("■") or normalized.endswith("QED")


def slugify(text: str) -> str:
    text = text.lower().replace("§", "")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_many(raw_documents: list[dict], cache_dir: Path) -> list[dict]:
    parsed = []
    for raw in raw_documents:
        print(f"[parse] {raw['document_id']}")
        parsed.append(parse_document(raw, cache_dir))
    return parsed
