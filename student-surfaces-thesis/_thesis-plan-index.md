---
id: student-thesis-plan-index
type: index
title: Student thesis guide — black-box march through Hartshorne IV–V
status: living
---

# Student thesis guide — black-box march through Hartshorne IV–V

**Student profile:** undergraduate; has read Atiyah–Macdonald (commutative algebra),
do Carmo *Riemannian Geometry*, Bott–Tu *Differential Forms in Algebraic Topology*
(so: de Rham/Čech-de Rham, spectral sequences, characteristic classes), and chapter 1
of Huybrechts *Complex Manifolds*. Already knows affine schemes. Strong in homological
algebra and spectral sequences; has not yet reached Hodge theory.

**Goal:** undergraduate thesis + preparation for master's study. The actual gap is not
theory — it's research obstruction: concrete mileage on real objects, especially
projective surfaces.

**Strategy:** do not march through Hartshorne II–III linearly. Hit Chapters IV (curves)
and V (surfaces) directly, treating II/III as reference, not prerequisite. When a
theoretical black box blocks understanding, name it, log it, and keep moving — most of
IV/V's *geometry* is legible modulo a short, identifiable list of black boxes. Once the
geography is built, go back and unlock the load-bearing black boxes from two
complementary angles at once: the student leads the **algebraic** route (his strength —
homological algebra, spectral sequences); Yan leads the **analytic/Hodge** route
(the student's current gap, and Yan's). This is mutual: the student teaches Yan
homological algebra along the way. The comparative write-up of 2–3 chosen black boxes,
anchored on one concrete surface, becomes the thesis.

This mirrors Hartshorne's own exposition of intersection theory (V.1 states the
intersection-number axioms and uses them immediately, before constructing the pairing
via cohomology later) — the plan works *with* the text's structure, not against it.

---

## Module map

