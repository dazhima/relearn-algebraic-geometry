---
id: surfaces-two-targets
type: note
title: Two targets for surfaces — the 27 lines, and minimal models
status: living
---

# Two targets for surfaces

Self-study notes, not board script — the point is for *you* to work through this first. Where a computation is short enough to check by hand, it's worked out in full; where I've marked "verify," that's a five-minute check worth actually doing rather than reading past. Where something is a genuinely deep citation (not just deferred bookkeeping), I've said so explicitly rather than blurring it into the flow.

Reuses two facts already nailed down in `board-script.md`: the blow-up canonical bundle formula $K_{\widetilde X}=\pi^*K_X+E$, and adjunction $2g(C)-2=C\cdot(C+K_X)$ for a curve $C$ on a surface.

---

## Target A — the 27 lines on a smooth cubic surface

### A.1 The model

**Fact (cited, classical):** every smooth cubic surface $X\subset\mathbb{P}^3$ is isomorphic to $\mathbb{P}^2$ blown up at six points $p_1,\dots,p_6$ in general position (no three collinear, not all six on a conic), embedded via the anticanonical system $|-K_{\widetilde X}|$. Conversely, blowing up six such points and embedding via $-K$ always produces a smooth cubic surface.

This is a real theorem (not a definition) — the embedding direction needs Riemann–Roch-for-surfaces to check $-K$ is very ample; I'm citing it here rather than proving it, since the target is the line count, not this construction. (Reference if you want the construction proof: Hartshorne V.4, or Manin's *Cubic Forms*, or Beauville's *Complex Algebraic Surfaces*.)

From here on, work entirely on $\widetilde X = \mathrm{Bl}_{p_1,\dots,p_6}\mathbb{P}^2$.

### A.2 Picard group and intersection numbers

$$\mathrm{Pic}(\widetilde X) = \mathbb{Z}H \oplus \mathbb{Z}E_1\oplus\cdots\oplus\mathbb{Z}E_6, \qquad \text{rank }7$$

where $H=\pi^*(\text{line})$ and $E_i$ = exceptional divisor over $p_i$. Intersection form:
$$H^2=1,\qquad E_i^2=-1,\qquad H\cdot E_i=0,\qquad E_i\cdot E_j=0\ (i\ne j).$$

Canonical class, via the blow-up formula applied six times:
$$K_{\widetilde X} = \pi^*K_{\mathbb{P}^2} + \sum_{i=1}^6 E_i = -3H+\sum_{i=1}^6 E_i.$$

**Verify:** $(-K)^2 = (3H-\textstyle\sum E_i)^2 = 9(1) + \sum(-1) = 9-6=3$. Cross-check independently: for a degree-$d$ surface in $\mathbb{P}^3$, adjunction on $\mathbb{P}^3$ gives $K_X=(d-4)H_{\mathbb{P}^3}|_X$; at $d=3$, $-K_X=H_{\mathbb{P}^3}|_X$ (the hyperplane class), so $(-K_X)^2=\deg X=3$. Same answer two ways — good sign the setup is right.

### A.3 What "a line" means, numerically

A line $L\subset X$ is a smooth rational curve of degree 1 for the embedding, i.e. $L\cong\mathbb{P}^1$ and $L\cdot(-K_X)=1$. Adjunction with $g(L)=0$:
$$-2 = L\cdot(L+K_X) = L^2+L\cdot K_X = L^2-1 \quad\Rightarrow\quad L^2=-1.$$

**So: lines $\leftrightarrow$ classes $D\in\mathrm{Pic}(X)$ with $D^2=-1$ and $D\cdot K_X=-1$, realized by an actual irreducible curve.** This is the whole strategy: turn a geometric question (find the lines) into a Diophantine one (find the classes).

### A.4 Solving the Diophantine system

