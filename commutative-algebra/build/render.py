from __future__ import annotations

import html
import json
import base64
import re
import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape


RESULT_TYPES = {"definition", "theorem", "lemma", "proposition", "corollary"}
THEOREMISH_TYPES = {"theorem", "lemma", "proposition", "corollary"}


def render_site(documents: list[dict], refmap_payload: dict, search_docs: list[dict], out_dir: Path, build_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    env = Environment(
        loader=FileSystemLoader(build_dir / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.filters["type_name"] = type_name
    env.filters["json_script"] = lambda value: json.dumps(value, ensure_ascii=False)
    env.filters["b64_json"] = b64_json

    lectures = [doc for doc in documents if doc["kind"] == "lecture"]
    homeworks = [doc for doc in documents if doc["kind"] == "homework"]
    refmap = refmap_payload.get("refs", refmap_payload)
    nav = navigation_items(lectures)

    lecture_template = env.get_template("lecture.html.jinja2")
    prepared_lectures = []
    for index, document in enumerate(lectures):
        prepared = prepare_document(document, refmap, search_docs)
        prepared["prev"] = lectures[index - 1] if index > 0 else None
        prepared["next"] = lectures[index + 1] if index + 1 < len(lectures) else None
        prepared_lectures.append(prepared)
        html_text = lecture_template.render(
            document=prepared,
            lectures=nav,
            search_documents=search_docs,
            is_homework=False,
        )
        (out_dir / f"{document['document_id']}.html").write_text(html_text, encoding="utf-8")

    if homeworks:
        homework_doc = combine_homeworks(homeworks)
        prepared_homework = prepare_document(homework_doc, refmap, search_docs)
        html_text = lecture_template.render(
            document=prepared_homework,
            lectures=nav,
            search_documents=search_docs,
            is_homework=True,
        )
        (out_dir / "homework.html").write_text(html_text, encoding="utf-8")

    index_template = env.get_template("index.html.jinja2")
    (out_dir / "index.html").write_text(
        index_template.render(
            lectures=overview_rows(prepared_lectures),
            has_homework=bool(homeworks),
            search_documents=search_docs,
        ),
        encoding="utf-8",
    )

    shutil.copy2(build_dir / "static" / "style.css", out_dir / "style.css")
    shutil.copy2(build_dir / "static" / "lunr.min.js", out_dir / "lunr.min.js")
    print(f"[render] wrote {out_dir}")


def navigation_items(lectures: list[dict]) -> list[dict]:
    return [
        {
            "document_id": doc["document_id"],
            "title": doc["title"],
            "href": f"{doc['document_id']}.html",
        }
        for doc in lectures
    ]


def b64_json(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False).encode("utf-8")
    return base64.b64encode(raw).decode("ascii")


def prepare_document(document: dict, refmap: dict, search_docs: list[dict]) -> dict:
    prepared = {**document}
    blocks = []
    for block in document["blocks"]:
        copied = {**block}
        copied["heading"] = block_heading(copied)
        copied["html"] = format_text(copied.get("text", ""), refmap, document["document_id"])
        blocks.append(copied)
    prepared["blocks"] = blocks
    prepared["search_documents"] = search_docs
    return prepared


def combine_homeworks(homeworks: list[dict]) -> dict:
    blocks: list[dict] = []
    for hw in homeworks:
        blocks.append(
            {
                "type": "section_heading",
                "number": None,
                "label": hw["title"],
                "text": "",
                "anchor_id": hw["document_id"],
            }
        )
        for block in hw["blocks"]:
            copied = {**block}
            if copied.get("anchor_id"):
                copied["anchor_id"] = f"{hw['document_id']}-{copied['anchor_id']}"
            blocks.append(copied)
    return {
        "document_id": "homework",
        "kind": "homework",
        "title": "Homework",
        "source_pdf": "hwpure/*.pdf",
        "blocks": blocks,
    }


def overview_rows(lectures: list[dict]) -> list[dict]:
    rows = []
    for doc in lectures:
        sections = [block for block in doc["blocks"] if block["type"] == "section_heading"]
        rows.append(
            {
                "document_id": doc["document_id"],
                "title": doc["title"],
                "href": f"{doc['document_id']}.html",
                "sections": sections,
                "definition_count": sum(1 for block in doc["blocks"] if block["type"] == "definition"),
                "theorem_count": sum(1 for block in doc["blocks"] if block["type"] in THEOREMISH_TYPES),
            }
        )
    return rows


def block_heading(block: dict) -> str:
    block_type = type_name(block["type"])
    number = block.get("number")
    label = block.get("label")
    if block["type"] == "section_heading":
        return f"{number}. {label}" if number and label else label or "Section"
    if number and label:
        return f"{block_type} {number} ({label})"
    if number:
        return f"{block_type} {number}"
    return block_type


def type_name(value: str) -> str:
    return value.replace("_", " ").title()


def format_text(text: str, refmap: dict, current_document: str) -> str:
    if not text:
        return ""
    paragraphs: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            flush_paragraph(current, paragraphs, refmap, current_document)
            current = []
            continue
        if is_display_math(line):
            flush_paragraph(current, paragraphs, refmap, current_document)
            current = []
            paragraphs.append(f'<div class="display-math">{linkify(html.escape(line), refmap, current_document)}</div>')
        else:
            current.append(line)
    flush_paragraph(current, paragraphs, refmap, current_document)
    return "\n".join(paragraphs)


def flush_paragraph(lines: list[str], paragraphs: list[str], refmap: dict, current_document: str) -> None:
    if not lines:
        return
    escaped = "<br>\n".join(html.escape(line) for line in lines)
    paragraphs.append(f"<p>{linkify(escaped, refmap, current_document)}</p>")


def is_display_math(line: str) -> bool:
    stripped = line.strip()
    if len(stripped) < 3 or len(stripped) > 220:
        return False
    math_chars = set("=∈∉⊂⊆⊗⊕∧∨∑∏∩∪→←↦⇒⇐⇔≤≥≃≅≈√±·×−∞∅{}[]()/_^")
    math_count = sum(1 for char in stripped if char in math_chars)
    alpha_count = sum(1 for char in stripped if char.isalpha())
    return math_count >= 3 and math_count >= alpha_count * 0.35


def linkify(escaped_text: str, refmap: dict, current_document: str) -> str:
    if not refmap:
        return escaped_text
    keys = sorted(refmap.keys(), key=len, reverse=True)
    if not keys:
        return escaped_text
    pattern = re.compile(r"(?<![\w>])(" + "|".join(re.escape(key) for key in keys) + r")(?![\w<])")
    parts = re.split(r"(<a\b[^>]*>.*?</a>|<[^>]+>)", escaped_text)
    linked_parts = []
    for part in parts:
        if not part or part.startswith("<"):
            linked_parts.append(part)
            continue
        linked_parts.append(pattern.sub(lambda match: ref_link(match, refmap, current_document), part))
    return "".join(linked_parts)


def ref_link(match: re.Match, refmap: dict, current_document: str) -> str:
    key = match.group(1)
    target = refmap[key]
    href = f"#{target['anchor_id']}" if target["lecture_id"] == current_document else f"{target['lecture_id']}.html#{target['anchor_id']}"
    return f'<a class="xref" href="{href}">{html.escape(key)}</a>'
