# Lecture 11 — Tensor products on maps

*MATH 464, Rice University, Spring 2020 · February 7, 2020*

---

## 1. Tensor products on maps
We’ve seen how to construct a tensor product of two A-modules. Now let’s see how to construct
a tensor product of maps of modules! Suppose that f : M \toM′ and g: N \toN′ are two A-module
homomorphisms. Define
$$
h: M \times N \toM′ \otimesA N′
$$
by h(x, y) = f(x) $\otimes$g(y) (extended by A-linearity). This map is bilinear and thus induces a map
$$
f \otimesg: M \otimesA N \toM′ \otimesA N′
x \otimesy 7\tof(x) \otimesg(y)
$$
This construction even respects composition: if f′ : M′ \toM′′ and g′ : N′ \toN′′ are two other
maps, then you can show that
$$
(f′ ◦f) \otimes(g′ ◦g) = (f′ \otimesg′) ◦(f \otimesg).
$$
This means that if we fix an A-module N, then tensoring with N is a functor, as follows:
$$
-\otimesA N : A-Mod \toA-Mod
on objects: M 7\toM \otimesA N =: T(M)
on morphisms: [f : M \toM′] 7\to
$$

$$
f \otimesidN : M \otimesA N \toM′ \otimesA N
$$

$$
.
$$
---
## 2. Adjointness of tensor and covariant Hom
Before we explore how the tensor functor plays with exact sequences, I want to mention a special
relationship that this functor has with the covariant Hom functor. Recall there is a bijection
$$
{A-bilinear maps M \times N \toP} \leftarrow\toHomA(M \otimesA N, P)
$$
There is also a bijection
$$
{A-bilinear maps M \times N \toP} \leftarrow\toHomA(M, HomA(N, P))
f -\to[m 7\to[fm : N \toP, n 7\tof(m, n)]]
[M \times N \toP, (m, n) 7\tog(m)(n)] \leftarrow-g
$$
Thus, we have a bijection
$$
HomA(M \otimesA N, P) \leftarrow\toHomA(M, HomA(N, P))
$$
These bijections are natural in M and P (look up what this means or ask me if you don’t know
and/or can’t find it). We say that -$\otimes$A N and HomA(N, -) are adjoint functors; or that -$\otimes$A N
is left adjoint to HomA(N, -); or that HomA(N, -) is right adjoint to -$\otimes$A N.

In order to see this relationship more clearly, write T(M) for M $\otimes$AN and U(P) for HomA(N, P).
Then the above bijection becomes
HomA(T(M), P) ←\toHomA(M, U(P)).
---
## 3. Tensor is right exact
Now we can prove the following theorem.
**Theorem 3.1**. The functor T is right exact.
*Proof.* Let
$$
M′ f-\toM
g-\toM′′ \to0
$$
be a right exact sequence of A-modules. For any A-module P, the contravariant functor HomA( · , U(P))
gives the left exact sequence
$$
0 \toHom(M′′, U(P))
$$
g∗
$$
-\toHom(M, U(P))
$$
f∗
$$
-\toHom(M′, U(P)).
$$
By adjunction of U and T, we obtain the exact sequence
$$
0 \toHom(T(M′′), P)
$$
(g$\otimes$idN)∗
$$
------\toHom(T(M), P)
$$
(f$\otimes$idN)∗
$$
------\toHom(T(M′), P).
$$
Since this sequence is exact for all A-modules P, it follows that
T(M′)
f$\otimes$idN
$$
----\toT(M)
$$
g$\otimes$idN
$$
----\toT(M′′) \to0
$$
is exact, i.e., that
$$
M′ \otimesA N
$$
f$\otimes$idN
$$
----\toM \otimesA N
$$
g$\otimes$idN
$$
----\toM′′ \otimesA N \to0
$$
is exact. Here we have used the fact that if the contravariant functor Hom(-, P) takes a short
sequence of A-modules to a left exact sequence (for any A-module P), then the short sequence we
started with is itself right exact.
$\square$
---
## 4. Tensor need not preserve injective maps
Last time we saw that, for a fixed A-module N, the tensor funtor T(M) := M $\otimes$A N is right
exact. Here’s an example that shows that tensor does not preserve injective maps.
**Example 4.1**. Let A = M = Z. Consider the map f : Z \toZ given by f(x) = 2x. This map is
clearly injective. Now tensor this map with Z/2Z to obtain
$$
f \otimesidZ/2Z : \mathbb{Z} \otimesZ \mathbb{Z}/2Z \toZ \otimesZ \mathbb{Z}/2Z
x \otimesy 7\to2x \otimesy
(extend by linearity). Now 2x \otimesy = x \otimes2y = x \otimes0, so f \otimesidZ/2Z is the zero map! However, the
$$
domain is Z $\otimes$Z Z/2Z \simeq Z/2Z, so our map can’t possibly be injective. Once again, torsion causes
problems with tensors.
**Definition 4.2**. An A-module N is said to be flat if for every injective map f : M \toM′ of
A-modules, the map
$$
f \otimesidN : M \otimesA N \toM′ \otimesA N
$$
is injective.

Equivalently, N is flat if the functor T transforms short exact sequences into short exact se-
quences. This is in turn equivalent to saying that T preserves any exact sequence (to se this last
equivalence, remember that any long exact sequence can be split up into short exact sequences).
**Example 4**. 1 says that Z/2Z is not flat as a Z-module.
**Example 4.3**. Let A = k be a field. Let V be a k-vector space. Then V is flat over k. I usually
remember this by the slogan tensoring over a field is exact. In fact, something much more general
is true: free modules are flat. To see this, first note that A is flat as an A-module thanks to the
isomorphism M $\otimes$A A \simeq M. Then, in the homework you’ll show that a direct sum of A-modules
M
i\inI
Mi is flat if and only if each of the Mi is flat.
Our claim now follows because a free module over A is isomorphic to a direct sum of copies of A.
**Example 4.4**. We will see in due course that if A is an integral domain, and K(A) is its field of
fractions, then K(A) is a flat A-module. So, for example, Q is a flat Z-module. This example is
best done in detail once we understand the concept of localization.
