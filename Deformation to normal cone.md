# Deformation to the Normal Cone

> **Goal.** Understand Fulton, _Intersection Theory_, Chapter 5. Sections marked `<!-- TODO -->` are left to fill in together.

---

## Module 1 — Graded Rings and the Rees Algebra

### The associated graded ring

Let $A$ be a ring and $I \subset A$ an ideal. The **associated graded ring** is

$$\text{gr}_I(A) = \bigoplus_{n \geq 0} I^n / I^{n+1}.$$

The ring structure: for $a \in I^m/I^{m+1}$ and $b \in I^n/I^{n+1}$, their product is the image of $ab \in I^{m+n}$ in $I^{m+n}/I^{m+n+1}$. One checks this is well-defined.

> **Note.** The degree-$0$ piece is $I^0/I^1 = A/I$, so $\text{gr}_I(A)$ is an algebra over $A/I$.

**Intuition.** An element $a \in A$ has _order $n$ along $I$_ if $a \in I^n$ but $a \notin I^{n+1}$. Its image in $I^n/I^{n+1}$ is its _leading term_ — the part of $a$ that is "exactly order $n$." The associated graded ring is the ring of all such leading terms, with no mixing between different orders.

### The (standard) Rees algebra

The **Rees algebra** (or **blow-up algebra**) of $I$ in $A$ is the subring

$$\text{Rees}(I) = \bigoplus_{n \geq 0} I^n t^n \;\subset\; A[t],$$

where $I^n t^n$ means the set ${a t^n : a \in I^n}$ sitting in polynomial degree $n$.

> **Warning.** Since $I \subsetneq A$ is a _proper_ ideal, the element $t$ itself is **not** in $\text{Rees}(I)$: the degree-$1$ piece is $It$, not $At$. This matters for fact (b) below.

**(a) Modding out by $t$:**

$$\text{Rees}(I)\,/\,(t) \;\cong\; \text{gr}_I(A).$$

Setting $t = 0$ kills the variable but each graded piece $I^n t^n$ survives as $I^n$ — except we can no longer "see" the ambient $I^{n-1}$, so the degree-$n$ piece becomes $I^n/I^{n+1}$.

<!-- TODO: verify this isomorphism degree by degree. Write down explicitly what the quotient map does to a general element a·t^n ∈ I^n·t^n. -->

### The extended Rees algebra

The standard Rees algebra is not quite the right object for the deformation story. The correct object is the **extended Rees algebra**:

$$R'(I) = \bigoplus_{n \in \mathbb{Z}} I^n t^n \;\subset\; A[t, t^{-1}], \qquad \text{where } I^n := A \text{ for all } n \leq 0.$$

In other words, we extend the filtration to negative degrees by setting $I^n = A$ for $n \leq 0$. 
* It looks like $\cdots \oplus A t^{-n}\oplus A t^{-n+1}\oplus \cdots At^{-1}\oplus A \oplus It \oplus I^2 t^2 \cdots$

Write $u = t^{-1}$ for the deformation parameter. Then

$$R'(I) = A[Iu^{-1}, u] \;\subset\; A[u, u^{-1}].$$

The degree-$(-n)$ piece is $A \cdot t^{-n} = A \cdot u^n$, and the degree-$n$ piece (for $n > 0$) is $I^n \cdot u^{-n}$.
* Note that $u^{-1}$ is not in $R'(I)$ because when $I$ is proper ideal, $It$ does not contain $1\cdot t$. So $R'(I)$ is just a graded $A[u]$-algebra but not $A[u,u^{-1}]$-algebra.
* Consequently, $\operatorname{Spec}R'(I)$ is an $\mathbb{A}_A^1$-scheme.

> **Why introduce $u^{-1}$?** The extended Rees algebra already contains $u^{-1} = t$, so it lives naturally over $\mathbb{A}^1_u = \text{Spec}(k[u])$, with $u$ as the deformation parameter.

