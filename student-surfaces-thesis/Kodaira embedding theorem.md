---
id: kodaira-embedding-theorem
type: theorem
title: The Kodaira Embedding Theorem — analytic and algebraic proofs
status: stub
parent: _thesis-plan-index.md
depends_on:
  - hartshorne-ii7-projective-morphisms   # algebraic route: C1/C3/C5, D8+C12-C16 for the surface case
used_by:
  - student-surfaces-thesis
---

# The Kodaira Embedding Theorem

Statement transcribed from `materials/Griffiths-harris/ch1.pdf`, p.181 (PDF page 53), 2026-07-06. **Stub**: no proof reconstructed on either route yet — this is the top-down theorem node per the framework's own recipe (write Statement + Idea of Proof first, then spawn the modules the proof depends on). Idea of Proof below is quoted/paraphrased from the source as a citation of *their* stated strategy, not yet independently verified.

## Motivation

This is the actual hinge fact for the project, not a side lemma: it's what turns "positive/ample line bundle" into "projective embedding," it specializes ($n=1$) to exactly the "$\deg P=1\Rightarrow P$ ample, $n\ge2g+1\Rightarrow$ very ample" fact board-script §8 already used without deriving, and it's cited directly by Hartshorne Prop 7.16(c) to justify that blow-ups of quasi-projective varieties stay quasi-projective — i.e. it's load-bearing for the surface case (V.3, blow-ups of $\mathbb P^2$) too. Two genuinely independent proofs exist — analytic (curvature positivity + a vanishing theorem) and algebraic (ample sheaves + Serre's construction) — matching this project's dual-unlock strategy exactly, and building both is also where "projective space + $\mathcal O(1)$" and "blowing up" each get introduced in their two languages.

## Statement

**(Griffiths–Harris, p.181).** Let $M$ be a compact complex manifold and $L\to M$ a positive line bundle (admits a Hermitian metric with curvature form $\Theta_h > 0$ everywhere, as a $(1,1)$-form). Then there exists $k_0$ such that for all $k \ge k_0$, the map
$$\iota_{L^k}: M \to \mathbb P^N, \qquad N = \dim H^0(M,L^k) - 1,$$
given by a basis of $H^0(M,L^k)$, is well-defined and is an **embedding**.

**Algebraic restatement (Hartshorne language) — not yet verified as literally the same theorem, flagged as its own citation.** "Positive" $\leftrightarrow$ "ample" is itself a real correspondence (GAGA-adjacent), not a notational translation. Granting it, the statement becomes exactly the assembly of `hartshorne-ii7-projective-morphisms#C5` (Thm 7.6: ample $\Rightarrow$ some power very ample) with `#C1` (Thm 7.1: generating sections $\Rightarrow$ a well-defined map to $\mathbb P^N$) and `#C3` (Prop 7.3: the separating-points/separating-tangent-vectors criterion for that map to be a closed immersion).

## Idea of Proof

**Analytic (G–H, cited, pp.181ff — not reconstructed).** Reduce "$\iota_{L^k}$ is an embedding" to two surjectivity statements — a map separating any two points $x,y$, and a map separating tangent directions at each point — by fitting each into a short exact sequence of sheaves ($0\to \mathscr I_{xy}(L)\to\mathscr O(L)\to L_x\oplus L_y\to0$ and similarly with $\mathscr I_x^2(L)$ for tangent vectors). Both surjectivities would follow from a vanishing statement $H^1(M,\mathscr I(L^k))=0$ for $k\gg0$ — except that for $\dim M>1$, $\mathscr I_{xy}$ and $\mathscr I_x^2$ are *coherent sheaves*, not sheaves of sections of a vector bundle (that only holds in codimension 1), so the direct harmonic-theory technique needs the coherent-sheaf machinery (G–H ch.5) or an induction on $\dim M$ via a hypersurface section — G–H flags both routes as available and picks one; which, not yet extracted here.

**Algebraic (Hartshorne, cited).** No vanishing theorem at this level — "ample" is *defined* directly via the generation property (`#D2`), and Thm 7.6's proof is a direct construction: cover $X$ by finitely many affines on which a power of $\mathscr L$ trivializes, then patch using that each such open is affine (not an existence argument via a PDE or a cohomology vanishing).

⚠ **Open question, genuinely unresolved, not to be papered over:** are these "the same" proof wearing different clothes (Hartshorne's construction $\leftrightarrow$ G–H's vanishing-theorem reduction), or are they structurally different arguments that happen to reach the same conclusion? Worth deciding only after both routes are actually built out, not now.

## Proof

*(Neither route assembled. Steps below name the module each step needs; ⟦NEW⟧ = not written yet. Building one of these — with its own Step-0 questionnaire — is the actual next unit of work.)*

**Analytic route** (curves first; general $M$/surfaces deferred):
- *Step A1.* Projective space and $\mathcal O(1)$ as the hyperplane line bundle $H\to\mathbb P^n$ with Fubini–Study curvature. → `gh-projective-space-O1` ⟦NEW⟧ (source: `Griffiths-harris/ch0.pdf` or early `ch1.pdf`, not yet located precisely)
- *Step A2.* Positive line bundles; Chern–Weil; curvature $\leftrightarrow$ degree — the curve case already touched informally in `board-script.md` §6. → `gh-positive-line-bundles` ⟦NEW⟧
- *Step A3.* The vanishing theorem the embedding reduces to. → `gh-kodaira-vanishing` ⟦NEW⟧ (source: `Griffiths-harris/ch1.pdf`, "Some Vanishing Theorems and Corollaries," pp.148–160 — PDF pages 20–32, located but not extracted)
- *Step A4.* $\bar\partial$-existence machinery, beyond the one-complex-variable case already used in `board-script.md` §6. → `berndtsson-dbar-existence` ⟦NEW⟧ (source: `materials/7nynot.pdf`)
- *Step A5* (surfaces only). Demailly's singular metrics — needed once $L$ isn't strictly positive everywhere (e.g. exceptional divisors of a blow-up). → `demailly-singular-metrics` ⟦NEW⟧ (source: `materials/bayreuth.pdf`)

**Algebraic route** (Hartshorne):
- *Step B1.* Morphisms to $\mathbb P^n$ via (invertible sheaf, generating sections). → `hartshorne-ii7-projective-morphisms#C1`
- *Step B2.* Closed-immersion criterion. → `hartshorne-ii7-projective-morphisms#C3`
- *Step B3.* Ample $\Rightarrow$ some power very ample. → `hartshorne-ii7-projective-morphisms#C5`
- *Step B4* (surfaces only). Blowing up. → `hartshorne-ii7-projective-morphisms#D8, #C12–#C16`

∎ *(not reached — both columns are lists of citations, not a completed proof)*

## Checks / Connections

- [ ] $n=1$ (curve) specialization should recover board-script §8's "$\deg P=1\Rightarrow P$ ample, $n\ge2g+1\Rightarrow nP$ very ample" once B2/B3 are actually built — this is the concrete check that the assembly is right, not just plausible.
- [ ] The "positive $\leftrightarrow$ ample" correspondence used silently in the Statement's algebraic restatement is its own citation and is not yet verified here.
- [ ] The open question at the end of Idea of Proof (same argument or genuinely different?) — revisit once A3/B3 both exist.
