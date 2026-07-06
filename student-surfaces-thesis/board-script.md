---
id: board-script
type: script
title: Board script — session 1 (Part I: curves and Riemann–Roch)
status: living
---

# Board script

Co-written live with Yan, topic by topic. Each entry: **Say** (what to say) / **Board** (what to write). Corrections/precision-adds from Claude are noted inline where relevant.

## Background map — whose tools these are

*Presentation note, for Yan, not for the board:* this map is for noticing connections out loud, not for skipping explanations. "You've seen this in Bott–Tu" is a mention, never an assumption — having read a book once is not the same as having it cold, and nothing here should be shortened on the theory that he "already knows it." If anything, undersell your own fluency rather than his — the goal is that he feels comfortable saying "actually I don't remember that part," not that he feels obligated to nod along. Full explanations stay, every time; the callback is a bonus on top, not a replacement.

| Source | Owns | Mention (don't assume) |
|---|---|---|
| Bott–Tu | Čech cohomology & the Čech–de Rham double complex, Mayer–Vietoris, the de Rham theorem, Poincaré duality | worth saying "this is the same construction as—" *after* explaining it in full, as a "does this ring a bell?" not a "you know this" |
| do Carmo | curvature, Gauss–Bonnet, geodesics | Gauss–Bonnet in §6 happens to be his theorem — nice to point out once it's back on the board in full, not instead of putting it there |
| Atiyah–Macdonald | exact sequences, additivity of length/rank on short exact sequences, the general rigor style | the Riemann–Roch induction in §7 rhymes with this — mention it, still derive every step |
| Huybrechts (through ch. 2) | complex manifolds, holomorphic vector bundles, divisors and line bundles | most recent reading, probably freshest — still don't skip steps that lean on it |
| *New this term* | Dolbeault cohomology, the Hodge theorem, harmonic representatives, Hörmander's $L^2$ estimate | genuinely new — say so plainly, it's fine and expected that this needs full explanation |

Update this table as Part II brings in more.

## Part I — Algebraic curves and Riemann–Roch

### 1. An algebraic curve is a compact Riemann surface — working definition

*Note:* trimmed, per Yan — proving the equivalence before Riemann–Roch exists was backwards. Definition now; the actual proof (both algebraically and analytically) is §8, once the tools are on the board.

**Say:** Fix vocabulary before anything else. Hartshorne's version: a nonsingular complete integral scheme of dimension 1. Over ℂ, work instead with the equivalent, more geometric description — an algebraic curve *is* a compact, connected Riemann surface. Take this as the working definition for now. The equivalence is a genuine theorem and it's worth actually proving, but not yet — it needs Riemann–Roch, which hasn't been built. Coming back to it in §8.

> [!board] Board
> algebraic curve$/\mathbb{C}$ $:=$ compact, connected Riemann surface — **working definition**
> Hartshorne: nonsingular complete integral scheme of dim 1 — equivalent, proof deferred to §8
>
> genus $g$ = # handles (topology) — preview: $=\dim H^0(X,\Omega^1_X)$, delivered in §3 (Serre duality)

### 2. A divisor records zeros and poles — with a catch

*Note:* the Z-linear-combination definition is right, and Mittag-Leffler is exactly the right classical touchstone. The subtlety worth surfacing: Mittag-Leffler holds unconditionally on ℂ (or any open Riemann surface); on a *compact* curve it doesn't — there's an obstruction, and measuring it is exactly what Riemann–Roch/Serre duality are for. If it held freely on compact curves, genus wouldn't exist as an invariant.

**Say:** A divisor is the bookkeeping device: a finite formal ℤ-linear combination of points, $D=\sum n_P \cdot P$. Where it comes from: any nonzero meromorphic function $f$ on $X$ has finitely many zeros and poles, recorded as $\operatorname{div}(f)$. Now the question you already have an instinct for from complex analysis: given a proposed list of zeros and poles, can you always find a function realizing exactly that data? On ℂ, yes, unconditionally — Mittag-Leffler. On a *compact* curve, no — there's an obstruction, and measuring it is exactly what Riemann–Roch and Serre duality do. If the naive Mittag-Leffler theorem held on compact curves, there would be nothing left to compute.

> [!board] Board
> Divisor: $D = \sum_P n_P \cdot P$, $\;n_P \in \mathbb{Z}$, finite support
>
> Principal divisor: for $0 \neq f \in K(X)^*$,
> $$\operatorname{div}(f) = \sum_P \operatorname{ord}_P(f)\cdot P$$
> (zeros: $\operatorname{ord}_P(f) > 0$, poles: $\operatorname{ord}_P(f) < 0$)
>
> $$\deg(\operatorname{div}(f)) = 0 \quad \text{always — compactness forces this (two proofs delivered in §3)}$$
>
> Mittag-Leffler, made precise: is there a nonzero $f$ with $\operatorname{div}(f)\ge -D$ — i.e. is $H^0(X,\mathcal{O}(D))\ne0$?
> *(not* $\operatorname{div}(f)=D$ *exactly — that additionally demands $D$ be principal, Abel's-theorem territory, a different question entirely)*
> - on $\mathbb{C}$ (open): **YES**, essentially always — classical Mittag-Leffler
> - on compact $X$: **NOT always** — obstruction $= h^1(D)$
>
> ↑ this is exactly Riemann–Roch / Serre duality — next

**What $\mathcal{O}(D)$ actually is, before it gets used everywhere.** No line bundle machinery needed to start — just a vector space of functions.

$$L(D) := \{f\in K(X)^*: \operatorname{div}(f)\ge -D\}\cup\{0\}$$

— meromorphic functions with poles no worse than $D$ allows, vanishing wherever $D$ demands. It's a $\mathbb{C}$-vector space: for $f,g\in L(D)$, $\operatorname{ord}_P(f+g)\ge\min(\operatorname{ord}_P f,\operatorname{ord}_P g)\ge -D_P$, so $f+g\in L(D)$ too.

**Anchor example, computable by hand:** $X=\mathbb{P}^1$, $D=n\cdot[\infty]$. $L(D)$ = rational functions with a pole only at $\infty$, order $\le n$ — exactly the polynomials of degree $\le n$, $\{1,z,\dots,z^n\}$, dimension $n+1$. Same object as $h^0(\mathcal{O}(n))=n+1$ from §1 — now with a face, not just a formula.

**Sheafify — the one genuinely new step, and it's small:** same formula, required only on an open $U$: $\mathcal{O}(D)(U):=\{f\in K(X)^*:\operatorname{div}(f)|_U\ge-D|_U\}\cup\{0\}$. Global sections recover $L(D)=H^0(X,\mathcal{O}(D))$. The only reason to bother: this is what makes $H^1$ meaningful at all — it measures whether local solutions (trivial to find on a small disk) patch into a global one, exactly §4's Čech story, now attached to a concrete object.

**Why it deserves "line bundle" — optional, satisfying once wanted, not required to proceed.** Cover $X$ by small opens $U_i$; on each, pick $g_i$ matching $D$ *exactly* on $U_i$ (near a single point $P$ with coefficient $n_P$: $g_i=z_P^{-n_P}$ in a local coordinate). For $f\in\mathcal{O}(D)(U_i)$, $f/g_i$ is genuinely holomorphic on $U_i$ — the poles cancel exactly. On overlaps, $g_{ij}:=g_i/g_j$ is holomorphic *and nowhere zero* (both match $D$ exactly there, so the ratio has divisor $0$); the cocycle condition $g_{ij}g_{jk}=g_{ik}$ is automatic. Those transition functions *are* the line bundle — its sections, by construction, are exactly elements of $\mathcal{O}(D)(U_i)$.

> [!board] Board — $\mathcal{O}(D)$, concretely first
> $$L(D) = \{f\in K(X)^*: \operatorname{div}(f)\ge -D\}\cup\{0\} \;=\; H^0(X,\mathcal{O}(D))$$
>
> $\mathbb{P}^1$, $D=n[\infty]$: $L(D) = \operatorname{span}\{1,z,\dots,z^n\}$, $\dim = n+1$
>
> sheafify (same condition, on opens $U$): $\mathcal{O}(D)(U) = \{f: \operatorname{div}(f)|_U\ge -D|_U\}\cup\{0\}$
> — this is what makes $H^1$ (§4, Čech) meaningful
>
> *optional — the line bundle picture:* local $g_i$ with $\operatorname{div}(g_i)|_{U_i}=-D|_{U_i}$ exactly
> $$f/g_i \text{ holomorphic on } U_i, \qquad g_{ij}:=g_i/g_j \text{ nowhere zero on } U_i\cap U_j$$
> $\{g_{ij}\}$ = transition functions of the line bundle; sections $\leftrightarrow$ elements of $\mathcal{O}(D)(U_i)$
>
> bonus: $D'=D+\operatorname{div}(h)$ (linearly equivalent) $\Rightarrow$ $f\mapsto fh^{-1}$ is an isomorphism $L(D)\xrightarrow{\sim}L(D')$
> — the line bundle depends only on the linear equivalence class; that's why $\operatorname{Pic}(X)$ (divisors mod $\sim$) is "the group of line bundles"

### 3. Serre duality, stated precisely

*Note:* this delivers on section 1's "preview" — $g=\dim H^0(\Omega^1_X)$ turns out to be the $D=0$ case of the statement below.

**Say:** Before killing the black box two ways, write down precisely what's being used. For $X$ compact of genus $g$ with canonical divisor $K$, Serre duality says $H^1(X,\mathcal{O}(D))$ isn't just abstractly isomorphic to $H^0(X,\mathcal{O}(K-D))^*$ — there's an explicit pairing realizing it: multiply a class $\xi\in H^1(D)$ by a section $\omega\in H^0(K-D)$ to land in $H^1(K)$, then take the residue (trace map $H^1(K)\to\mathbb{C}$). The theorem is that this pairing is *perfect* — nondegenerate — which is what makes the two spaces genuinely dual, not just equal in dimension.

> [!board] Board
> Serre duality (curves): for $D$ a divisor, $K$ canonical,
> $$H^1(X,\mathcal{O}(D)) \times H^0(X,\mathcal{O}(K-D)) \longrightarrow H^1(X,K_X) \xrightarrow{\ \mathrm{res}\ } \mathbb{C}$$
> $$(\xi,\ \omega)\ \longmapsto\ \xi\cdot\omega\ \longmapsto\ \operatorname{res}(\xi\cdot\omega)$$
> this pairing is **perfect** (nondegenerate)
> $$\Rightarrow\quad H^1(X,\mathcal{O}(D)) \cong H^0(X,\mathcal{O}(K-D))^*, \qquad h^1(D) = \ell(K-D)$$
>
> special case $D=0$: $\quad h^1(\mathcal{O}_X) = \ell(K) = g$
> — this *is* section 1's $g=\dim H^0(\Omega^1_X)$, now identified as $H^1(\mathcal{O}_X)$

**Sketch — where the pairing actually comes from:** don't leave "perfect pairing" as an assertion; the pairing itself is concrete. A class in $H^1(X,\mathcal{O}(D))$ is exactly Mittag-Leffler data (§2): a finite collection of prescribed principal parts (Laurent tails) $\{f_p\}$ at points $p$, modulo those realized by an honest global section. Given such data and $\omega\in H^0(K-D)$, define the pairing by multiplying the tail by the differential and summing residues. This is well-defined — independent of the representative — for exactly one reason: a global meromorphic 1-form has no choice but to have its residues cancel.

> [!board] Board — the pairing, concretely
> $\{f_p\}$ = principal parts at points $p$ (Mittag-Leffler data, §2), $\omega\in H^0(K-D)$
> $$\langle \{f_p\},\ \omega\rangle := \sum_p \operatorname{Res}_p(f_p\cdot\omega)$$
>
> Residue theorem (why this is well-defined): for any meromorphic 1-form $\eta$ on compact $X$,
> $$\sum_p \operatorname{Res}_p(\eta) = 0$$
> proof (one line, Stokes): $\eta$ is closed away from its poles, so
> $$0 = \int_{X\setminus\bigcup_p D_\epsilon(p)} d\eta = -\sum_p \oint_{\partial D_\epsilon(p)} \eta = -2\pi i \sum_p \operatorname{Res}_p(\eta)$$
> — no outer boundary term, since $X$ is compact (no boundary at all)
>
> still genuinely cited: **nondegeneracy** of $\langle\ ,\ \rangle$ — that it detects *everything*, not merely that it's well-defined

**Delivering on §2 — why $\deg(\operatorname{div} f)=0$, two ways.** Time to actually derive something that got asserted back in §2 rather than just trusted. First, geometrically: a nonzero meromorphic function is exactly a nonconstant holomorphic map $f:X\to\mathbb{P}^1$ — a pole is just a point mapping to $\infty$, nothing left singular once you land in $\mathbb{P}^1$ instead of $\mathbb{C}$. Since $X$ is compact, $f$ is a branched covering of some fixed degree $n$: *every* point of $\mathbb{P}^1$ has exactly $n$ preimages counted with multiplicity, the same $n$ no matter which point. $\operatorname{div}(f)=f^{-1}(0)-f^{-1}(\infty)$, and both terms total exactly $n$ — so $\deg(\operatorname{div} f)=n-n=0$.

Second, and this one costs nothing new — it's the residue theorem just derived above, aimed at a different 1-form: $d\log f=df/f$ is meromorphic on $X$. Locally, $\operatorname{ord}_P(f)=k$ means $f=z^kh(z)$ with $h$ holomorphic and nonvanishing at $P$, so $df/f=k\,dz/z+dh/h$, and $\operatorname{Res}_P(df/f)=k=\operatorname{ord}_P(f)$. Apply the residue theorem to $\eta=df/f$: $\sum_P\operatorname{ord}_P(f)=\sum_P\operatorname{Res}_P(df/f)=0$. Same conclusion, same tool, second use.

> [!board] Board — delivering on §2
> Geometric: $f:X\to\mathbb{P}^1$ nonconstant holomorphic (poles $\mapsto\infty$); $X$ compact $\Rightarrow$ $f$ has a well-defined degree $n$
> $$\operatorname{div}(f) = f^{-1}(0) - f^{-1}(\infty), \qquad \#f^{-1}(0) = \#f^{-1}(\infty) = n \ \text{(with multiplicity)}$$
> $$\Rightarrow\quad \deg(\operatorname{div} f) = n - n = 0$$
>
> Residue-theoretic (reuses the tool just built — nothing new): for $\operatorname{ord}_P(f)=k$, locally $f=z^kh(z)$, $h(P)\ne0$,
> $$\frac{df}{f} = k\,\frac{dz}{z} + \frac{dh}{h} \quad\Rightarrow\quad \operatorname{Res}_P\!\left(\frac{df}{f}\right) = k = \operatorname{ord}_P(f)$$
> $$\Rightarrow\quad \deg(\operatorname{div} f) = \sum_P \operatorname{ord}_P(f) = \sum_P\operatorname{Res}_P(df/f) \overset{\text{residue thm}}{=} 0$$

> [!success] Payoff — say this out loud
> Two more independent derivations of a fact that was just being trusted — and the second one is literally the same residue theorem from a few lines up, pointed at a different form. That's what "the tools start paying for themselves" actually looks like in practice.

**Geometric intuition — the same fact ($g=\dim H^0(\Omega^1_X)$), via topology from Bott–Tu.** Don't think about holomorphic forms directly — split the *real* de Rham cohomology using the complex structure. Start by actually walking through $b_1(X)=2g$ rather than just naming it: this is de Rham's theorem ($b_1=\dim H^1_{dR}(X;\mathbb{R})$) applied to the handle picture — cut the surface along $2g$ standard loops into a $4g$-gon, or build it up handle-by-handle with Mayer–Vietoris, and each handle contributes one independent pair of non-bounding loops. If this construction (or Mayer–Vietoris itself) isn't sitting ready to hand, that's completely fine — worth pausing and rebuilding it together rather than plowing past it; it's from Bott–Tu, but a book read once doesn't mean instant recall on demand.

Now split every smooth 1-form by type using nothing but the complex structure — no metric needed yet: locally $\alpha=\alpha^{1,0}+\alpha^{0,1}$, a $dz$-part and a $d\bar z$-part, pure linear algebra.

**Genuinely new material now** (this previews Huybrechts §3.2, still ahead in the reading, so it should be introduced as new, not glossed): the Hodge theorem gives every de Rham class a unique *harmonic* representative — "harmonic" meaning a Hodge-star/Laplacian condition that doesn't show up in Bott–Tu (that book is purely topological, no Riemannian metric involved) and isn't quite do Carmo's curvature either (a different use of the Laplacian). On a Riemann surface, harmonicity of $\alpha$ is exactly equivalent to $\alpha^{1,0}$ holomorphic and $\alpha^{0,1}$ anti-holomorphic (write out $d\alpha=0$, $d{*}\alpha=0$ in $z,\bar z$ and Cauchy–Riemann falls out on each piece separately — worth doing by hand once; cited here, not re-derived — it's the Hodge theorem, borrowed ahead of schedule). So harmonic 1-forms split as (holomorphic) $\oplus$ (anti-holomorphic), and complex conjugation is a real-linear bijection between the two halves — forcing equal dimension. Half of $2g$ is $g$.

