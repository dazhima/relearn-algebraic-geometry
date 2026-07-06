# Lecture 16 — More on the Alternating algebra

*MATH 464, Rice University, Spring 2020 · February 21, 2020*

---

A is a commutative ring with unit. All modules considered are A-modules.
---
## 1. More on the Alternating algebra
Recall that last class we ended in the middle of proving the following theorem:
**Theorem 1.1**. Let M be a free module of finite rank n over a (nonzero) ring A. Fix an
A-basis e1, . . . , en for M.
$$
(1) If 1 \leqr \leqn then Vr(M) is free over A and the elements
{ei1 \wedge\cdot \cdot \cdot \wedgeeir : i1 < i2 < \cdot \cdot \cdot < ir}
$$
form a basis of Vr(M) over A.
$$
(2) If r > n then Vr(M) = 0.
$$
(3) We have rkA
Vr(M) =
n
r

$$
.
$$
*Proof.* For (1), we completed the proof with r = n.
Now we do the case when r < n. Let I = (i1, . . . , ir) be a multi-index such that i1 < · · · <
ir. Suppose that there is a relation of the form
X
I
aIei1 ∧· · · ∧eir = 0.
Select any tuple J = (j1, . . . , jr) and let jr+1, . . . , jn be the indices that don’t appear in the
tuple. Now take the product of the relation above with ejr+1 ∧· · · ∧en. Only one term
survives, so we obtain
$$
aJej1 \wedge\cdot \cdot \cdot \wedgeejr \wedgeejr+1 \wedge\cdot \cdot \cdot \wedgeen = 0.
$$
Reordering the ei’s we obtain
±aJe1 ∧· · · ∧en = 0
and hence aJ = 0, since e1 ∧· · · ∧en \neq 0, by our work on the r = n case. Assertion (2) is
trivial, and assertion (3) follows immediately from (1) and (2) (the case r = 0 is easy: we
are dealing with an empty product, and 1 is a basis for V0(M) over A).
$\square$
Given a free module M over A of rank n, we define its determinant det(M) as the top
nonzero exterior power Vn(M).

**Exercise 1.2**. In an upcoming homework, you will show that if f : M \toM is an endo-
morphism of a free A-module of rank n < ∞, then ∧n(f) is scalar multiplication by the
determinant of the map.
The functor V is as nice as we can expect it to be on exact sequences, at least when all
modules involved are free of finite rank.
**Proposition 1.3**. Let
$$
0 \toM ′ \toM \toM ′′ \to0
$$
be an exact sequence of free A-modules of ranks r, n and s, respectively. Then there is a
natural isomorphism
φ:
r^
$$
M ′ \otimes
$$
s^
$$
M ′′ \to
$$
n^
M.
$$
In other words: det(M ′) \otimesdet(M ′′) \simeq det(M).
$$
Sketch of proof. Constructing φ is half the battle. Pick bases v1 . . . , vr of M ′ and w1, . . . , ws
$$
of M ′′. Let ui be a pre-image of wi in M for i = 1, . . . , s. Consider the A-bilinear map
$$
determined by
$$
det(M ′) \times det(M ′′) \todet(M)
$$
(v1 ∧· · · ∧vr, w1 ∧· · · ∧ws) \mapstov1 ∧· · · ∧vr ∧u1 ∧· · · ∧us.
Check that this map is well-defined and independent of the choice of u’s (use Exercise 1.2).
We get an induced map on the tensor products. Now check it’s an isomorphism.
$\square$
Similarly, we have the following theorem.
**Theorem 1.4**. Let M = M ′ $\oplus$M ′′ be a direct sum of finite free modules. Then for n > 0
we have
n^
(M) \simeq
M
$$
p+q=n
$$
p^
$$
(M ′) \otimesA
$$
q^
$$
(M ′′).
$$
Sketch of proof. The inclusions M ′ \toM and M ′′ \toM give rise to maps V(M ′) \toV M
$$
and V(M ′′) \toV M. We can put these maps together to get an A-bilinear map
$$
^
$$
(M ′) \times
$$
^
$$
(M ′′) \to
$$
^
M
(α, β) \mapstoα ∧β.
By the universal property of tensor product we get a natural map
^
$$
(M ′) \otimes
$$
^
$$
(M ′′) \to
$$
^
M
This map is graded, in the sense that for p = 0, . . . , n, it breaks up as
p^
$$
(M ′) \otimes
$$
n-p
^
$$
(M ′′) \to
$$
n^
M

By the universal property of direct sum these maps, together, are equivalent to a single
A-module homomorphism
M
$$
p+q=n
$$
p^
$$
(M ′) \otimes
$$
q^
$$
(M ′′) \to
$$
n^
(M).
Now pick bases to see that this map is an isomorphism.
$\square$
---
## 2. Symmetric and Alternating tensors
Starting from an A-module M, we constructed the symmetric algebra S(M) and the
alternating algebra V(M) as quotient algebras of the tensor algebra T(M). If A is a field
of characteristic zero, then there is a way to construct S(M) and V(M) as subalgebras of
T(M). This dual status of S(M) and V(M) is exploited to great eﬀect in the theory of
smooth manifolds.
We assume throughout this section that A is a field of characteristic zero.
There is left group action of Sr on T r(M) defined by
$$
σ \cdot x1 \otimes\cdot \cdot \cdot \otimesxr = xσ-1(1) \otimes\cdot \cdot \cdot \otimesxσ-1(r)
$$
σ \inSr.
**Definition 2.1**. An element x \inT r(M) is called a symmetric r-tensor if σ · x = x for all
$$
σ \inSr; it is called an alternating k-tensor if σ \cdot x = sgn(σ)x for all σ \inSr.
$$
**Example 2.2**. The 2-tensor x1 $\otimes$x2 + x2 $\otimes$x2 is symmetric, while x1 $\otimes$x2 -x2 $\otimes$x1 is
alternating.
The action of Sr on T r(M) stabilizes both ar and br, and thus we get induced actions on
Sr(M) and Vr(M). In fact, it is easy to check that
σ · x = x
for x \inSr(M) and
σ · x = sgn(σ)x
for x \in∧r(M).
We define operators
$$
Sym: T r(M) \toT r(M)
$$
x \mapsto
X
σ\inSr
σ · x
$$
Alt: T r(M) \toT r(M)
$$
x \mapsto
X
σ\inSr
sgn(σ)σ · x
called symmetrization and skew-symmetrization. If x is already symmetric (resp. alternating),
$$
then Sym(x) = r!x (resp. Alt(x) = r!x).
$$
Note that Sym(x) is a symmetric r-tensor and Alt(x) is an alternating r-tensor, so that
the image of Sym (resp. Alt) lies in the submodule of T r(M) consisting of symmetric (resp.
alternating) r-tensors. The operators don’t surject onto these submodules, but since we are

working in over a field of characteristic zero, if x is symmetric then we have
r! Sym(x) = x,
and if x is alternating we have
r! Alt(x) = x.
Hence, the maps
$$
r! Sym: T r(M) \to{symmetric r-tensors}
and
r! Alt: T r(M) \to{alternating r-tensors}
$$
are surjective A-module homomorphisms. It is easy to check that their respective kernels
are ar and br, and thus we obtain A-module isomorphisms
Sr(M)
$$
∼-\to{symmetric r-tensors}
and
$$
r^
(M)
$$
∼-\to{alternating r-tensors}.
$$
