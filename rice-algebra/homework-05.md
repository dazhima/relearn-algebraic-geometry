# Homework 05

*MATH 464, Rice University, Spring 2020 · Due: Wednesday, February 19th, by 5pm. Each exercise is worth 10 points*

---

Due date: Wednesday, February 19th, by 5pm. Each exercise is worth 10 points.
Math 464 and 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. A criterion for flatness
In this exercise you’ll prove the following criterion for flatness: an A-module M is flat if and only
if for every finitely generated ideal I of A, the map I $\otimes$A M \toA $\otimes$A M induced by the inclusion
I \subseteqA is injective. One direction, of course, is trivial.
The following fact may come in handy: let xi \inM and yi \inN and suppose that P xi $\otimes$yi = 0
in M $\otimes$N.
Then there exist finitely generated submodules M0 of M and N0 of N such that
$$
P xi \otimesyi = 0 in M0 \otimesN0.
$$
**(1)** (a) Show that if I $\otimes$A M \toA $\otimes$A M is injective for every finitely generated ideal I, then
$$
I \otimesA M \toA \otimesA M is injective for any ideal I.
$$
This result can be used to show the following: if I $\otimes$A M \toA $\otimes$A M is injective for
every finitely generated ideal I, and if K is a submodule of a free module F, then
K $\otimes$A M \toF $\otimes$A M is injective. We will take this for granted to complete the exercise
(the easiest way to show this is through Tor functors—we’ll come back to it).
(b) Under the assumption of part (a), suppose that φ: N \toN′ is an injective map of
A-modules. Prove that φ $\otimes$idM is injective and thus that M is flat. [Hint: write N′
as a quotient of a free module F (not necessarily finitely generated though):
$$
0 \toK \toF
f-\toN′ \to0.
Let J = f-1(φ(N)). Then the diagram
$$
/ K
/
=

J
/

N
/
φ

/ K
/ F
$$
/ N′
$$
/ 0
commutes and has exact rows. Apply · $\otimes$A M to the diagram and use part (a) and
either a diagram chase or the 5-lemma to conclude. You will need to use the fact from
part (a) that we are taking for granted.]
---
## 2. Torsion modules
An element x \inM of an A-module is a torsion element if Ann(x) \neq 0, i.e., if ax = 0 for some
a \neq 0. When A is an integral domain, the torsion elements of M form a submodule of M called
the torsion submodule T(M) of M. (Yes, it is annoying that the standard notation conflicts with
the tensor algebra notation.) If T(M) = 0, the module is said to be torsion-free. The point of the
following (easy—I promise!) exercise is to see that T( · ) is a covariant left-exact functor.
**(2)** Assume A is an integral domain. Show that
(a) If M is an A-module then M/T(M) is torsion-free.
$$
(b) If f : M \toN is a map of A-modules then f(T(M)) \subseteqT(N).
(c) If 0 \toM′ \toM \toM′′ \to0 is an exact sequence of A-modules, then
0 \toT(M′) \toT(M) \toT(M′′)
$$
is also exact.
---
## 3. Symmetric algebra and direct limit commute
**(3)** Let (Mi, µij) be a directed system of A-modules over a directed set I. By functoriality of
the symmetric algebra functor, (S(Mi), S(µij)) is also a directed system of modules. Show
there are natural A-module maps
φ: S
lim
$$
-\toMi
$$

\tolim
$$
-\toS(Mi)
and
$$
ψ: lim
$$
-\toS(Mi) \toS
$$
lim
$$
-\toMi
$$

that are inverse to each other.
