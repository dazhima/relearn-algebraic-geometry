from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

import pdfplumber


LECTURE_RE = re.compile(r"Lecture\s*(\d+)", re.IGNORECASE)
HOMEWORK_RE = re.compile(r"HW\s*(\d+)|Problem\s*Set\s*(\d+)", re.IGNORECASE)


def numeric_key(path: Path) -> tuple[int, str]:
    match = re.search(r"(\d+)", path.stem)
    return (int(match.group(1)) if match else 10_000, path.name.lower())


def lecture_id_from_path(path: Path) -> str:
    match = re.search(r"Lecture\s*(\d+)", path.stem, re.IGNORECASE)
    number = int(match.group(1)) if match else numeric_key(path)[0]
    return f"lecture-{number:02d}"


def homework_id_from_path(path: Path) -> str:
    match = re.search(r"HW\s*(\d+)", path.stem, re.IGNORECASE)
    number = int(match.group(1)) if match else numeric_key(path)[0]
    return f"homework-{number:02d}"


def find_pdfs(pdf_dir: Path, pattern: str = "*.pdf") -> list[Path]:
    return sorted(pdf_dir.glob(pattern), key=numeric_key)


def extract_pdf(path: Path, document_id: str, cache_dir: Path, kind: str) -> dict:
    pages: list[dict] = []
    title = None
    expected_lecture = int(document_id.split("-")[1]) if kind == "lecture" and "-" in document_id else None
    with pdfplumber.open(path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            if expected_lecture is not None and page_num > 1 and starts_later_lecture(text, expected_lecture):
                print(f"[extract] {path.name}: stopping before embedded later lecture on page {page_num}")
                break
            pages.append({"page_num": page_num, "text": text})
            if page_num == 1:
                title = extract_title(text, fallback=document_id, kind=kind)

    payload = {
        "document_id": document_id,
        "lecture_id": document_id if kind == "lecture" else None,
        "homework_id": document_id if kind == "homework" else None,
        "kind": kind,
        "title": title or document_id,
        "source_pdf": path.name,
        "source_path": str(path),
        "pages": pages,
    }
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / f"{document_id}.raw.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return payload


def extract_title(text: str, fallback: str, kind: str) -> str:
    lines = [normalize_spaces(line) for line in text.splitlines() if line.strip()]
    first_heading = None
    for line in lines[:40]:
        if re.match(r"^\d+(?:\.\d+)*\.\s+[A-Z]", line):
            first_heading = line
            break
    number_match = LECTURE_RE.search("\n".join(lines[:8]))
    if kind == "lecture" and number_match:
        prefix = f"Lecture {int(number_match.group(1))}"
        return f"{prefix}: {first_heading}" if first_heading else prefix
    hw_match = HOMEWORK_RE.search("\n".join(lines[:8]))
    if kind == "homework" and hw_match:
        number = hw_match.group(1) or hw_match.group(2)
        prefix = f"Problem Set {int(number)}"
        return f"{prefix}: {first_heading}" if first_heading else prefix
    return first_heading or fallback


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def starts_later_lecture(text: str, expected_lecture: int) -> bool:
    first_lines = "\n".join(text.splitlines()[:8])
    match = LECTURE_RE.search(first_lines)
    return bool(match and int(match.group(1)) > expected_lecture)


def extract_many(paths: Iterable[Path], cache_dir: Path, kind: str) -> list[dict]:
    extracted: list[dict] = []
    for path in paths:
        document_id = lecture_id_from_path(path) if kind == "lecture" else homework_id_from_path(path)
        try:
            print(f"[extract] {path.name} -> {document_id}")
            extracted.append(extract_pdf(path, document_id, cache_dir, kind))
        except Exception as exc:  # noqa: BLE001 - keep pipeline resilient by design.
            print(f"[extract] ERROR {path}: {exc}")
    return extracted