Write $D=aH-\sum_{i=1}^6 b_iE_i$. Two computations (do these yourself, they're short):
$$D\cdot K_X = -3a+\textstyle\sum b_i \overset{!}{=} -1 \ \Rightarrow\ \sum b_i = 3a-1$$
$$D^2 = a^2-\textstyle\sum b_i^2 \overset{!}{=} -1 \ \Rightarrow\ \sum b_i^2 = a^2+1$$

Now hunt for integer solutions, by $a$:

- $a=0$: $\sum b_i=-1$, $\sum b_i^2=1$. Only way: one $b_i=-1$, rest $0$ — giving $D=E_i$. **6 solutions.** (The exceptional curves themselves are lines — matches the classical picture.)
- $a=1$: $\sum b_i=2$, $\sum b_i^2=2$. Only way: two $b_i=1$, rest $0$ — giving $D=H-E_i-E_j$. $\binom{6}{2}=$ **15 solutions.** (Strict transforms of lines through pairs of the six points.)
- $a=2$: $\sum b_i=5$, $\sum b_i^2=5$. Only way: five $b_i=1$, one $=0$ — giving $D=2H-\sum_{j\ne k}E_j$. $\binom{6}{1}=$ **6 solutions.** (Strict transforms of conics through five of the six points.)

For each case, a quick budget check (Cauchy–Schwarz flavor: spreading $\sum b_i$ across more nonzero entries only increases $\sum b_i^2$) rules out any other integer pattern — worth confirming for yourself at $a=1$ at least, it's a two-line argument.

$$6+15+6=27.$$

**What's genuinely still cited here:** that each of these 27 numerical classes is realized by a unique *irreducible* curve, not just a formal divisor class. That needs $h^0(D)=1$ for each (a Riemann–Roch-for-surfaces computation) plus irreducibility from the genericity of the six points. I haven't derived that part — it's a real citation, not bookkeeping.

### A.5 Incidence — which lines meet which

Compute $E_1\cdot(\text{everything})$ as the worked case:

| Other line | $E_1\cdot(\cdot)$ | meets? |
|---|---|---|
| $E_j,\ j\ne1$ | $0$ | no |
| $H-E_1-E_j$ | $1$ | **yes** (5 of these) |
| $H-E_j-E_k$, $1\notin\{j,k\}$ | $0$ | no (10 of these) |
| conic omitting point 1 | $0$ | no |
| conic omitting point $k\ne1$ | $1$ | **yes** (5 of these) |

Totals: $5+5=10$ meets, $5+10+1=16$ skew, $10+16=26$ ✓ (matches $27-1$).

**So every line meets exactly 10 of the other 26, and is skew to the remaining 16 — a fact you just derived, not a fact to memorize.** Pick one $H-E_i-E_j$ line and redo this table yourself as a check; the pattern (10 meets, 16 skew) should repeat by symmetry, but confirming it independently is the actual exercise.

### A.6 The $E_6$ structure — name-level only

The orthogonal complement of $K_X$ inside $\mathrm{Pic}(X)$ (rank 6, negative definite) is isomorphic to the $E_6$ root lattice, and the 27 lines correspond to the weights of $E_6$'s 27-dimensional minuscule representation. The Weyl group $W(E_6)$ (order 51840) acts as exactly the symmetries of the incidence pattern you just computed a piece of. This is a genuinely deep fact — flagging it precisely rather than deriving it: it needs representation theory beyond this note. (Dolgachev's *Classical Algebraic Geometry* has the full story if you want to chase it.)

---

## Target B — Castelnuovo's criterion and minimal models

### B.1 $(-1)$-curves, both directions

**Definition:** an irreducible curve $E\subset X$ is a $(-1)$-curve if $E\cong\mathbb{P}^1$ and $E^2=-1$.

