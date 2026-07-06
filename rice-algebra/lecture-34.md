# Lecture 34 — Projective, Injective and Flat modules

*MATH 464, Rice University, Spring 2020 · April 17, 2020*

---

In this last part of the course, we turn to homological algebra.
I will be using Scott
Osborne’s book Basic Homological Algebra for the remainder of the course.
---
## 1. Projective, Injective and Flat modules
There are excellent reasons why one might want to study projective, injective and flat
modules (look up the Serre-Swan theorem in wikipedia, and the the notion of left-derived
functor). However, we will take a bit of a pedestrian approach in the course. I will define
these notions in terms of exactness of certain functors. Our goal will be to become familiar
with the properties these modules enjoy. As you learn more abstract mathematics, these
modules will come up again, and you’ll have no trouble dealing with them!
Let A be a commutative ring with unit, and let M be an A-module. Recall that the
functors Hom(M, •) and Hom(•, M) are both left exact. They don’t have to be exact on the
right, but if they are, then we give M special names. We’ve done something like this before:
the functor • $\otimes$A M is right exact; when it is exact, we said M is called flat.
**Definition 1.1**. An A-module P is projective if the covariant Hom(P, •) is an exact functor.
Since Hom(P, •) is already left exact, for P to be projective, all we are asking for is:
M
$$
φ-\toM ′′ \to0 is exact
\Rightarrow
$$
Hom(P, M)
φ∗
$$
-\toHom(P, M ′′) \to0 is exact.
$$
Equivalently, for a diagram
P
f

M
φ
$$
/ M ′′
$$
/ 0
with an exact row, we want there to exist a filler g
P
g
}
f

M
φ
$$
/ M ′′
$$
/ 0
that makes the diagram commute.
**Definition 1.2**. An A-module I is injective if the contravariant Hom(•, P) is an exact func-
tor.

Since Hom(•, P) turns exact sequences into left exact sequences, for I to be projective, all
we are asking for is:
$$
0 \toM ′
φ-\toM is exact
\Rightarrow
$$
Hom(M, I)
φ∗
$$
-\toHom(M ′, I) \to0 is exact.
$$
Equivalently, for a diagram
$$
/ M ′
$$
φ
/
f

M
I
with an exact row, we want there to exist a filler g
$$
/ M ′
$$
φ
/
f

M
g
}
I
that makes the diagram commute.
Recall that if {Mi}i\inI is a collection of A-modules, then L
i Mi is flat if and only if Mi is
flat for every i \inI. A similar result is true for projective and injective modules.
**Proposition 1.3**. Let {Mi}i\inI be a collection of A-modules. Then
(1) The module L
i Mi is projective if and only if Mi is projective for every i \inI.
(2) The module Q
i Mi is injective if and only if Mi is injective for every i \inI.
*Proof.* We’ll prove (1), the proof of (2) being quite similar. Let
$$
0 \toM ′ \toM \toM ′′ \to0
$$
be an exact sequence of A-modules. Then L
i Mi is projective if and only if the sequence
0 \toHom
M
i
Mi, M ′
!
\toHom
M
i
Mi, M
!
\toHom
M
i
$$
Mi, M ′′
$$
!
\to0
is exact. But this exact sequence is canonically equal to
0 \to
Y
i
$$
\operatorname{Hom} (Mi, M ′) \to
$$
Y
i
Hom (Mi, M) \to
Y
i
$$
\operatorname{Hom} (Mi, M ′′) \to0
$$
Exercise: this sequence is exact if and only if the sequences
$$
0 \toHom (Mi, M ′) \toHom (Mi, M) \toHom (Mi, M ′′) \to0
$$
are exact for all i \inI.
$\square$
We turn to a particular example: consider A as an A-module. Then HomA(A, M) \simeq M
via the map f \mapstof(1).
This observation implies that A is projective as an A-module.
Combining this with Proposition 1.3(1) we obtain the following corollary.

**Corollary 1.4**. Free modules are projective.
$\square$
**Corollary 1.5** *(Enough projectives).* Every A-module M is the homomorphic image of a
projective module.
*Proof.* Let F(M) be the free module with a generator for each element of M. Then there is
a surjection F(M) \toM \to0. The module F(M) is projective since it is free.
$\square$
In fact, we can say a little more:
**Corollary 1.6**. An A-module M is projective if and only if it is a direct summand of a free
module.
*Proof.* ( =$\Rightarrow$) Since M is projective, there is a filler arrow making the following diagram
commute
M
id

|
/ ker φ
/ F(M)
φ
/ M
/ 0
The filler gives a section making the exact sequence split, so that F(M) \simeq M $\oplus$ker φ as
A-modules.
( ⇐= ) Say M $\oplus$M ′ is free. Then it is also projective, but then by Proposition 1.3(1), both
M and M ′ are projective.
$\square$
**Corollary 1.7**. If an A-module M is projective, then M is flat.
*Proof.* Say M $\oplus$M ′ is free. Then M $\oplus$M ′ is flat, and so both M and M ′ are flat.
$\square$
Identifying injective modules is a little harder than identifying projective modules since
there is not such a close relationship between free modules and injective modules. It should
remind you of the criterion for flatness we proved in Problem Set #5.
**Proposition 1.8** *(Injectivity test/Baer’s criterion).* An A-module I is injective if and only
if there is a filler g for every diagram of the form
/ a
φ
/
f

A
g

I
where a is an ideal of A.
*Proof.* The forward ( =$\Rightarrow$) direction of this is trivial, so we prove the other direction.
Suppose that
$$
/ M ′
$$
φ
/
f

M
I

has an exact row. Consider the set
X
=
(
$$
(N ′, g′) : φ(M ′) \subseteqN ′ \subseteqM and 0
/ M ′
$$
φ
/
f

N ′
g′
}
I
commutes
)
Note that P \neq $\emptyset$because (φ(M ′), f ◦φ-1) belongs to it. Partially order P by restriction,
i.e., say that
$$
(N ′, g′) \geq(N ′′, g′′)
$$
if N ′ \subseteqN ′′ and g′′|N′ = g′. Note that chains in P are bounded: an upper bound for a chain
C is (N0, g0), where
N0 =
n[
$$
N ′ : (N ′, g′) \inC
$$
o
$$
and
g0(x) = g′(x) if x \inN ′
$$
By Zorn’s lemma, P has a maximal element.
Call this element (N, g).
We claim that
N = M. Suppose this is not the case so there is an x \inM \ N. Now we use the hypothesis:
$$
let a \subseteqA be the colon ideal (N : (x)), i.e.
a = {a \inA : ax \inN}.
$$
Consider the map of A-modules ¯f : a \toI defined by ¯f(a) = g(ax). By hypothesis this
$$
map extends to a map f : A \toI.
Now let N ′ = N + Ax and define g′ : N ′ \toI by
$$
g′(b + ax) = g(b) + f(a). Note that (N ′, g′) majorizes (N, g), which contradicts maximality
of the latter. Hence N = M.
$\square$