- The map $A[u] \hookrightarrow R'(I)$, $f(u) \mapsto f(t^{-1})$, is simply the naive inclusion: $u = t^{-1}$ lives in the degree $-1$ piece of $R'(I)$ as $1 \cdot t^{-1}$, and $A$ sits in the degree-$0$ piece. The corresponding scheme morphism $\operatorname{Spec}(R'(I)) \to \operatorname{Spec}(A[u]) = Y \times \mathbb{A}^1_u$ is exactly what "living over $\mathbb{A}^1$" means.

- However $u^{-1} = t$ is **not** in $R'(I)$: the degree-$1$ piece is $I \cdot t \subsetneq A \cdot t$, so $t \notin R'(I)$ when $I$ is proper. Thus $R'(I)$ is an $A[u]$-algebra but not an $A[u, u^{-1}]$-algebra — it sees $u$ but not $u^{-1}$, consistent with the morphism landing in $\mathbb{A}^1$ rather than $\mathbb{G}_m$.

**(b) The two structural facts for $R'(I)$:**

**At $u = 0$ (mod out by $u$):**

$$R'(I)\,/\,(u) \;=\; A[u, Iu^{-1}]/(u) \;\cong\; \text{gr}_I(A).$$
* Let $S$ be a graded ring, $I$ be a homogeneous ideal. Then $S/I = \bigoplus_{n}S_n/(I\cap S_n)$.
* Setting $u = 0$: 
	* The degree $n>0$ piece are gone.
	* On the degree $u^{-n}$ piece, the quotient gets $I^n u^{-n}/(u)\cap I^nu^{-n}$. But what is $(u)\cap I^n u^{-n}$? It consists of degree $-n$ piece in the homogeneous ideal $(u)$. After multiplying by $u$ becomes degree $-n$, so this element must be in $I^{n+1}u^{-(n+1)}$. So we get $(u)\cap I^{n}u^{-n} = I^{n+1}u^{-n}$.
	* It follows that $I^nu^-n/(u)\cap I^nu^{-n} = I^nu^{-n}/I^{n+1}u^{-n} \simeq I^n/I^{n+1}$.

**Away from $u = 0$ (invert $u$, i.e. adjoin $t = u^{-1}$):**

$$R'(I)[t] \;=\; A[Iu^{-1}, u, t] \;=\; A[t, t^{-1}],$$
- The degree $-n$ part was $I^nu^{-n}$, degree $0$ part was $A$. After adding $t=u^{-1}$, the degree $-1$ part becomes $Au^{-1}+Iu^{-1}$ which is just $Au^{-1}$. This makes $1_A$ appear in degree $-1$ on $u$. This happens on every degree $-n$ on $u$, so the $I$ issue disappear and the result becomes $A[u,u^{-1}] = A[t,t^{-1}]$.

Inverting $u$ in $R'(I)$ gives $R'(I)[u^{-1}] = A[u, u^{-1}]$. Since the family is $\operatorname{Spec}(R'(I)) \to \operatorname{Spec}(A[u]) = Y \times \mathbb{A}^1_u$, restricting to the locus $\{u \neq 0\}$ corresponds exactly to inverting $u$, giving

$$\operatorname{Spec}(R'(I)[u^{-1}]) = \operatorname{Spec}(A[u, u^{-1}]) \longrightarrow \operatorname{Spec}(A[u, u^{-1}]) = Y \times (\mathbb{A}^1 \setminus \{0\}),$$

where the map is the identity. So over every point $u \neq 0$, the fiber is $\operatorname{Spec}(A) = Y$ — the family is constant, with no variation. The filtration by $I$, which was the only thing making $R'(I)$ smaller than $A[u, u^{-1}]$, becomes invisible once $u$ is invertible.

### Geometric punchline: the interpolation

The extended Rees algebra defines a flat family over $\mathbb{A}^1_u = \text{Spec}(k[u])$:

$$\text{Spec}(R'(I)) \;\longrightarrow\; \mathbb{A}^1_u,$$

whose fibers are:

|Value of $u$|Fiber|Ring|
|---|---|---|
|$u = 0$|$C_X Y$ (normal cone to $X$ in $Y$)|$\text{gr}_I(A)$|
|$u \neq 0$|$Y = \text{Spec}(A)$ (constant)|$A$|

**Why the grading does the work.** An element $a \in I^n \setminus I^{n+1}$ has _order $n$ along $X$_. In the generic fiber ($u \neq 0$), all elements of $A$ are on equal footing — the filtration is invisible. In the special fiber ($u = 0$), only the leading term of $a$ in $I^n/I^{n+1}$ survives. The normal cone is thus the scheme of "leading terms," the tangent cone to $Y$ along $X$.

- **Why the special fiber sees only leading terms.** Take $a \in I^n \setminus I^{n+1}$.
  - **In $R'(I)$**, the element $a$ appears at multiple $u$-degrees: as $a \cdot u^0$ in degree $0$, as $a \cdot u^{-1}$ in degree $-1$, ..., and finally as $a \cdot u^{-n}$ in degree $-n$ — but no further, since $a \notin I^{n+1}$. So $-n$ is the most negative degree at which $a$ appears, reflecting its order of vanishing along $I$.
  - **Setting $u = 0$**: the degree-$k$ piece of $R'(I)/(u)$ is $I^{-k}/I^{-k+1}$, so:
    - In degree $0$: $a$ maps to $0 \in A/I$, since $a \in I$. Killed.
    - In degree $-n$: $a \cdot u^{-n}$ maps to $[a] \in I^n/I^{n+1}$, which is nonzero precisely because $a \in I^n \setminus I^{n+1}$.
  - **Conclusion.** The special fiber does not see $a$ as an element of $A$ — it only sees its **leading term** $[a] \in I^n/I^{n+1}$, the part of $a$ at its exact order of vanishing along $X$. This is why $\operatorname{Spec}(\operatorname{gr}_I(A))$ is called the tangent cone: it is the scheme of leading terms, organized by order of vanishing along $I$.

This is exactly what the deformation space $M^\circ \to \mathbb{P}^1$ does geometrically: it is the trivial family $Y \times \mathbb{A}^1$ away from the special fiber, and degenerates to $C_X Y$ at the special fiber.

### Worked example

Let $A = k[x, y]$, $I = (x, y)$.

<!-- TODO: (a) Write down the first few graded pieces of Rees(I) and gr_I(A) explicitly. (b) Write down the extended Rees algebra R'(I) = A[Iu, u^{-1}] in this case. What does the fiber over u=0 look like? What does it look like for u ≠ 0? (c) Observe: gr_I(A) = k[x,y] again (a polynomial ring). Why? What does this say about the normal cone to the origin in A^2? -->

---

## Module 2 — The Normal Cone

### Definition

Let $Y = \text{Spec}(A)$ and $X = V(I) = \text{Spec}(A/I)$ a closed subscheme. The **normal cone** to $X$ in $Y$ is

$$C_X Y = \text{Spec}(\text{gr}_I(A)).$$

It comes with a projection $C_X Y \to X$ (since $\text{gr}_I(A)$ is an $A/I$-algebra).

### Why "cone"?

The grading on $\text{gr}_I(A)$ gives a $\mathbb{G}_m$-action on $C_X Y$. A **cone** is precisely a scheme with such an action (a $\mathbb{G}_m$-action scaling the fibers). The fixed locus of this action is the zero section $X \hookrightarrow C_X Y$.

### Example: smooth point

Let $X = {0} \hookrightarrow \mathbb{A}^n_k$, so $A = k[x_1, \ldots, x_n]$, $I = (x_1, \ldots, x_n)$.

<!-- TODO: compute gr_I(A). Show it is isomorphic to k[x_1,...,x_n] (a polynomial ring). Conclude C_X(A^n) ≅ A^n — the normal cone to a smooth point is the tangent space. -->

### Example: nodal curve

<!-- TODO (harder): 
let A = k[x,y]/(y^2 - x^2(x+1)), I = (x,y). Compute gr_I(A).
What does the normal cone look like? (It should be two lines, reflecting the two branches at the node.) -->

---

## Module 3 — Proj (Solidified)

_You already have the idea from your notes. This module makes it precise._

### Recap

Let $S = \bigoplus_{n \geq 0} S_n$ be a graded ring. $\text{Proj}(S)$ is the set of homogeneous prime ideals not containing all of $S_+ = \bigoplus_{n \geq 1} S_n$.

For a homogeneous element $f \in S_+$, the distinguished open $D_+(f) \subset \text{Proj}(S)$ is:

$$D_+(f) \cong \text{Spec}(S_{(f)}),$$

where $S_{(f)} = { s/f^n : s \in S_n, , n \geq 0 }$ is the degree-$0$ part of the localization $S[f^{-1}]$.



---

## Module 4 — The Blow-Up

### Definition

Let $Y = \text{Spec}(A)$, $X = V(I)$. The **blow-up** of $Y$ along $X$ is

$$\tilde{Y} = \text{Bl}_X Y = \text{Proj}(\text{Rees}(I)).$$

It comes with a projection $\pi: \tilde{Y} \to Y$.

### The exceptional divisor

The **exceptional divisor** is the preimage of $X$:

$$E = \pi^{-1}(X) = \text{Proj}(\text{gr}_I(A)) = P(C_X Y).$$

It is a Cartier divisor on $\tilde{Y}$ (this is one of the key properties of the blow-up).

### The birational map

$\pi$ is an isomorphism away from $X$: the restriction $\tilde{Y} \setminus E \xrightarrow{\sim} Y \setminus X$ is an isomorphism.

### Affine charts

The affine open sets of $\tilde{Y} = \text{Proj}(\text{Rees}(I))$ are $D_+(a)$ for generators $a \in I$. If $I = (a_1, \ldots, a_r)$, then

$$D_+(a_i) = \text{Spec}\left(A\left[\frac{a_1}{a_i}, \ldots, \frac{a_r}{a_i}\right]\right).$$

### Worked example: blowing up the origin in $\mathbb{A}^2$

Let $A = k[x,y]$, $I = (x,y)$, so $\text{Rees}(I) = k[x,y][xt, yt] \subset k[x,y,t]$.

<!-- TODO: (a) Write down the two affine charts D_+(x) and D_+(y). (b) Identify the exceptional divisor E in each chart. (c) Identify the transition functions on the overlap. (d) Verify E ≅ P^1. -->

---

## Module 5 — Projective Completion $P(C \oplus 1)$

### Projective bundle (recap from Fulton B.5)

For a vector bundle $E$ on $X$ with sheaf of sections $\mathscr{E}$:

$$P(E) = \text{Proj}(\text{Sym}(\mathscr{E}^\vee)).$$

On $P(E)$ there is a tautological line bundle $\mathscr{O}_E(-1) \hookrightarrow p^* E$ (the universal sub-line-bundle).

### The projective completion of a cone

Let $C = C_X Y$ be the normal cone, with graded ring $S^\bullet = \text{gr}_I(A)$. Define the **projective completion**:

$$P(C \oplus 1) = \text{Proj}(S^\bullet[z]),$$

where $z$ is a new variable of degree $1$.

The two key open/closed pieces:

|Locus|Description|Ring|
|---|---|---|
|${z \neq 0}$|Open dense copy of $C$|$\text{Spec}(S^\bullet_{(z)}) \cong \text{Spec}(S^\bullet_0[S^1/S^0]) \cong C$|
|${z = 0}$|"Hyperplane at infinity" $P(C)$|$\text{Proj}(S^\bullet)$|

<!-- TODO: verify the identification of the {z ≠ 0} locus with C by computing S^•[z]_{(z)}. -->

> **Why this matters.** In the fiber $M_\infty = \varrho^{-1}(\infty)$, one irreducible component is $P(C \oplus 1)$. The normal cone $C$ sits as a dense open inside it.

---

## Module 6 — Flatness (Minimal)

### Definition

A module $F$ over a ring $R$ is **flat** if $F \otimes_R -$ is an exact functor.

A morphism of schemes $f: X \to S$ is flat if $\mathscr{O}_{X,x}$ is flat over $\mathscr{O}_{S,f(x)}$ for all $x \in X$.

### Key examples

- Free modules are flat.
- Localizations $A \to S^{-1}A$ are flat (you know this from Atiyah-Macdonald).
- A product $Y \times S \to S$ is flat.

### Geometric meaning

A flat family $f: X \to S$ is one where the fibers "vary continuously" — no fiber suddenly gains or loses components in a set-theoretically invisible way. Flat families are precisely the ones where the cycle class $[X_s]$ is well-defined and constant.

### The one result needed from Fulton B.6.7

> _If $Y$ is flat over a non-singular curve $T$, then $\text{Bl}_X Y$ is also flat over $T$, for any $X \subset Y$._

This is the reason $\varrho: M \to \mathbb{P}^1$ is flat: $Y \times \mathbb{P}^1 \to \mathbb{P}^1$ is flat (it's a product), and $M$ is its blow-up.

---

## Module 7 — Chow Groups $A_k(X)$

### Cycles

A **$k$-cycle** on a scheme $X$ is a formal finite $\mathbb{Z}$-linear combination

$$\alpha = \sum n_i [V_i],$$

where each $V_i$ is an irreducible closed subvariety of dimension $k$. The group of $k$-cycles is $Z_k(X)$.

### Rational equivalence

Two cycles $\alpha, \beta \in Z_k(X)$ are **rationally equivalent** if $\alpha - \beta$ can be expressed as a sum of cycles of the form

$$[\text{div}(f)] = \sum_V \text{ord}_V(f) \cdot [V],$$

for rational functions $f$ on $(k+1)$-dimensional subvarieties of $X$.

<!-- TODO: unpack what ord_V(f) means. Why is this the right equivalence relation? (Think: fibres of a flat family over P^1 are rationally equivalent.) -->

### The Chow group

$$A_k(X) = Z_k(X) , / , (\text{rational equivalence}).$$

### Key operations

- **Proper push-forward** $f_*: A_k X \to A_k Y$ for $f: X \to Y$ proper.
- **Flat pull-back** $f^*: A_k Y \to A_{k+d} X$ for $f$ flat of relative dimension $d$.

### The exact sequence for a closed/open pair (Fulton §1.8)

For $Z \hookrightarrow X$ closed with open complement $U = X \setminus Z$:

$$A_k Z \longrightarrow A_k X \longrightarrow A_k U \longrightarrow 0.$$

<!-- TODO: why is this exact on the right but not on the left in general? Give a simple example. -->

---

## Module 8 — Gysin Map for Cartier Divisors

### Definition

Let $D$ be an effective Cartier divisor on $X$, with inclusion $i: D \hookrightarrow X$. The **Gysin map** (or intersection with $D$) is

$$i^*: A_{k+1}(X) \longrightarrow A_k(D).$$

### Formula on subvarieties

For an irreducible $(k+1)$-dimensional subvariety $V \subset X$:

- If $V \not\subset D$: then $V \cap D$ is a well-defined effective Weil divisor on $V$, and $i^*[V] = [V \cap D] \in Z_k(D)$.
- If $V \subset D$:

<!-- TODO: what is the correct definition in this case? (Hint: it involves the normal bundle / ideal sheaf of D in X restricted to V.) -->

### Use in the proof of Proposition 5.2

In the proof, $C = M^\circ \cap \varrho^{-1}(\infty)$ is a Cartier divisor on $M^\circ$. The map $i^*$ for this divisor is what takes $[M^\circ_{V \cap X} V]$ to $[C_{V \cap X} V]$.

<!-- TODO: trace this through the diagram in the proof once you've read §5.2. -->

---

## Module 9 — The Deformation Space $M$

### Construction

Let $X \hookrightarrow Y$ be a closed embedding, $C = C_X Y$ the normal cone. Define:

$$M = M_X Y = \text{Bl}_{X \times {\infty}}(Y \times \mathbb{P}^1).$$

This comes with a flat morphism $\varrho: M \to \mathbb{P}^1$ and a closed embedding $X \times \mathbb{P}^1 \hookrightarrow M$.

### The two fibers

**(1) Over $t \neq \infty$** (i.e., over $\mathbb{A}^1 = \mathbb{P}^1 \setminus {\infty}$):

$$\varrho^{-1}(\mathbb{A}^1) \cong Y \times \mathbb{A}^1.$$

Reason: $M \to Y \times \mathbb{P}^1$ is an isomorphism away from $X \times {\infty}$, and $X \times {\infty}$ does not meet $Y \times \mathbb{A}^1$.

**(2) Over $\infty$:**

$$M_\infty = \varrho^{-1}(\infty) = P(C \oplus 1) + \tilde{Y},$$

as a sum of two effective Cartier divisors, where $\tilde{Y} = \text{Bl}_X Y$ is the blow-up of $Y$ along $X$.

<!-- TODO: verify the fiber (2) using the affine computation from §5.1. Set Y = Spec(A), X = V(I), and identify P^1 - {0} with A^1 = Spec(K[T]). The blow-up M is Proj(S^•) where S^n = (I,T)^n. Check: inverting T gives Y × A^1; modding out T gives P(C ⊕ 1). Where does Ỹ come from? -->

### The complement $M^\circ$

Define $M^\circ = M \setminus \tilde{Y}$ (remove the blow-up component of the special fiber). Then:

- $\varrho^\circ: M^\circ \to \mathbb{P}^1$ is still flat.
- $M^\circ$ deforms the given embedding $X \hookrightarrow Y$ (at $t \neq \infty$) to the zero-section embedding $X \hookrightarrow C_X Y$ (at $t = \infty$).

---

## Module 10 — Specialization and Proposition 5.2

### The specialization map

Define

$$\sigma: Z_k Y \longrightarrow Z_k C, \qquad \sigma[V] = [C_{V \cap X} V],$$

and extend linearly.

The claim (Proposition 5.2) is that $\sigma$ **passes to rational equivalence**, hence defines a map

$$\sigma: A_k Y \longrightarrow A_k C.$$

### The proof strategy

The proof uses the flat family $M^\circ$ over $\mathbb{P}^1$. Since $\varrho^\circ$ is flat of relative dimension $\dim Y$:

$$\text{pr}^*[V] = [V \times \mathbb{A}^1] \in A_{k+1}(Y \times \mathbb{A}^1).$$

The variety $M^\circ_{V \cap X} V$ (the closure of $V \times \mathbb{A}^1$ in $M^\circ$) is a flat family over $\mathbb{P}^1$ whose fiber over any $t \neq \infty$ is $V$, and whose fiber over $\infty$ is $C_{V \cap X} V$. Therefore $[V]$ and $[C_{V \cap X} V]$ are rationally equivalent in $A_k(M^\circ)$.

### The diagram

The proof works via the diagram:

$$ A_{k+1}(C) \xrightarrow{i__} A_{k+1}(M^\circ) \xleftarrow{j^_} A_{k+1}(Y \times \mathbb{A}^1) \to 0 $$ $$ \quad i^* \downarrow \qquad\qquad\qquad\qquad \uparrow \text{pr}^* $$ $$ A_k(C) \longleftarrow!!-!!-!!-!!-!!-!!- A_k(Y) $$

<!-- TODO: once you have read the proof, annotate each arrow: - which map is the Gysin map i*? - which map is flat pull-back pr*? - why is the composite i* ∘ i_* = 0? (What is the normal bundle of C in M°?) - how does the induced map Coker(i_*) → A_k(C) give σ? -->

---

## Summary: The Big Picture

```
Y × P^1
   │
   │  blow up X × {∞}
   ▼
   M ──────────────────── ρ ──────► P^1
   │                                  │
   │  fiber over t ≠ ∞                │  Y × A^1  (trivial)
   │  fiber over ∞                    │  P(C⊕1) + Ỹ
   │
   └── M° = M \ Ỹ
           │
           │  deforms:
           │    t ≠ ∞  :  X ↪ Y  (given embedding)
           │    t = ∞  :  X ↪ C_X Y  (zero section)
```

The flat family $M^\circ \to \mathbb{P}^1$ is the engine that makes $\sigma$ well-defined on Chow groups: rational equivalence on $M^\circ$ descends to rational equivalence on the fibers.

---

_Placeholders marked `<!-- TODO -->` to be filled in together._