**Necessity (derive this, it's the same move as A.3):** if $E$ is the exceptional divisor of blowing up a point, then $K_{\widetilde X}=\pi^*K_Y+E$, and since $E$ contracts to a point, $E\cdot\pi^*(\text{anything})=0$. So $E\cdot K_{\widetilde X} = E\cdot\pi^*K_Y+E^2 = E^2$. With $g(E)=0$: $-2=E\cdot(E+K)=E^2+E^2=2E^2\Rightarrow E^2=-1$. So every exceptional divisor of a blow-up is a $(-1)$-curve.

**Sufficiency — Castelnuovo's theorem (cited, real content):** the converse holds too. *Every* $(-1)$-curve, however it arises, is the exceptional divisor of *some* blow-down $X\to Y$ with $Y$ smooth projective.

### B.2 Why $E^2=-1$ is exactly the right number

The intuition worth having, even without the full proof: the normal bundle of $E$ in $X$ is $N_{E/X}=\mathcal{O}_X(E)|_E$, of degree $E^2=-1$, i.e. $N_{E/X}\cong\mathcal{O}_{\mathbb{P}^1}(-1)$ — *exactly* the normal bundle of the exceptional $\mathbb{P}^1$ in an actual blow-up. So a formal/analytic neighborhood of any $(-1)$-curve already looks identical to a neighborhood of a genuine exceptional divisor. Castelnuovo's theorem is the statement that this local coincidence globalizes into an actual algebraic contraction — built via a sufficiently positive linear system on $X$ that's constant on $E$ but separates everything else, contracting exactly $E$. Producing that linear system is where cohomology vanishing enters (the citation flagged back in the dependency map).

### B.3 Minimal models, and why the process terminates

$X$ is **minimal** if it contains no $(-1)$-curve. Repeatedly contracting $(-1)$-curves (when they exist) must stop: each blow-up increases the Picard rank by exactly 1 — $\mathrm{Pic}(\widetilde X)=\pi^*\mathrm{Pic}(Y)\oplus\mathbb{Z}E$ — so each contraction decreases it by 1, and $\rho(X)\ge1$ always. So after at most $\rho(X)-1$ contractions, no $(-1)$-curves remain: a minimal model. (Second check, consistent: contraction increases $K^2$ by exactly 1, since blowing up gives $K_{\widetilde X}^2 = (\pi^*K_Y+E)^2 = K_Y^2 + E^2 = K_Y^2-1$.)

**Named but not derived — the horizon:** minimal surfaces are classified by Kodaira dimension $\kappa\in\{-\infty,0,1,2\}$ (Enriques–Kodaira): $\kappa=-\infty$ is rational/ruled surfaces, $\kappa=0$ is K3/abelian/Enriques/bielliptic, $\kappa=1$ is elliptic surfaces, $\kappa=2$ is general type. That's the actual destination past this thesis; not attempting it here.

### B.4 Worked example: our cubic surface is very much not minimal

Every one of the 27 lines from Target A has $L^2=-1$ (that was the defining computation in A.3) — so $X=\mathrm{Bl}_6\mathbb{P}^2$ has *at least* 27 different $(-1)$-curves sitting on it. $\rho(X)=7$; contracting any one line drops $\rho$ to 6. Repeating eventually bottoms out at $\rho=1$, i.e. $\mathbb{P}^2$ itself (or possibly a minimal ruled surface, depending on choices).

**Remark, not developed here:** contracting *different* lines from the same $X$ can lead to differently-configured presentations as a blow-up of $\mathbb{P}^2$ — this is the classical Cremona-transformation phenomenon (the same del Pezzo surface, many ways to see it as $\mathrm{Bl}_6\mathbb{P}^2$). A good rabbit hole for later, not now.

---

## Honest ledger — derived here vs. still cited

| Fact | Status |
|---|---|
| $L^2=-1$, $L\cdot K=-1$ characterizes lines | derived (A.3) |
| The 27 numerical solutions | derived (A.4) |
| Each solution is a unique irreducible curve | **cited** — needs Riemann–Roch-for-surfaces + genericity |
| Incidence pattern (10 meets, 16 skew) | derived, one case (A.5) — verify a second case yourself |
| $E_6$/Weyl group identification | **cited** — genuinely deep, representation theory |
| $(-1)$-curve $\Rightarrow$ contractible (necessity) | derived (B.1) |
| Contractible $\Rightarrow$ $(-1)$-curve (Castelnuovo, sufficiency) | **cited** — real theorem, cohomology-vanishing proof |
| Termination into a minimal model | derived (B.3) |
| Enriques–Kodaira classification | **cited** — the horizon, not attempted |
