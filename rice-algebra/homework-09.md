# Homework 09

*MATH 464, Rice University, Spring 2020 · Due: Wednesday, April 8th, by 5pm. Each exercise is worth 10 points*

---

Due date: Wednesday, April 8th, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problems 3 and 5 and three other problems.
Math 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Integrality
We begin with a warm-up problem. It’s individual parts are not related.
**(1)** (a) Show that φ: A \toB makes B into a finite A-algebra if and only if B is a finitely
generated A-algebra and B is integral over A. (We did this in class, so I guess this is
a freebie.)
(b) Show that unique factorization domains are normal.
The next problem shows that “integrality is preserved by extension of scalars.”
**(2)** Let B, B′ and C be A-algebras. Assume that B′ be an integral B-algebra via some map
φ: B \toB′ of A-algebras. Show that B′ $\otimes$A C is integral over B $\otimes$A C via the map φ $\otimes$idC
Here are two situations where integrality comes up. The first is resolution of curve singularities,
and the second is an important lemma that gets part of the subject of Invariant Theory started.
**(3)** Let A = k[X, Y ]/(Y 2-X2-X3). Prove that the normalization of A is k[t], where t = Y/X.
This says that the “aﬃne line is the resolution of a nodal singularity.”
**(4)** Let G be a finite group of automorphisms of a ring A, and let
$$
AG := {a \inA : g \cdot a = a for all g \inG}.
$$
This set is a subring of A, known as the subring of invariants of G. Prove that A is integral
over AG.
The “lying over theorem” has very important geometric consequences:
**(5)** Let B be an integral A-algebra via the map φ: A \toB. Show that the induced map on ring
spectra φ∗: Spec B \toSpec A is closed, i.e., it takes closed sets to closed sets.
Finally, we prove that being integrally closed is a local property.

**(6)** Let A \subseteqB be rings, and let C be the integral closure of A in B. Let S be a multiplicatively
closed subset of A. Prove that S-1C is the integral closure of S-1A in S-1B.
**(7)** Let A be an integral domain. Prove that the following are equivalent:
(a) A is integrally closed.
(b) Ap is integrally closed for each p \inSpec A.
(c) Am is integrally closed for each p \inMaxSpec A.
