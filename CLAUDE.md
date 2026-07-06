# CLAUDE.md — Relearn algebraic geometry

parent: ../CLAUDE.md

skills: math-research-framework, math-human-discipline

framework: `../_framework/` — start at `../_framework/FRAMEWORK — operating manual.md` (format → spec, pedagogy + human discipline → principles). Framework rules are not restated here; this file holds only local state.

## Purpose

Fundamental-knowledge base for algebraic geometry — the scheme-theoretic / commutative-algebra background Yan has already worked through, which other projects and talk-decoding chats hook into instead of re-deriving. Sibling of `../relearn complex analysis/`. Registered as fundamental in `../fundamental knowledges/`.

## Status

Established, actively used. Twelve core "brick" notes written; full Rice commutative-algebra course available as deeper backup. Several live hook-names already used in `../talks/`.

## Document tree

- `_AG-prep-index.md` — **living index / hook-name catalog. Start here** when AG background is in play. Lists the bricks, their one-line hooks, and maintenance rules.
- Core notes (top level) — `fiber-of-morphism`, `spec-Zx`, `relative-canonical-bundle`, `deformation-to-normal-cone`, `direct-image`, `cohomology-base-change`, `proj`, `gm-grading`, `gluing`, `schemes`, `going-up`. (Filenames in `_AG-prep-index.md`.)
- `rice-algebra/` — Rice MATH 464 Commutative Algebra, full course (37 lectures + 11 homeworks). Prerequisite layer; start at `rice-algebra/course-index.md`.
- `fiber-product-beamer.{tex,pdf}` — Yan's own beamer talk on fiber products.
- `commutative-algebra/` — build/site artifacts (ignore for math).
- `student-surfaces-thesis/` — subproject. See `student-surfaces-thesis/CLAUDE.md`.
  Current status: guiding an undergrad (strong background, gap = research obstruction)
  through Hartshorne IV–V via a black-box-first march toward a thesis; session 1 is
  2026-07-02. The shared, hands-on side of this same thesis work — the actual
  notes-and-annotations repo the student clones — lives at `../hartshorne-project/`, kept
  as a sibling rather than nested here since it's a standalone git repo pushed to its own
  GitHub remote (`dazhima/hartshorne-project`, private), and this folder is the working
  tree of a *different*, already-public repo (`dazhima/relearn-algebraic-geometry`).

## Usage note

Cite notes by name; flag genuinely new bricks as ⟦NEW⟧ candidates for their own note and add a stub + index row. Do not require the folder to be attached for read-on-demand use from other projects.
