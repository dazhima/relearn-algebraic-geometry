---
id: ag-prep-index
type: index
title: Algebraic Geometry preparation — index (for hooking into talks)
status: living
---

# Algebraic Geometry preparation — index

**Owner:** Yan. **Purpose:** the scheme-theoretic / AG background Yan has already worked through. Talk-decoding chats should **hook new concepts into these notes** (as `wed-3-gao` did) instead of re-deriving from scratch, and should **not** require Yan to attach this folder.

**Absolute path:** `/Users/yanh/Docs/@Archive/2026/claude/obsidian-ai/math/Relearn algebraic geometry/`
**How to use:** read the specific note on demand when a talk touches it; cite it by name; flag genuinely new bricks as ⟦NEW⟧ candidates for their own note.

## Core notes (top level) — the bricks

| Note | One line | Live hook-name |
|---|---|---|
| `The Fiber of a Morphism (new-template rewrite).md` | scheme-theoretic fibre $f^{-1}(y)=\operatorname{Spec}(A\otimes_B\kappa(y))$; the canonical "fibre = base-change to a residue field" picture | **fiber-of-morphism** |
| `The Fiber of a Morphism and the Tensor Product.md` | longer original of the same: fibre via tensor product, worked affine-locally | fiber-of-morphism (long) |
| `Spec Z[x].md` | $\operatorname{Spec}\mathbb Z[x]\to\operatorname{Spec}\mathbb Z$ as a family of curves; generic vs closed fibre dichotomy $\mathfrak p\cap\mathbb Z=(0)$ or $(p)$ | **spec-Zx** |
| `Relative canonical bundle.md` | $K_{X/Y}$ for a smooth submersion; relative dualizing / fibrewise canonical | **relative-canonical-bundle** |
| `Deformation to normal cone.md` | Rees algebra + deformation to the normal cone (Fulton, Intersection Theory ch.5) | **deformation-to-normal-cone** |
| `Direct image sheaf.md` | pushforward $f_*\mathcal F$: definition + sheaf axioms | direct-image |
| `Cohomology and base change.md` | higher direct images $R^if_*$; the base-change theorem | cohomology-base-change |
| `Proj construction.md` | $\operatorname{Proj}$ of a graded ring; relative Proj of a sheaf of graded algebras; $\mathbb P^n$ charts | proj |
| `Group scheme and graded algebra.md` | $\mathbb G_m$, group schemes, gradings; grading $\leftrightarrow$ $\mathbb G_m$-action | gm-grading |
| `The gluing construction.md` | gluing sheaves via the cocycle condition; line/vector bundles as the example | gluing |
| `Schemes.md` | how to define a scheme; isomorphisms of ringed spaces | schemes |
| `The Going-up theorem.md` | going-up for integral extensions; field-over-field corollary | going-up |

**Live hooks already used:** `fiber-of-morphism`, `spec-Zx`, `relative-canonical-bundle`, `deformation-to-normal-cone` (see `talks/.../wed-3-gao/talk-note.md` for a worked example of hooking a talk into them).

## Deeper backup
- `rice-algebra/` — Rice MATH 464 **Commutative Algebra**, full course: **37 lectures + 11 homeworks** (categories → modules → tensor/symmetric/exterior algebra → localization → chain conditions → primary decomposition → …). Start at `rice-algebra/course-index.md`. Use as the prerequisite layer when a talk needs commutative-algebra machinery.
- `commutative-algebra/` — build/site artifacts (ignore for math).
- `fiber-product-beamer.{tex,pdf}` — Yan's own beamer talk on fiber products.

## Maintenance
When a talk forces a genuinely new AG brick (e.g. valuative criterion of properness, GAGA/analytification, Cartier pullback + degree on a curve — all flagged in the Gao decode), add a stub note here and a row above.