| # | Module | Content | Yan does | Student does | Status |
|---|---|---|---|---|---|
| M0 | Contract & first black box | State the black-box-first rule; put V.1's intersection-number axioms on the board as the seed example; shortlist thesis anchors | Explain strategy + labor split; present V.1 axioms; propose anchor shortlist; assign first reading | Read Hartshorne V.1 (statement + examples) and IV.1 (Riemann–Roch statement only); start a black-box log | **in progress — session tomorrow, 2026-07-02** |
| M1 | Minimal geometric vocabulary | Divisors (Weil/Cartier), invertible sheaves, linear systems, maps to $\mathbb P^n$ — just enough to parse IV/V's sentences | Point to existing bricks (`proj`, `gm-grading`, `gluing`) as the algebraic skeleton; supply the "line bundle = functions with prescribed zeros/poles" picture | Look up II.6/II.7 definitions on demand, only when a black box requires one — not sequentially | planned, on-demand — `../Hartshorne-II.7 — Projective morphisms.md` exists as a **stub** (7.1–7.17 statements only, quoted from the book, no proofs/examples worked yet). II.6 (Divisors proper) still ⟦NEW⟧, not written. |
| M2 | Chapter IV fast pass (curves) | Riemann–Roch used immediately; degree–genus formula for plane curves; Hurwitz; elliptic curves as first example | Supply the analytic cross-check (genus = topological genus; degree-genus via adjunction in $\mathbb P^2$) | Compute degree–genus on 2–3 explicit curves (conic, nodal cubic, smooth quartic); use Riemann–Roch to get $h^0$ for line bundles on $\mathbb P^1$ and an elliptic curve | planned |
| M3 | Chapter V fast pass (surfaces) | Intersection axioms (V.1); blow-ups (V.3); ruled surfaces (V.2); worked examples — blow-ups of $\mathbb P^2$, cubic surface & 27 lines, del Pezzo surfaces | Connect blow-ups to the existing `deformation-to-normal-cone` brick; supply curvature/Chern-Weil picture of self-intersection | Compute self-intersections and canonical class on blow-ups of $\mathbb P^2$; locate the 27-lines computation as a concrete target | planned |
| M4 | Black-box ledger compiled | After M2/M3: list every black box actually used (expect Serre duality, finiteness of cohomology, Riemann–Roch's own proof, adjunction, existence of the intersection pairing) | Triage jointly | Triage jointly | not started — depends on M2/M3 |
| M5a | Algebraic unlock track | Comm. algebra (`../rice-algebra/`) → Hartshorne: Čech cohomology; cohomology of $\mathcal O(d)$ on $\mathbb P^n$; Serre duality via Čech/residues; Riemann–Roch derivation; intersection numbers via Fulton / deformation to the normal cone. **Deliberately the harder entry point** — assigned first, per book, before any G–H picture exists to lean on | Check work; connect to existing `cohomology-base-change`, `direct-image` bricks | Leads — his strength | in progress — first black box (ample point on a curve, board-script §8) live |
| M5b | Analytic unlock track | Griffiths–Harris (`materials/Griffiths-harris/`) + Berndtsson `materials/7nynot.pdf` + Demailly `materials/bayreuth.pdf`: Dolbeault cohomology; Hodge theory; harmonic-form proof of Serre duality; Riemann–Roch via Hodge decomposition; Chern-Weil computation of adjunction; Kodaira embedding (G-H p.181) via vanishing theorems + $\bar\partial$-existence + (surfaces) Demailly's singular metrics. Arrives **second**, as independent confirmation, not the easy way in | Leads — fills the student's Hodge gap | Checks against the algebraic statement for consistency | not started |
| M6 | Synthesis: the thesis | Comparative write-up of the 2–3 dual-unlocked black boxes, anchored on the chosen concrete surface | Advises on structure and exposition standard (per `math-research-framework`) | Writes | not started — depends on M4 |

---

## Tomorrow — session 1 script (2026-07-02)

1. Open with the diagnosis: his gap isn't more theory, it's concrete mileage — state
   the black-box-first plan explicitly, and name the labor split (he leads algebra,
   Yan leads analysis, thesis = the comparison).
2. Put Hartshorne V.1's axiomatic characterization of the intersection number on the
   board — the five properties — as the very first black box. Don't derive it.
3. One example immediately: self-intersection of a line in $\mathbb P^2$ is $1$; use it
   to show the axioms are the *right* axioms, before any cohomology appears.
4. State Riemann–Roch for curves (IV.1) without proof; connect it to genus via the
   degree–genus formula on a plane curve.
5. Assign: read V.1 + IV.1 (statement only); start the black-box log (one line per
   black box, with the exact statement used and where it was needed); come back with
   2–3 surfaces he finds appealing as a thesis anchor.
6. Do **not** assign Chapter III yet. First debt payment happens at M4, not before.

---

## Candidate thesis anchors (open — decide together, not tomorrow)

- **Cubic surfaces & the 27 lines** — self-contained, classical, rich intersection-theory
  computations, clean stopping point for an undergraduate thesis.
- **Hirzebruch / ruled surfaces** — $\mathbb P^1$-bundles; connects naturally to his
  do Carmo curvature background and to the existing `relative-canonical-bundle` and
  `direct-image` bricks.
- **Blow-ups & minimal models of surfaces** — broadest, most "research obstruction"
  flavored, longest.

---

## Black-box log

Registered as hit; not yet unlocked (entries below are open, not resolved — resolving
one is separate work, done as its own module).

| Black box | First hit (module) | Statement used | Unlocked? (algebraic / analytic) |
|---|---|---|---|
| A point on a curve is ample; Riemann–Roch gives explicit very-ample threshold $n\ge2g+1$ | board-script §8 (session 1) | Hartshorne Prop 7.3 + Thm 7.6 (general ample/very-ample + embedding criteria), specialized via IV.3.3 | algebraic: not yet — student's first Hartshorne II.7 pass hit trouble, being checked now / analytic: not started (G–H + Kodaira route, TBA) |
| Serre duality's nondegeneracy (the pairing is *perfect*, not just well-defined) | board-script §3 | cited, not derived | algebraic: not started / analytic: not started |
| The Hodge theorem (harmonic representatives) | board-script §3 | cited, not derived | not started (this *is* M5b's analytic track, once reached) |
| Hörmander's $L^2$ estimate | board-script §6 | cited (Berndtsson Lecture 1), sketched not fully derived | analytic: partially (Sketches A–C in board-script) |
| Chow's theorem (analytic $\Rightarrow$ algebraic in $\mathbb P^N$) | board-script §8 | cited, not derived | not started |

*(Backfilled 2026-07-06 from `board-script.md`; log as-you-go from here rather than
backfilling again.)*
