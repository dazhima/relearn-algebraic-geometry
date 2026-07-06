# Lecture 31 — An equivalence of categories (continued)

*MATH 464, Rice University, Spring 2020 · March 29, 2019*

---

## 1. An equivalence of categories (continued)
Recall the contravariant functor
Γ: { algebraic sets V } \to{ Finitely generated, reduced k-algebras }
$$
V 7\tok[V ] = k[X1, . . . , Xn]/I(V )
[φ: V \toW] 7\to[φ∗: k[W] \tok[V ], f 7\tof ◦φ]
$$
**Theorem 1.1**. The functor Γ is an equivalence of categories.
*Proof.* We’ll show that Γ is essentially surjective and fully faithful. Last class, we showed
essential surjectivity, and that the map from the set Reg(V, W) of regular maps between two
algebraic sets V and W to the set Homk-alg(k[W], k[V ]) is injective.
Finally, we consider surjectivity. Let θ: k[W] \tok[V ] be a map of k-algebras, taking
$$
yi 7\toFi + I(V ). Define a map φ: V \tokm by
$$
(a1 . . . , an) \mapsto(F1(a1, . . . , an), . . . , Fm(a1, . . . , an))
We need to check that the image of φ is contained in W. Recall that
$$
W = {P \inkm : f(P) = 0 for all f \inI(W)}.
$$
So let f \inI(W). We must show that
f(F1(a1, . . . , an), . . . , Fm(a1, . . . , an)) = 0.
The left hand side is
f(θ(y1)(a1, . . . , an), . . . , θ(ym)(a1, . . . , an)) = f(θ(y1), . . . , θ(ym))(a1, . . . , an).
But θ is a k-algebra homomorphism! So we get
$$
θ(f(y1, . . . , ym))(a1, . . . , an) = θ(0)(a1, . . . , an) = 0.
$$
$\square$
---
## 2. Artinian rings
For this topic, we follow Atiyah & MacDonald, Chapter 8.

Recall A is an Artinian if it satisfies the d.c.c. on ideals. As Atiyah and MacDonald suggest,
“the apparent symmetry with Noetherian rings is misleading.” In fact, every Artinian ring
is a special kind of Noetherian ring. Artinian rings are just about the simplest rings that
are not fields.
Examples 2.1. Z/pnZ and k[x]/f n, where f is irreducible. In particular, k[x]/x2 is Artinian.
**Proposition 2.2**. In an Artinian ring every prime ideal is maximal
*Proof.* Let p be a prime ideal of A. Then B := A/p is an integral domain. Let 0 \neq x \inB;
$$
by the d.c.c. we have (xn) = (xn+1) for some n, so xn = xn+1y for some y \inB. Since x \neq 0
$$
and B is an integral domain, we may cancel xn to obtain 1 = xy. Hence x is a unit, and
thus B is a field. This shows that p is a maximal ideal.
$\square$
**Corollary 2.3**. In an Artinian ring the nilradical and the Jacobson radical coincide.
$\square$
We give a geometric interpretation of Proposition 2.2. A chain of prime ideals of a ring A
is a finite strictly increasing sequence of prime ideals:
$$
p0 \subsetp1 \subset\cdot \cdot \cdot \subsetpn;
$$
the length of the chain is n. The Krull dimension of A is the supremum of the lengths of
all chains of prime ideals in A. For example, a field has dimension 0; Z has dimension 1.
**Proposition 2**. 2 says that Artinian rings have dimension zero. The Krull dimension of A
coincides with the dimension of Spec A as a topological space. In particular, if A is a finitely
generated reduced k-algebra, the Krull dimension captures what you’d like the dimension
of the corresponding variety to be: the number of free variables in a Noether Normalization
decomposition of your algebra.
Next, we’ll show that an Artinian ring has a finite number of maximal ideals (!!). First,
we’ll need the following lemma.
**Lemma 2.4**. Let a1, . . . , an be ideals of a ring A, and let p \subseteqA be a prime ideal. Suppose
that T
$$
i ai \subseteqp. Then ai \subseteqp for some i.
$$
*Proof.* We prove the contrapositive. If ai ̸\subseteqp for all i, then we can find xi \inai \ p. Since
the ai are ideals, we have x1 · · · xn \in∩iai. On the other hand, since p is a prime ideal, we
$$
have x1 \cdot \cdot \cdot xn \notinp. Hence \capiai \not\subseteqp.
$$
$\square$
**Proposition 2.5**. An Artinian ring A has finitely many maximal ideals.
*Proof.* Consider the set of all finite intersections m1 ∩· · · ∩mr of maximal ideals in A. Since
A is Artinian, this set has a minimal element, say m1 ∩· · · ∩mn. This means that for any
maximal ideal m we have
$$
m \capm1 \cap\cdot \cdot \cdot \capmn = m1 \cap\cdot \cdot \cdot \capmn,
$$
so that m1 ∩· · · ∩mn \subseteqm. By Lemma 2.4, m \subseteqmi for some i. But since m is maximal, we
have m = mi.
$\square$

Next we’ll show that Artinian rings are actually a special class of Noetherian rings. To do
this, we’ll need a couple of lemmas.
**Lemma 2.6**. Let A be a ring in which the zero ideal is a product of (not necessarily distinct)
maximal ideals. Then A is Noetherian if and only if it is Artinian.
*Proof.* Consider the chain of ideals
A ⊃m1 ⊃m1m2 ⊃· · · ⊃m1 · · · mk = 0.
Each factor m1 · · · mi-1/m1 · · · mi is an A/mi-vector space. Hence d.c.c. $\Longleftrightarrow$a.c.c. for each
factor.
I claim that a.c.c. holds for each factor if and only if a.c.c. holds for A, and ditto for d.c.c.
This claim would show that a.c.c. for A holds if and only if d.c.c. holds for A, which is what
we want. I’ll prove the claim for a.c.c.
Suppose that a.c.c. holds for each factor. For i = k, this means that m1 · · · mk-1 satisfies
a.c.c. Hence the extremes of the short exact sequence
$$
0 \tom1 \cdot \cdot \cdot mk-1 \tom1 \cdot \cdot \cdot mk-2 \tom1 \cdot \cdot \cdot mk-2/m1 \cdot \cdot \cdot mk-1 \to0
$$
satisfy a.c.c.; consequently, m1 · · · mk-2 satisfies a.c.c. Repeat this argument to show that
m1 · · · mk-3, · · · , m1, A satisfy a.c.c. These steps can be reversed (recall that if 0 \toM ′ \to
M \toM ′′ \to0 is a short exact sequence of A-modules, then M ′ and M ′′ are Noetherian if
and only if M is Noetherian).
$\square$
**Lemma 2.7**. Suppose A is Artinian or Noetherian. Then the nilradical N(A) of A is nilpo-
tent, i.e., N(A)k = (0) for some k.
*Proof.* Exercise (or see the proofs in Atiyah & MacDonald, 7.15 for Noetherian and 8.4 for
Artinian).
$\square$
