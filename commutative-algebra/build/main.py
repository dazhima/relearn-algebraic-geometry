from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT_DIR / "build"
DEPS_DIR = BUILD_DIR / ".deps"
if DEPS_DIR.exists():
    sys.path.insert(0, str(DEPS_DIR))

from claude_index import write_claude_index  # noqa: E402
from extract import extract_many, find_pdfs  # noqa: E402
from parse import parse_many  # noqa: E402
from refmap import build_refmap  # noqa: E402
from render import render_site  # noqa: E402
from search_index import build_search_documents  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a static commutative algebra knowledge base.")
    parser.add_argument("--pdf-dir", required=True, type=Path, help="Directory containing LectureN.pdf files.")
    parser.add_argument("--out-dir", required=True, type=Path, help="Output directory for the generated site.")
    parser.add_argument("--homework-dir", type=Path, default=None, help="Directory containing HWN.pdf files.")
    parser.add_argument("--sample", type=int, default=0, help="Only process the first N lectures for smoke testing.")
    args = parser.parse_args()

    pdf_dir = args.pdf_dir.expanduser().resolve()
    out_dir = args.out_dir.expanduser().resolve()
    homework_dir = args.homework_dir.expanduser().resolve() if args.homework_dir else pdf_dir.parent / "hwpure"
    cache_dir = BUILD_DIR / "cache"

    print("[main] Commutative algebra static site pipeline")
    print(f"[main] lecture PDF dir: {pdf_dir}")
    print(f"[main] homework PDF dir: {homework_dir}")
    print(f"[main] output dir: {out_dir}")

    lecture_paths = find_pdfs(pdf_dir, "Lecture*.pdf")
    if args.sample:
        lecture_paths = lecture_paths[: args.sample]
        print(f"[main] sample mode: first {len(lecture_paths)} lectures")
    homework_paths = [] if args.sample else find_pdfs(homework_dir, "HW*.pdf")

    raw_lectures = extract_many(lecture_paths, cache_dir, "lecture")
    raw_homework = extract_many(homework_paths, cache_dir, "homework") if homework_paths else []
    documents = parse_many(raw_lectures + raw_homework, cache_dir)
    refmap = build_refmap(documents, cache_dir)
    search_docs = build_search_documents(documents, out_dir)
    render_site(documents, refmap, search_docs, out_dir, BUILD_DIR)
    if not args.sample:
        write_claude_index(documents, ROOT_DIR)

    print("[main] done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
