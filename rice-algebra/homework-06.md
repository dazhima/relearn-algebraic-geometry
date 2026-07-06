# Homework 06

*MATH 464, Rice University, Spring 2020 · Due: MONDAY, February 24th, by 5pm. Each exercise is worth 10 points*

---

Due date: MONDAY, February 24th, by 5pm. Each exercise is worth 10 points.
Math 464 and 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Symmetric and Alternating Algebras
**(1)** Let f : V \toW be a linear transformation between two vector spaces of the same dimension
$$
n < ∞. We know the induced map Vn(f): Vn(V ) \toVn(W) is given by multiplication by a
$$
scalar. Prove that if [aij] is a matrix for f with respect to chosen bases of V and W, then this
scalar is
X
σ\inSn
sgn(σ)a1σ(1) · · · anσ(n).
**(2)** Let k be a field of characteristic diﬀerent from 2, and let V be a vector space over k. Prove
$$
that V \otimesk V = S2(V ) \oplusV2(V ).
$$
Of course, we are thinking of S2(V ) and V2(V ) as subvector spaces of V $\otimes$k V , as opposed
to quotient vector spaces. This result says that every 2-tensor may be written uniquely as a
sum of a symetric and an alternating tensor.
**Definition 1.1**. Let V be a k-vector space. An element α \inVk(V ) is called decomposible if it can
be expressed in the form v1 ∧· · · ∧vk.
**Example 1.2**. If k = R and V = R3 with the standard basis e1, e2, e3, then the element
e1 ∧e3 + e2 ∧e3
is decomposible since it can be expressed as (e1 + e2) ∧e3.
**(3)** (a) Show that if dimk(V ) ≤3, then every homogenous element in V(V ) is decomposable
(where a homogeneous element is one which is a sum of elements from Vk(V ) for some k).
(b) Let dimk(V ) > 3. Give an example of an indecomposable homogeneous element of V(V ).
