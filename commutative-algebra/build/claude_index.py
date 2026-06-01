from __future__ import annotations

from pathlib import Path


ARC = [
    ("Category theory and ideals", 1, 4),
    ("Modules, exactness, tensor products", 4, 13),
    ("Symmetric and alternating algebras", 14, 17),
    ("Localization and local properties", 18, 20),
    ("Noetherian and Artinian rings, primary decomposition", 20, 24),
    ("Integrality, Nullstellensatz, affine algebraic geometry", 25, 31),
    ("Dedekind domains", 32, 33),
    ("Projective, injective, flat modules; Tor and Ext", 34, 37),
]


KEYWORDS = [
    "category", "initial", "terminal", "functor", "maximal ideal", "nilradical",
    "jacobson", "chinese remainder", "module", "direct sum", "product",
    "exact sequence", "snake lemma", "finitely generated", "nakayama",
    "tensor", "flat", "adjoint", "fibered", "symmetric algebra",
    "alternating algebra", "differential forms", "localization", "local property",
    "noetherian", "artinian", "composition series", "primary decomposition",
    "integral", "going up", "going down", "noether normalization",
    "nullstellensatz", "algebraic sets", "dedekind", "rings of integers",
    "projective", "injective", "resolution", "tor", "ext", "support",
    "spectrum", "zariski", "affine scheme",
]


def write_claude_index(documents: list[dict], root_dir: Path) -> None:
    lectures = [doc for doc in documents if doc["kind"] == "lecture"]
    md: list[str] = [
        "# Commutative Algebra — Claude Knowledge Index",
        "",
        f"**Source:** Lecture notes, {len(lectures)} lectures",
        "**HTML knowledge base:** `commutative-algebra/site/index.html`",
        "",
        "## Course Arc",
        "",
    ]
    for idx, (name, start, end) in enumerate(ARC, start=1):
        md.append(f"{idx}. {name} — lectures {start:02d}–{end:02d}")

    md.extend(["", "## Key Definitions", "", "| Term | Lecture | Reference |", "|------|---------|-----------|"])
    for row in key_blocks(lectures, {"definition"}, limit=40):
        md.append(row)

    md.extend(["", "## Key Theorems", "", "| Name | Lecture | Reference |", "|------|---------|-----------|"])
    for row in key_blocks(lectures, {"theorem", "lemma", "proposition", "corollary"}, limit=45):
        md.append(row)

    md.extend(["", "## Topic Lookup", "", "| Topic | Where to look |", "|-------|--------------|"])
    for topic, where in topic_rows(lectures)[:50]:
        md.append(f"| {topic} | {where} |")

    root_dir.mkdir(parents=True, exist_ok=True)
    (root_dir / "index.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"[claude-index] wrote {root_dir / 'index.md'}")


def key_blocks(lectures: list[dict], types: set[str], limit: int) -> list[str]:
    rows = []
    for doc in lectures:
        for block in doc["blocks"]:
            if block["type"] not in types or not block.get("number") or not block.get("anchor_id"):
                continue
            name = block.get("label") or first_words(block.get("text", ""), 9) or f"{block['type'].title()} {block['number']}"
            display = f"{block['type'].title()} {block['number']}"
            href = f"site/{doc['document_id']}.html#{block['anchor_id']}"
            rows.append(f"| {escape_md(name)} | {doc['document_id']} | [{display}]({href}) |")
            if len(rows) >= limit:
                return rows
    return rows


def topic_rows(lectures: list[dict]) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    seen = set()
    for keyword in KEYWORDS:
        for doc in lectures:
            for block in doc["blocks"]:
                haystack = " ".join(
                    str(x or "") for x in [doc.get("title"), block.get("label"), block.get("text"), block.get("number")]
                ).lower()
                if keyword in haystack:
                    section = nearest_section(doc, block)
                    href = f"[{doc['document_id']} {section}](site/{doc['document_id']}.html#{block.get('anchor_id') or ''})"
                    if keyword not in seen:
                        candidates.append((keyword, href))
                        seen.add(keyword)
                    break
            if keyword in seen:
                break
    return candidates


def nearest_section(doc: dict, block: dict) -> str:
    page = block.get("page_start")
    previous = None
    for candidate in doc["blocks"]:
        if candidate is block:
            break
        if candidate["type"] == "section_heading":
            previous = candidate
    if previous and previous.get("number"):
        return f"§{previous['number']}"
    return f"p.{page}" if page else ""


def first_words(text: str, count: int) -> str:
    words = text.replace("\n", " ").split()
    return " ".join(words[:count])


def escape_md(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")
