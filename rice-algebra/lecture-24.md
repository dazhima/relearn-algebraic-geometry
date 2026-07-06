# Lecture 24 — Primary Decomposition in Noetherian rings

*MATH 464, Rice University, Spring 2020 · March 25, 2020*

---

## 1. Primary Decomposition in Noetherian rings
As usual, we assume our rings are commutative, with unit, unless otherwise stated.
We now come to the definition of a primary decomposition.
**Definition 1.1**. A primary decomposition of an ideal a \subseteqA is an expression
a =
n\
i=1
qi
for which the qi are primary ideals. Such a decomposition need not exist; the ideal a is
decomposable if it has a primary decomposition, and the decomposition is minimal if
(1) the r(qi) are distinct, and
$$
(2) for 1 \leqi \leqn we have qi \not\supseteqT
$$
j̸=i qj
If a primary decomposition exists, the second condition for minimality can always be
achieved by omitting superfluous terms. By the following lemma, the first condition can also
be achieved. So if a primary decomposition exists, it can always be reduced to a minimal
decomposition.
**Lemma 1.2**. If {qi}n
i=1 is a finite collection of p-primary ideals, then q := T
i qi is also a
p-primary ideal.
*Proof.* We have
r(q) = r
$$
\
$$
i
qi
!
=
$$
\
$$
i
r(qi) =
$$
\
$$
i
p = p.
To see that q is primary, suppose that xy \inq but that x /\inq. Then there is an i such that
xy \inqi but x /\inqi. Since qi is primary, we have y \inr(qi) = p = r(q), by what we’ve shown.
Thus q is p-primary.
$\square$
Before moving further with the theory of primary decomposition, we will establish that
primary decompositions always exists for Noetherian rings. So let A be a Noetherian ring.
An ideal a \subseteqA is irreducible if
$$
a = b \capc \Rightarrow(a = b or a = c).
$$

**Lemma 1.3**. Let A be a Noetherian ring. Every ideal is a finite intersection of irreducible
ideals.
*Proof.* Suppose the claim is false. Then the set P of ideals that are counterexamples to the
claim is not empty. Order this set by inclusions. Since A is Noetherian, P has a maximal
element. Call a one such element. Then a is not irreducible, because it is in P, which means
that we can write a = b∩c with a \subsetb and a \subsetc. By maximality, b, c /\inP. Hence these two
ideals are finite intersections of irreducible ideals, and then so is a, which is a contradiction.
So P is empty.
$\square$
**Proposition 1.4**. Let A be a Noetherian ring. Every irreducible ideal a \subseteqA is primary.
*Proof.* First we pass to the quotient ring A/a: a \subseteqA is irreducible if and only if 0 is
irreducible as an ideal of A/a. We will show that if 0 is irreducible in A/a, then 0 is primary
in A/a. It will follow that a is primary in A.
So assume that 0 is irreducible in A/a. Suppose that xy = 0 in A/a but x \neq 0. We want
to show that y is nilpotent. Consider the ascending chain
$$
\operatorname{Ann}(y) \subseteqAnn(y2) \subseteq\cdot \cdot \cdot
$$
Since A is Noetherian, A/a is also Noetherian, so this ascending chain stabilizes; say Ann(yn) =
Ann(yn+1) = · · · . We claim that (x) ∩(yn) = 0. To see this, let a \in(x) ∩(yn). Then since
a \in(x), we have ay = 0. On the other hand, since a \in(yn), we have a = byn. But then
$$
0 = ay = byn+1, so b \inAnn(yn+1) = \operatorname{Ann}(yn). Hence byn = 0 and a = 0. Since 0 is
irreducible, and x \neq 0, it follows that yn = 0, so y is nilpotent.
$$
$\square$
**Corollary 1.5**. Let A be a Noetherian ring. Every ideal a \subsetA has a primary decomposition.
Minimal primary decompositions are not unique! Here’s an example.
**Example 1.6**. Let A = k[x, y] and let a = (x2, xy). Then
$$
(x2, xy) = (x) \cap(x2, xy, y2) = (x) \cap(x, y)2
$$
and (x) is a prime ideal (hence primary) and r((x, y)2) = (x, y) is maximal, so (x, y)2 is also
primary. On the other hand, we have
$$
(x2, xy) = (x) \cap(x2, y)
$$
and we’ve seen before that (x2, y) is primary. So we have two distinct minimal primary
decompositions of the same ideal.
Not all is lost! Notice that the radicals of the primary ideals in both decompositions are
(x) and (x, y). It turns out that the set of radicals in a minimal primary decomposition is
unique.
---
## 2. The geometry of Primary Decomposition
Recall that to an ideal a \subseteqA we can associate a subspace V (a) \subsetSpec A. You’ve shown
that V (a) = V (r(a)), and V (b∩c) = V (b)∪V (c). Recall also that the quotient map A ↠A/a
gives rise to an inclusion Spec A/a ,\toSpec A which is a homeomorphism onto the image
V (a), so we will often just identify V (a) = Spec A/a.
**Example 2.1**. Let A = C[x, y], and let a = (x2, xy). Recall that
$$
a = (x) \cap(x, y)2
is a minimal primary decomposition of a. Let p1 = (x) and p2 = (x, y). Then p1 ⊊p2; the
$$
prime ideal p1 is isolated, while the ideal p2 is embedded. Geometrically, the quotient map
$$
\mathbb{C}[x, y] \toC[x, y]/(x2, xy)
$$
is surjective, so the corresponding map of prime spectra
$$
V (a) = \operatorname{Spec} \mathbb{C}[x, y]/(x2, xy) \toSpec \mathbb{C}[x, y] = A2
$$
is a homeomorphism onto its image. On the other hand
$$
V (a) = V (x) \cupV ((x, y)2)
$$
|
{z
}
=V (x,y)
= V (x). (set-theoretically)
So the picture you should have in your mind is that of the y-axis including into the xy-plane
(the complex plane, which we can’t actually draw but still choose to draw as the usual xy-
plane). Notice that set-theoretically, and hence topologically, we lost the information about
the ideal (x, y)2 in the primary decomposition, since this corresponded to V (x, y), the origin
sitting in the y-axis.