> [!board] Board — topological derivation
> from Bott–Tu (walk through it, don't just cite it):
> $$b_1(X) = \dim H^1_{dR}(X;\mathbb{R}) = 2g \qquad\text{de Rham's theorem; each handle} \to \text{one independent loop-pair (Mayer–Vietoris)}$$
>
> type decomposition (complex structure only, no metric — elementary): $\ \alpha=\alpha^{1,0}+\alpha^{0,1}$
> $$dz = dx+i\,dy, \qquad d\bar z = dx - i\,dy$$
>
> genuinely new (previews Huybrechts §3.2):
> Hodge theorem (cited): every de Rham class has a unique harmonic representative
> harmonic $\alpha$ $\iff$ $\alpha^{1,0}$ holomorphic **and** $\alpha^{0,1}$ anti-holomorphic
> $$\Rightarrow\quad \{\text{harmonic 1-forms}\} = H^0(X,\Omega^1_X)\ \oplus\ \overline{H^0(X,\Omega^1_X)}$$
>
> conjugation $\omega\mapsto\bar\omega$: real-linear bijection between the two halves $\Rightarrow$ equal dimension
> $$\Rightarrow\quad \dim_{\mathbb{C}}H^0(X,\Omega^1_X) = \tfrac12 b_1(X) = \tfrac12(2g) = g$$

> [!board] Board — two anchors, make it tangible
> **Torus, $g=1$:** $X=\mathbb{C}/\Lambda$; $dx,dy$ generate $H^1_{dR}$ (one handle, two loops); $dz=dx+idy$ descends to the quotient, nowhere zero, holomorphic, unique up to scalar — $H^0(\Omega^1)=\mathbb{C}\cdot dz$, matching $g=1$.
>
> **Hyperelliptic curves, any $g$:** $y^2=\prod_{i=1}^{2g+1}(x-e_i)$ — holomorphic differentials are explicitly
> $$\frac{dx}{y},\ \frac{x\,dx}{y},\ \dots,\ \frac{x^{g-1}dx}{y} \qquad\text{— exactly }g\text{ of them}$$
> exercise: check $dx/y$ is actually finite at the points over infinity — not obvious at a glance, satisfying to verify by hand

> [!success] Payoff — say this out loud
> Two completely independent derivations of the same number: the residue pairing above (algebraic, §3) and the Hodge decomposition of real cohomology (topological/analytic, just now) — the dual-unlock pattern showing up *inside* a single fact, not just across separate theorems.

### 4. The obstruction is cohomology — two lenses, one group

**Say:** The Mittag-Leffler question — can a proposed pole data be realized — is fundamentally a cohomological question, tied to $H^1(X,\mathcal{O}(D))$ — exactly how gets sharpened precisely later in this section, once the subscheme structure of $D$ is on the board; for now, the point is just that $H^1(X,\mathcal{O}(D))$ is a single group with two genuinely different constructions, which is exactly why two independent proofs are possible. Algebraically: cover $X$ by small opens where $\mathcal{O}(D)$ is trivial, try to find compatible local sections, glue — the failure to glue is a Čech cocycle, and Čech $H^1$ measures precisely the failure that no adjustment of the local pieces can fix. Analytically: a smooth section solves $\bar\partial u=0$ exactly when it's holomorphic; asking whether every smooth candidate can be corrected to a holomorphic one is asking whether $\bar\partial u=f$ is always solvable, and the Dolbeault group $H^{0,1}_{\bar\partial}(X,\mathcal{O}(D))$ measures that obstruction. The Dolbeault theorem says these are canonically the same group. So "unlock the black box" has two literal routes: patch-and-glue, or solve-a-PDE — same target.

Worth a pause, not a passing remark: does this "cover $X$, glue local data, measure the failure with $H^1$" pattern look familiar from anywhere? It's the same Čech machinery behind the Čech–de Rham double complex — just with coefficients in $\mathbb{C}$ replaced by coefficients in the line bundle $\mathcal{O}(D)$. If that connection doesn't come immediately, that's completely normal — rebuild it here rather than assuming it should already be obvious.

> [!board] Board
> $$H^1(X,\mathcal{O}(D)) \quad\text{— one group, two constructions}$$
> Čech: cover $X=\bigcup U_i$, glue local sections, obstruction = cocycle not a coboundary
>
> Dolbeault: $\{\text{smooth }(0,1)\text{-forms valued in }\mathcal{O}(D)\}\ /\ \bar\partial\{\text{smooth sections of }\mathcal{O}(D)\}$
>
> Dolbeault theorem: $H^1_{\check{C}ech} \cong H^{0,1}_{\bar\partial}$ — same group, two computations

**A third derivation, and the sharp Mittag-Leffler criterion — via the subscheme structure of $D$ itself.** For $D$ effective, there's a cleaner route than either proof below, and it sharpens the loose "vanishing question" framing above into something precise and checkable. $D$, being effective, is literally a closed subscheme of $X$ — a finite-length scheme, points with multiplicity — with ideal sheaf $\mathcal{O}(-D)$: near a point with coefficient $n_P$, generated by $z^{n_P}$, exactly "vanish to order $\ge n_P$." So
$$0\to\mathcal{O}(-D)\to\mathcal{O}_X\to\mathcal{O}_D\to0$$
with $\mathcal{O}_D:=\mathcal{O}_X/\mathcal{O}(-D)$ the subscheme's own structure sheaf. Tensor by the line bundle $\mathcal{O}(D)$ — exact, since line bundles are locally free:
$$0\to\mathcal{O}_X\to\mathcal{O}(D)\to\mathcal{O}(D)|_D\to0$$
(middle term becomes $\mathcal{O}_X$ since $\mathcal{O}(-D)\otimes\mathcal{O}(D)=\mathcal{O}_X$; last term is $\mathcal{O}(D)$ restricted to the subscheme $D$). This is the same quotient sheaf as §2's $\mathcal{O}(D)/\mathcal{O}_X$, reached from the subscheme structure instead of by hand.

$D$ is $0$-dimensional, so $H^1(\mathcal{O}(D)|_D)=0$ — any coherent sheaf on a finite-length scheme has no higher cohomology. The sequence terminates:
$$0\to\mathbb{C}\to H^0(\mathcal{O}(D))\to H^0(\mathcal{O}(D)|_D)\xrightarrow{\delta} H^1(\mathcal{O}_X)\to H^1(\mathcal{O}(D))\to0.$$

Take dimensions — the alternating sum across *any* exact sequence of finite-dimensional vector spaces is zero, no need to chase kernels and images of $\delta$ individually:
$$1-\ell(D)+\deg D-g+h^1(D)=0 \quad\Rightarrow\quad \ell(D)-h^1(D)=\deg D+1-g.$$
Riemann–Roch, a third time — the whole divisor handled at once via its subscheme structure, no point-by-point induction needed.

Now sharpen the obstruction itself. Serre duality (§3) gives $H^1(\mathcal{O}_X)\cong H^0(X,K)^*$ — the *dual*, via the perfect residue pairing, not a bare isomorphism (worth being careful here — equating them instead of dualizing loses the pairing structure that makes the next step work). Dualizing $\delta$ turns it from a map into a **pairing**: $H^0(\mathcal{O}(D)|_D)\times H^0(X,K)\to\mathbb{C}$. And this pairing is nothing new: $H^0(\mathcal{O}(D)|_D)$ is exactly a choice of principal part (Laurent tail, bounded by $D$'s orders) at each point of $D$, and pairing one against $\omega\in H^0(K)$ gives $\sum_{P\in\operatorname{supp}D}\operatorname{Res}_P(p\cdot\omega)$ — §3's residue pairing again, not a new construction.

So, the sharp criterion, replacing the loose "vanishing question" from above: principal-part data $p$ (bounded by $D$) is realized by an actual global section of $\mathcal{O}(D)$ if and only if
$$\sum_{P\in\operatorname{supp}D}\operatorname{Res}_P(p\cdot\omega)=0\quad\text{for every }\omega\in H^0(X,K).$$
That's the classical Mittag-Leffler theorem for compact Riemann surfaces, made precise — not a blanket statement about $D$, but a checkable condition on the specific data being prescribed.

> [!board] Board — third Riemann–Roch proof + the sharp criterion
> $D\ge0$: closed subscheme, ideal sheaf $\mathcal{O}(-D)$
> $$0\to\mathcal{O}(-D)\to\mathcal{O}_X\to\mathcal{O}_D\to0 \ \xrightarrow[\text{exact, locally free}]{\otimes\,\mathcal{O}(D)}\ 0\to\mathcal{O}_X\to\mathcal{O}(D)\to\mathcal{O}(D)|_D\to0$$
>
> $D$ is $0$-dimensional $\Rightarrow H^1(\mathcal{O}(D)|_D)=0$
> $$0\to\mathbb{C}\to H^0(\mathcal{O}(D))\to H^0(\mathcal{O}(D)|_D)\xrightarrow{\delta} H^1(\mathcal{O}_X)\to H^1(\mathcal{O}(D))\to0$$
>
> alternating sum of dimensions $=0$:
> $$1-\ell(D)+\deg D-g+h^1(D)=0 \;\Rightarrow\; \ell(D)-h^1(D)=\deg D+1-g \qquad\textbf{Riemann–Roch, third proof}$$
>
> Serre duality (§3): $H^1(\mathcal{O}_X)\cong H^0(X,K)^*$ (dual, via the pairing — not a bare isomorphism)
> dualize $\delta$: pairing $H^0(\mathcal{O}(D)|_D)\times H^0(X,K)\to\mathbb{C}$, $\ (p,\omega)\mapsto\sum_P\operatorname{Res}_P(p\cdot\omega)$
>
> $$\textbf{sharp criterion:}\quad p\text{ realizable} \iff \sum_{P\in\operatorname{supp}D}\operatorname{Res}_P(p\cdot\omega)=0\ \ \forall\,\omega\in H^0(X,K)$$

> [!success] Payoff — say this out loud
> Riemann–Roch is now derivable two ways — this all-at-once subscheme argument, and §7's point-by-point induction (coming up, same conclusion from a different exact sequence) — plus the two independent proofs of the $\deg D>2g-2$ vanishing corollary right below. And Mittag-Leffler has gone from a vague "is $H^1$ zero" to an actual checkable criterion on the specific data being realized.

### 5. Algebraic proof: Riemann–Roch + Serre duality

**Say:** Target: $H^1(X,\mathcal{O}(D))=0$ whenever $\deg D > 2g-2$. By Serre duality (section 3), this is $H^0(X,\mathcal{O}(K-D))^*$, so it suffices to show $H^0(K-D)=0$. Now $\deg(K-D)=(2g-2)-\deg D<0$ by hypothesis. And this part is genuinely elementary, not cited: a divisor of negative degree can't have a nonzero section, because a nonzero section of $\mathcal{O}(E)$ corresponds to an effective divisor linearly equivalent to $E$, and effective divisors have degree $\ge0$. So $H^0(K-D)=0$, hence $H^1(D)=0$. Four lines, and the only outside input is Serre duality itself.

> [!board] Board
> Target: $H^1(X,\mathcal{O}(D)) = 0$ for $\deg D > 2g-2$
>
> Serre duality (§3): $H^1(X,\mathcal{O}(D)) \cong H^0(X,\mathcal{O}(K-D))^*$
>
> $$\deg(K-D) = (2g-2) - \deg D < 0 \qquad \text{[hypothesis]}$$
>
> Lemma (elementary), spelled all the way out: $s\in H^0(X,\mathcal{O}(E))\setminus\{0\}$ $\leftrightarrow$ rational $f$ with $\operatorname{div}(f)+E\ge0$
> $$\deg\big(\operatorname{div}(f)+E\big)\ge0 \;\Rightarrow\; \underbrace{\deg(\operatorname{div} f)}_{=\,0\ \text{(§2)}} + \deg E \ge 0 \;\Rightarrow\; \deg E \ge 0$$
> so $\deg E<0$ forces $f=0$ — this is §2's $\deg(\operatorname{div} f)=0$ doing the work directly, not a separate fact
>
> $$\Rightarrow\ H^0(K-D) = 0\ \Rightarrow\ H^1(D) = 0 \qquad \blacksquare$$

### 6. Analytic proof: Gauss–Bonnet + Hörmander's $L^2$ estimate

*Note:* corrected version — the object that needs a positively curved metric is $\mathcal{O}(D)\otimes K_X^{-1}$, not $\mathcal{O}(D)$ alone (a bare $\deg D>0$ threshold would be wrong — a single point on a genus-2 curve has $\deg P=1>0$ but $h^1(P)=g-1=1\ne0$).

**Say:** Same target, completely different method — this one never touches Serre duality. The key player is curvature: any Hermitian metric on a line bundle $L$ has curvature integrating to a fixed topological number, $\frac{i}{2\pi}\int_X\Theta_h=\deg L$, independent of the metric (Chern–Weil). Applied to $K_X$, this specializes to a theorem worth naming plainly: it's Gauss–Bonnet, restated for a line bundle instead of the tangent bundle — the same "total curvature is topological" idea, just one level more general. Worth actually restating the classical version on the board too and matching it up term by term, rather than asserting the connection and moving on. One notational trap to flag out loud: do Carmo's Gaussian curvature is usually written $K$, and this script's canonical divisor is $K_X$ — genuinely different objects, easy to conflate on sight, so curvature gets its own symbol $\kappa$ here.

Hörmander's $L^2$ existence theorem, one complex variable (Berndtsson's Lecture 1): if a weight has $\Delta\varphi>0$ everywhere, $\bar\partial u=f$ is always solvable with an $L^2$ bound — positivity alone gives it, no cohomology to check. This part is genuinely new (see the background map) and should be introduced as such. The object that needs this positivity isn't $\mathcal{O}(D)$ in isolation, it's $\mathcal{O}(D)\otimes K_X^{-1}$, because $(0,1)$-forms valued in a line bundle are really sections of that bundle twisted by $\overline{K_X}$. Since $\deg(D-K_X)=\deg D-(2g-2)>0$ by hypothesis, and curvature integrates to $2\pi$ times that positive number, the curvature can be redistributed (solve one linear equation for a correction weight) to be positive everywhere. Feed that into Hörmander: $\bar\partial$ is solvable for every smooth $(0,1)$-form valued in $D$, i.e. $H^{0,1}_{\bar\partial}(X,\mathcal{O}(D))=0$, i.e. $H^1(X,\mathcal{O}(D))=0$ by Dolbeault. Same threshold, same conclusion — Gauss–Bonnet supplied the $2g-2$, Riemann–Roch never appeared.

> [!board] Board
> Target (again): $H^1(X,\mathcal{O}(D))=0$ for $\deg D>2g-2$ — now via curvature
>
> Chern–Weil / Gauss–Bonnet: $\dfrac{i}{2\pi}\displaystyle\int_X \Theta_h = \deg(L)$, for **any** metric $h$ on any line bundle $L$
> applied to $K_X$: $\deg K_X = 2g-2$ — do Carmo's Gauss–Bonnet, one level up: $\int_X \kappa\,dA = 2\pi\chi(X)$
> ($\kappa$ = Gaussian curvature — deliberately not $K$, to keep it apart from the canonical divisor $K_X$)
>
> positivity needed: $\mathcal{O}(D)\otimes K_X^{-1}$ has a metric with curvature $>0$ everywhere
> possible $\iff$ $\deg(D-K_X) = \deg D - (2g-2) > 0$ ✓ (hypothesis) — redistribute curvature, solve one linear PDE
>
> Hörmander (Berndtsson, Lecture 1 — new, previews beyond current reading): $\Delta\varphi>0$ everywhere $\Rightarrow$ $\bar\partial u=f$ always solvable, $L^2$ bound
> $$\Rightarrow\ H^{0,1}_{\bar\partial}(X,\mathcal{O}(D)) = 0\ \Rightarrow\ H^1(X,\mathcal{O}(D)) = 0 \quad\text{(Dolbeault)} \qquad \blacksquare$$

**Sketch A — the curvature redistribution, concretely.** Start from any smooth metric $h_0$ on $\mathcal{O}(D-K_X)$, curvature density $\rho_0$ (so $\frac{i}{2\pi}\int_X\rho_0 = \deg(D-K_X) =: \delta > 0$). Look for a new metric $h=h_0e^{-\psi}$: its curvature is $\rho_0+\Delta\psi$. Want this constant and positive, so solve
$$\Delta\psi = c - \rho_0, \qquad c := \frac{2\pi\delta}{\operatorname{Area}(X)}.$$
This is solvable for the same reason a battery of charges with total charge zero can always be balanced by a potential: the right-hand side has mean zero, $\int_X(c-\rho_0) = 2\pi\delta - 2\pi\delta = 0$, and the Laplacian on a compact surface surjects exactly onto mean-zero functions (standard elliptic theory / Hodge theory for functions — its own small citable fact, much more elementary than the $\bar\partial$-existence theorem it's feeding into). New metric, curvature $\equiv c>0$ everywhere. Done — no PDE left unsolved by name only.

**Sketch B — Hörmander's estimate itself, in one variable (Berndtsson Lecture 1, verified — see the fetched notes).** The whole proof is two short steps, not a monolith:
- *Basic identity* (one integration by parts): for $\alpha$ compactly supported,
$$\int \Delta\varphi\,|\alpha|^2 e^{-\varphi} + \int\Big|\frac{\partial\alpha}{\partial\bar z}\Big|^2 e^{-\varphi} \;=\; \int |\bar\partial_\varphi^*\alpha|^2 e^{-\varphi}, \qquad \bar\partial_\varphi^*\alpha := -e^{\varphi}\frac{\partial}{\partial z}\big(e^{-\varphi}\alpha\big).$$
Since $\Delta\varphi>0$, drop the second (nonnegative) term on the left to get the a priori inequality $\int\Delta\varphi\,|\alpha|^2 e^{-\varphi} \le \int|\bar\partial_\varphi^*\alpha|^2 e^{-\varphi}$.
- *Turn the inequality into a solution* (Hahn–Banach + Riesz representation, pure functional analysis, no PDE technique): the inequality says a certain linear functional on the range of $\bar\partial_\varphi^*$ is bounded; extend it, represent it, and the representing element *is* the solution $u$, satisfying
$$\int |u|^2 e^{-\varphi} \;\le\; \int \frac{|f|^2}{\Delta\varphi}\,e^{-\varphi}.$$

**Sketch C — the actual meromorphic function, constructed (cutoff-and-correct).** This is the part that produces the object, not just the vanishing statement: local coordinate $z$ at $p$, cutoff $\chi\equiv1$ near $z=0$ supported in the chart,
$$\eta := \frac{\chi(z)}{z^{\,n}} \quad(\text{smooth section of }\mathcal{O}(D)\text{ away from }p,\text{ exact pole of order }n\text{ at }p),$$
$$\beta := \bar\partial\eta = \frac{\partial\chi}{\partial\bar z}\cdot\frac{1}{z^{\,n}} \quad(\text{smooth, supported in the transition annulus, extends smoothly over }p\text{ since }\chi\equiv1\text{ there}).$$
Solve $\bar\partial u=\beta$ via Sketch B (with the curvature-adjusted weight from Sketch A). Set $f:=\eta-u$: then $\bar\partial f = \beta-\beta=0$ away from $p$, so $f$ is holomorphic there, and it retains $\eta$'s pole at $p$ since $u$ is smooth. A genuine meromorphic section, built, not asserted.

> [!success] Payoff — say this out loud
> Same threshold, $2g-2$, reached two ways: duality + a dimension count, or curvature positivity + Gauss–Bonnet. Neither proof borrowed the other's tool. That's the dual-unlock strategy, working for real, on the first black box.

### 7. Riemann–Roch, stated — and actually derived, not cited

**Say:** Time to state Riemann–Roch properly, and it turns out to be fully derivable from what's already on the board — not a new citation. The tool: compare $D$ and $D-P$ for a point $P$. There's a short exact sequence $0\to\mathcal{O}(D-P)\to\mathcal{O}(D)\to k(P)\to0$ — a section of $\mathcal{O}(D)$ modulo one that vanishes at $P$ leaves exactly its value there, a 1-dimensional skyscraper. Euler characteristics are additive on exact sequences, so $\chi(D)=\chi(D-P)+1$ for every point $P$. Worth pointing out, gently, once this is on the board: the move "an exact sequence lets you compute one thing from two others" is the same habit Atiyah–Macdonald builds constantly for modules — length, rank, that kind of additivity — just one level up, for sheaves. If that parallel doesn't land immediately, no matter; the derivation here stands on its own regardless.

Start the induction at $D=0$: $\chi(\mathcal{O}_X)=\ell(\mathcal{O})-h^1(\mathcal{O})$, and $\ell(\mathcal{O})=1$ — a holomorphic function on compact connected $X$ attains its maximum modulus somewhere, forcing it constant — while $h^1(\mathcal{O})=g$ is exactly §3's special case. So $\chi(\mathcal{O}_X)=1-g$, and adding or removing points one at a time gives $\chi(D)=\deg D+1-g$ for *every* divisor $D$, not just where the correction term vanishes. Combine with Serre duality ($h^1(D)=\ell(K-D)$, §3) and $\chi(D)=\ell(D)-h^1(D)$: Riemann–Roch, in full.

> [!board] Board
> $$0\to\mathcal{O}(D-P)\to\mathcal{O}(D)\to k(P)\to0 \quad\Rightarrow\quad \chi(D)=\chi(D-P)+1 \quad\text{(any point }P\text{)}$$
>
> base case $D=0$: $\ \chi(\mathcal{O}_X)=\ell(\mathcal{O})-h^1(\mathcal{O})$
> $\ell(\mathcal{O})=1$ (max modulus principle, compact connected $X$ $\Rightarrow$ holomorphic functions are constant)
> $h^1(\mathcal{O})=g$ (§3, special case)
> $$\Rightarrow\ \chi(\mathcal{O}_X)=1-g$$
>
> induct (add/remove points one at a time):
> $$\chi(D) = \deg D+1-g \qquad\text{for every divisor }D$$
>
> Serre duality (§3): $h^1(D)=\ell(K-D)$, and $\chi(D)=\ell(D)-h^1(D)$
> $$\Rightarrow\quad \ell(D)-\ell(K-D) = \deg D+1-g \qquad\textbf{Riemann–Roch}\quad\blacksquare$$

### 8. Proving §1's equivalence — both ways, tools now in hand

**Say:** Now actually prove what §1 only defined. **Algebraically:** take any point $P\in X$. $\deg P=1>0$, so $P$ is ample — automatic for curves, no proof needed. Riemann–Roch (§7) says exactly how large a multiple gives the stronger embedding property: for $n\ge2g+1$, $\deg(K-nP)<0$ so $\ell(K-nP)=0$, and separating points/tangent vectors reduces to the same vanishing shifted by one or two points — $nP$ is very ample. The linear system $|nP|$ embeds $X\hookrightarrow\mathbb{P}^{n-g}$ holomorphically. Chow's theorem: any closed analytic subvariety of $\mathbb{P}^N(\mathbb{C})$ is automatically algebraic. So the image is a projective algebraic curve, and $X$ is biholomorphic to it — Hartshorne's definition, reached, with Riemann–Roch actually in hand this time rather than borrowed from nowhere.

**Analytically — a completely independent second construction, reusing none of the above:** "$P$ ample," in this language, means $\mathcal{O}(P)$ admits a metric with curvature strictly positive everywhere. That's Sketch A (§6) run on $D=P$: $\deg P=1>0$ gives a positive target, the same Poisson equation redistributes any starting curvature into something positive everywhere. Positivity alone isn't yet ampleness — for the embedding, Sketch B and C (§6) get applied again, to $nP$, to manufacture the separating sections. Same threshold falls out: separating points needs $\deg(nP-P-Q)>2g-2$, i.e. $n>2g$, same for tangent vectors, so $n\ge2g+1$ — §1's exact bound, reached with zero algebraic input.

> [!board] Board — algebraic
> $$P\in X\ \Rightarrow\ \deg P=1>0\ \Rightarrow\ P\text{ ample (automatic)}$$
> $$n\ge2g+1\ \Rightarrow\ nP\text{ very ample}\quad\text{(§7, Riemann–Roch)}$$
> $$\varphi_{|nP|}:X\hookrightarrow\mathbb{P}^{\,n-g}\quad\text{holomorphic embedding}\ \xrightarrow{\text{Chow}}\ \text{algebraic}$$
> converse (free): smooth projective $X/\mathbb{C}$ proper $\Rightarrow$ compact; scheme-smooth $\Rightarrow$ complex manifold

> [!board] Board — analytic, independent
> "$P$ ample" (analytic) $=$ $\mathcal{O}(P)$ admits a metric with curvature $>0$ everywhere
> $\deg P=1>0\ \Rightarrow$ Sketch A (§6) directly: $\Delta\psi=c-\rho_0$, target $c>0$
>
> separates points: $\deg(nP-P-Q)=n-2>2g-2\ \Rightarrow\ n>2g$
> separates tangents: $\deg(nP-2P)=n-2>2g-2\ \Rightarrow\ n>2g$
> $$\Rightarrow\ n\ge2g+1 \quad\text{— identical bound, via Sketches A+B+C, no algebra}$$

> [!success] Payoff — say this out loud
> §1's definition just got proved twice, from opposite directions, using nothing invented for the occasion — every tool was already on the board. That's what "black-box-first, unlock later" actually buys you.

<!-- next topic goes here -->
