---
id: kodaira-network-index
type: index
title: Kodaira network — complete module catalog (hinge, destination, SCV horizon)
status: living
parent: _thesis-plan-index.md
---

# Kodaira network — complete module catalog

The full decomposition of the knowledge network rendered in `kodaira-hinge.html`: every
module, existing or planned, with id, source, status, and dependency edges. **This is
the ledger the graph is drawn from** — when a module's status changes here, the graph
is stale until updated.

Conventions per `../../_framework/math-framework-spec.md`. Rows marked ⟦NEW⟧ have **no
file yet** — the filename is reserved, the stub gets created when the module is opened
(with its Step-0 questionnaire), not before. `depends_on` cites module ids (or
`id#entry` for II.7's internal entries).

Legend for the conference tag: 🎤 = core vocabulary for the upcoming SCV conference
(L² estimates, multiplier ideals) — the student-facing byproduct target.

---

## Layer 0 — prerequisites, already on file elsewhere

Not re-listed as rows; these are the standing floor.

- `../rice-algebra/` — full commutative algebra course (algebraic track's base).
- `../_AG-prep-index.md` bricks used here: `proj`, `gm-grading`, `gluing`,
  `direct-image`, `cohomology-base-change`, `relative-canonical-bundle`,
  `deformation-to-normal-cone` (⚠ the *normal cone* — Spec of the associated graded —
  **not** the blow-up, which is Proj of the Rees algebra; documented trouble spot).

## Layer 1 — curve floor: session-1 black-box homes

| Filename | id | type | status | depends_on | notes |
|---|---|---|---|---|---|
| `Hartshorne-II.6 — Divisors.md` | `hartshorne-ii6-divisors` | module | ⟦NEW⟧ | rice-algebra | II.7 imports it as cited; already flagged in II.7's frontmatter |
| `Hartshorne-II.7 — Projective morphisms.md` | `hartshorne-ii7-projective-morphisms` | module | **stub — exists** | hartshorne-ii6-divisors | 16 entries, statements only; B-route home; student's first pass on C5 hit trouble |
| `Hartshorne-IV.3 — Very ampleness on curves (n ≥ 2g+1).md` | `hartshorne-iv3-curve-embedding` | module | ⟦NEW⟧ | hartshorne-ii7-projective-morphisms#C3, #C5; board-script §7 (Riemann–Roch) | black box #1's algebraic home — the n=1 case of the hinge; **under attack now** |
| `Hartshorne-III.7 — Serre duality, nondegeneracy.md` | `serre-duality-nondegeneracy` | module | ⟦NEW⟧ | cohomology-base-change (brick); rice-algebra | black box #2; §3 built the pairing, the *perfect*ness is what's cited |
| `GH-ch0 — Hodge theorem and harmonic forms.md` | `hodge-theorem` | module | ⟦NEW⟧ | — | black box #3; *is* M5b's core once reached; analytic route to Serre duality |
| `GH-ch1 — Chow's theorem.md` | `chow-theorem` | module | ⟦NEW⟧ | gh-projective-space-O1 | black box #5; last step of board-script §8; also feeds the GAGA bridge |

## Layer 2 — the hinge's two proof routes

**Algebraic route (B-steps) — not separate files**: B1 = `…ii7…#C1`, B2 = `#C3`,
B3 = `#C5`, B4 = `#D8 + #C12–C16`. They live inside the II.7 module; unlocking a
B-step = reconstructing that entry's proof there.

**Analytic route (A-steps) — five modules, named in `Kodaira embedding theorem.md`:**

| Filename | id | type | status | depends_on | notes |
|---|---|---|---|---|---|
| `GH-ch0 — Projective space, O(1), Fubini–Study.md` | `gh-projective-space-O1` | module | ⟦NEW⟧ | — | A1; source in G–H ch.0/early ch.1, not yet located precisely |
| `GH-ch1 — Positive line bundles, Chern–Weil.md` | `gh-positive-line-bundles` | module | ⟦NEW⟧ | gh-projective-space-O1 | A2; curve case touched informally, board-script §6 |
| `GH-ch1 — Kodaira vanishing.md` | `gh-kodaira-vanishing` | module | ⟦NEW⟧ | gh-positive-line-bundles, hodge-theorem | A3; G–H pp.148–160 — located, not extracted |
| `Berndtsson — dbar existence via L².md` 🎤 | `berndtsson-dbar-existence` | module | ⟦NEW⟧ (1-var **partial**) | hormander via board-script §6 Sketches A–C | A4; black box #4's home; source `materials/7nynot.pdf` |
| `Demailly-Bayreuth — singular hermitian metrics.md` | `demailly-singular-metrics` | module | ⟦NEW⟧ | gh-positive-line-bundles, berndtsson-dbar-existence | A5, surfaces only; source `materials/bayreuth.pdf` |

## Layer 3 — the hinge and its bridge

| Filename | id | type | status | depends_on | notes |
|---|---|---|---|---|---|
| `Kodaira embedding theorem.md` | `kodaira-embedding-theorem` | theorem | **stub — exists** | all A-steps; ii7#C1,#C3,#C5 (+#D8,#C12–C16 for surfaces) | statement transcribed (G–H p.181); neither route assembled |
| `GAGA — positive ↔ ample.md` | `gaga-positive-ample` | module | ⟦NEW⟧ | chow-theorem, gh-positive-line-bundles | the silently-used correspondence in the algebraic restatement — flagged in the theorem note's Checks; source TBD (Serre GAGA / Hartshorne App. B) |

## Layer 4 — destination floor: surfaces

| Filename | id | type | status | depends_on | notes |
|---|---|---|---|---|---|
| `Hartshorne-V.1 — Intersection pairing.md` | `hartshorne-v1-intersection` | module | ⟦NEW⟧ | serre-duality-nondegeneracy; ii7 (linear systems) | axioms already used since session 1 (M0 seed example) |
| `Hartshorne-V.3 — Blow-ups.md` | `hartshorne-v3-blowups` | module | ⟦NEW⟧ | ii7#D8,#C12–C16; kodaira-embedding-theorem (via 7.16(c)) | ⚠ Proj(Rees) ≠ normal cone — see Layer 0 caution |
| `GH-ch3 — Further techniques: currents, Chern classes.md` | `gh-ch3-currents` | module | ⟦NEW⟧ | hodge-theorem | G–H Ch. III; *also* the entry door to the whole horizon layer (currents) |
| `GH-ch4 — Surfaces, analytic side.md` | `gh-ch4-surfaces` | module | ⟦NEW⟧ | gh-ch3-currents, kodaira-embedding-theorem | G–H Ch. IV; the analytic twin of Hartshorne V |

## Layer 5 — SCV horizon

Sources verified on arXiv 2026-07-06. All strictly downstream of A4 + A5. None started.

| Filename | id | type | status | depends_on | source + notes |
|---|---|---|---|---|---|
| `Demailly-Bayreuth — multiplier ideal sheaves.md` 🎤 | `multiplier-ideal-sheaves` | module | ⟦NEW⟧ | demailly-singular-metrics, berndtsson-dbar-existence | $\mathscr J(\varphi)$ = germs with $\|f\|^2e^{-2\varphi}$ locally integrable; defined in `materials/bayreuth.pdf` — **already on disk** |
| `Nadel90 — Nadel vanishing.md` 🎤 | `nadel-vanishing` | theorem | ⟦NEW⟧ | multiplier-ideal-sheaves, gh-kodaira-vanishing | Nadel, Ann. of Math. 132 (1990); = A3 upgraded to singular metrics, $\mathscr J$ absorbing singularities; also in bayreuth.pdf |
| `OT87 — Ohsawa–Takegoshi L² extension.md` 🎤 | `ohsawa-takegoshi` | module | ⟦NEW⟧ | berndtsson-dbar-existence | Math. Z. (1987); the engine under Guan–Zhou; conference staple |
| `Demailly92 — Regularization of closed positive currents.md` | `demailly-regularization` | module | ⟦NEW⟧ | gh-ch3-currents, berndtsson-dbar-existence | J. Alg. Geom. 1 (1992) 361–409 — no arXiv, PDF on Demailly's page; approximation by smooth currents, negative part controlled by Lelong numbers, **via Hörmander L²** |
| `DP04 — Numerical characterization of the Kähler cone.md` | `demailly-paun-kahler-cone` | theorem | ⟦NEW⟧ | demailly-regularization | arXiv:math/0105176, Ann. of Math. 159 (2004); the flagship application of regularization (mass concentration). *Note: "Demailly–Păun's regularization" in conversation = Demailly-solo regularization (1992) + this application* |
| `Boucksom04 — Divisorial Zariski decomposition.md` | `boucksom-zariski` | theorem | ⟦NEW⟧ | demailly-regularization | arXiv:math/0204336 ("Higher dimensional Zariski decompositions"), publ. Ann. Sci. ENS 37 (2004) 45–76; psef class = nef-in-codim-1 part + exceptional divisorial part, via currents with minimal singularities |
| `DK01 — Semicontinuity of singularity exponents.md` | `dk-semicontinuity` | module | ⟦NEW⟧ | multiplier-ideal-sheaves, ohsawa-takegoshi | arXiv:math/9910118, Ann. Sci. ENS 34 (2001) 525–556; complex singularity exponents $c(\varphi)$, semicontinuity; poses the openness conjecture |
| `GZ15 — Strong openness of multiplier ideals.md` | `guan-zhou-strong-openness` | theorem | ⟦NEW⟧ | dk-semicontinuity, ohsawa-takegoshi | arXiv:1311.3781, Ann. of Math. 182 (2015); proves Demailly's strong openness conjecture, $\mathscr J(\varphi)=\mathscr J_+(\varphi)$, via O–T |

---

## Skim layer

Each module has (or will get) a recognition-mode webpage in `skim/` — what it is,
where it sits, the delta, the picture; no proofs. Hub: `skim/index.html`; the graph's
nodes link to them. Skim pages carry the module's status but never change it — they
are intake surfaces, like talk notes. Round 1 (hinge layer) written 2026-07-06;
destination + horizon pages pending.

## Maintenance

- Opening any ⟦NEW⟧ module: create the stub per the spec (Step-0 questionnaire first),
  flip its row to `stub — exists`, add real `children`/`used_by` links in its
  frontmatter, and update the graph in `kodaira-hinge.html`.
- The five black boxes in `_thesis-plan-index.md`'s log map to Layer-1 rows
  (#1 → `hartshorne-iv3-curve-embedding`, #2 → `serre-duality-nondegeneracy`,
  #3 → `hodge-theorem`, #4 → `berndtsson-dbar-existence`, #5 → `chow-theorem`).
  The log tracks *hits*; this catalog tracks *homes*.
- 🎤 modules are the conference-prep spine: A4 → O–T → multiplier ideals → Nadel.
  Recognition mode, not mastery — per-talk `talk-init` cards when the program is out.
