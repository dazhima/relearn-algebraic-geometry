# CLAUDE.md — student-surfaces-thesis

parent: ../CLAUDE.md

skills: math-research-framework, math-human-discipline

## Purpose

Guiding an undergraduate student (background: Atiyah–Macdonald, do Carmo Riemannian
geometry, Bott–Tu *Differential Forms in Algebraic Topology*, Huybrechts ch.1 on complex
manifolds) toward an undergraduate thesis and master's-study prep, via Hartshorne GTM 52.
Strategy: skip the linear march through II/III; hit Chapters IV (curves) and V (surfaces)
directly for the geometry — the student's actual gap is concrete-example mileage and
research obstruction, not more theory. Log theoretical black boxes as they're hit rather
than pre-deriving them, then unlock the load-bearing ones jointly from two sides: the
student leads the algebraic route (his strength — homological algebra, spectral
sequences), Yan leads the analytic/Hodge route (his gap). The comparative unlock of 2–3
chosen black boxes, anchored on one concrete surface, becomes the thesis itself.

## Resources — two tracks, on purpose

- **Algebraic track:** commutative algebra (`../rice-algebra/`) → Hartshorne
  (`materials/hartshorne1977.pdf`).
- **Analytic track:** Griffiths–Harris (`materials/Griffiths-harris/`, ch.0–6 + front/index
  matter) + Berndtsson, *An Introduction to things* $\bar\partial$ (`materials/7nynot.pdf`)
  + Demailly, *Singular hermitian metrics on positive line bundles* (`materials/bayreuth.pdf`).
  All three are locally present — confirmed 2026-07-06; the "TBA" this used to say was stale.

**Ordering is deliberate, not incidental.** For any given black box, the student is sent
into the **harder**, more scheme-theoretic source (Hartshorne) *first*, even where
Griffiths–Harris would be more accessible given his background (do Carmo, Bott–Tu,
Huybrechts ch.1 — all closer to G–H's register) — so that he builds the rigorous version
before a geometric picture exists to lean on. The analytic/G–H route is meant to arrive
*second*, as an independent confirmation of the same fact from the opposite direction
(the same dual-unlock pattern as M5a/M5b), not as the easier way in.

## Status

Session 1 (2026-07-02) happened — see `board-script.md` (the actual live-session script,
much further along than the pre-session module map below suggests: full dual algebraic +
analytic derivation of Riemann–Roch and Serre duality for curves, culminating in a proof
of "algebraic curve = compact Riemann surface"). Several black boxes were cited live but
never logged (Serre duality's nondegeneracy, the Hodge theorem, Hörmander's estimate,
Chow's theorem, and — the first one now under attack — "a point on a curve is ample").
Black-box log in `_thesis-plan-index.md` needs backfilling from `board-script.md`; thesis
anchor not yet chosen (shortlist in the index).

## Document tree

- `Kodaira embedding theorem.md` — **theorem-node stub** (top-down: Statement + Idea of
  Proof only, no proof reconstructed). The actual hinge fact for M5a/M5b: recovers
  board-script §8's curve-case fact as $n=1$; needed for Hartshorne 7.16(c) in the
  surface case. Two routes, both unbuilt: analytic (G–H + Berndtsson + Demailly) and
  algebraic (cites `Hartshorne-II.7 — Projective morphisms.md` entries directly).
- `Hartshorne-II.7 — Projective morphisms.md` — **stub**, 7.1–7.17 statements only
  (morphisms to $\mathbb P^n$, ample/very ample, linear systems, Proj/$\mathbb P(\mathscr
  E)$/blowing up), quoted from `materials/hartshorne1977.pdf`. Feeds the algebraic route
  of the theorem above.
- `_kodaira-network-index.md` — **complete module catalog** of the hinge network
  (curve floor, A/B routes, GAGA bridge, destination floor, SCV horizon incl. the
  conference-prep 🎤 spine, with verified arXiv sources). The graph in
  `kodaira-hinge.html` is drawn from this ledger — update both together.
- `skim/` — **recognition-mode webpages** (talk-register applied to modules): one page
  per hinge module + `skim/index.html` hub, linked from the graph's clickable nodes.
  Orientation only — reading them upgrades nothing; statuses mirror the catalog.
  Round 1 = hinge layer (13 pages); destination + horizon pages planned.
- `kodaira-hinge.html` — dual-use big-picture page (extends `dependency-map.html`,
  whose Stem-6 vanishing-theorem prediction it confirms): Kodaira embedding as the
  central hinge, A/B proof tracks, black-box log, two-track resource map, SCV
  horizon, global module graph. New third file; `dependency-map.html` kept intact.
- `thesis-guide.html` — **the artifact to show the student.** A single hand-authored
  reading-webpage (not slides): hero, SVG module-roadmap/progress chart, sticky
  table-of-contents, and full prose sections with real theorem statements (Hartshorne
  V.1 intersection axioms, Riemann–Roch for curves and the degree–genus derivation,
  blow-up canonical bundle formula, Noether's formula, the 27-lines/$W(E_6)$ picture),
  the Yan/student labor split, the session-1 script, and the three thesis anchors.
  KaTeX rendered client-side via CDN. Hand-edit directly — no build step.
- `_thesis-plan-index.md` — Yan's own working ledger: module map M0–M6 as a table,
  black-box log (empty, to fill in as sessions happen). Internal tracking, not for
  the student.
- `thesis-plan-slides.md` / `thesis-plan-slides.html` — superseded first attempt (slide
  deck via the `md-to-html` skill); Yan found the slide format unsuitable. Kept only
  because workspace files aren't deleted without confirmation — safe to ignore.

## Note

`../_AG-prep-index.md` bricks (`proj`, `gm-grading`, `gluing`, `direct-image`,
`cohomology-base-change`, `relative-canonical-bundle`, `deformation-to-normal-cone`) are
the shared algebraic skeleton this subproject draws on — not migrated here, since they
are used by other AG work too.
