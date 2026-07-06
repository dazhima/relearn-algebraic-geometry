# Homework 03

*MATH 464, Rice University, Spring 2020 · Due: Wednesday, February 5th, by 5pm. Each exercise is worth 10 points*

---

Due date: Wednesday, February 5th, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problems worth a total of at least 40 points (e.g.,
problems (1), (3), (4), and (6)) but should carefully read and understand the statements of all six
problems.
Math 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Hom, (co)-products and direct limits
**(1)** Let C be a category. For A, B \inOb(C), we will write HomC(A, B) for the set Mor(A, B)
of arrows between A and B.
(a) Assume that products exist in C. Show there is bijection of sets
HomC

X,
Y
i\inI
Yi

\simeq
Y
i\inI
HomC(X, Yi)
If C = A-Mod, then the above bijection is in fact an isomorphism of A-modules.
(b) Assume that coproducts exist in C. Show there is bijection of sets
HomC
 a
i\inI
Xi, Y

\simeq
Y
i\inI
HomC(Xi, Y )
If C = A-Mod, then the above bijection is in fact an isomorphism of A-modules.
**(2)** (Hom and direct limits) Let N be a finitely generated A-module, and let M = (Mi, µij) be
a directed system of A-modules. Prove that the natural map
lim
$$
-\toHomA(N, Mi) \toHomA
$$
N, lim
$$
-\toMi
$$

is injective. If N is finitely presented, show that this map is an isomorphism Hint: First
prove the statements when N is a finitely generated free module. Now say that N is finitely
presented by an exact sequence An \toAm \toN \to0. Consider the diagram:
/ lim
$$
-\toHomA(N, Mi)
$$

/ lim
$$
-\toHomA(Am, Mi)
$$

/ lim
$$
-\toHomA(An, Mi)
$$

/ HomA
N, lim
$$
-\toMi
$$

/ HomA
Am, lim
$$
-\toMi
$$

/ HomA
An, lim
$$
-\toMi
$$


**(3)** (Splitting a short exact sequence) Let
$$
0 \toM′ f-\toM
g-\toM′′ \to0
$$
be a short exact sequence of A-modules. Prove that the following two conditions are equiv-
alent:
(a) There exists an A-module homomorphism φ: M′′ \toM such that g ◦φ = idM′′.
(b) There exists an A-module homomorphism ψ: M \toM′ such that ψ ◦f = idM′.
If these conditions are satisfied, show that we have isomorphisms
$$
M = \operatorname{im} f \oplusker ψ = \ker g \oplusim φ,
and M \simeq M′ \oplusM′′.
$$
In this case, the sequence is said to split. The map φ is called a section and ψ is called a
retraction.
**(4)** Describe, as explicitly as possible, the following Hom groups:
$$
(a) HomZ(\mathbb{Z}/nZ, \mathbb{Z}/mZ), where m and n are positive integers.
(b) Homk[x] (k[x]/(xn), k[x]/(xm)), where m and n are positive integers.
$$
In addition, show that an element of order n in HomZ(Z3, Q/Z) can be represented by the
following data: a subgroup of Z3 of index n with cyclic quotient, together with a generator
for Z/nZ. [I.e., show that an element of order n in HomZ(Z3, Q/Z) gives rise to this data,
and that conversely, given this data you can construct an element of HomZ(Z3, Q/Z).]
---
## 2. Homological goodness
The following exercise, known as the 5-lemma, gets used all over the place.
**(5)** Consider a commutative diagram of A-modules and homomorphisms such that each row is
exact:
M1
/
f1

M2
/
f2

M3
/
f3

M4
/
f4

M5
f5

N1
/ N2
/ N3
/ N4
/ N5
(a) Prove that if f1 is surjective and f2, f4 are injective, then f3 is injective.
(b) Prove that if f5 is injective and f2, f4 are surjective, then f3 is surjective. (one approach
uses the Snake Lemma)
The cheap version of the 5-lemma that you’ll find in many texts is as follows: Suppose that
f1, f2, f4 and f5 are all isomorphisms.
Then f3 is an isomorphism.
This is a consequence of
what you’ve shown. An even cheaper version of the 5-lemma that you often see is the case where
M1 = N1 = M5 = N5 = 0 (the maps f1 and f5 are just the trivial maps then). In this case, the

result just says that given a morphism between two exact sequences1.
$$
/ M′
$$
/
f′

M
/
f

$$
M′′
$$
/
$$
f′′
$$

$$
/ N′
$$
/ N
$$
/ N′′
$$
/ 0
such that f′ and f′′ are isomorphisms, the map f is also an isomorphism.
But wait a minute! Consider the following exact sequences in the category of groups:
$$
/ \mathbb{Z}/2Z
$$
/
=

D8
$$
/ \mathbb{Z}/2Z \times \mathbb{Z}/2Z
$$
/
=

$$
/ \mathbb{Z}/2Z
$$
/ Q8
$$
/ \mathbb{Z}/2Z \times \mathbb{Z}/2Z
$$
/ 0
where D8 is the dihedral group with 8 elements, Q8 is the quaternion group, and the maps Z/2Z \to
D8 and Z/2Z \toQ8 are inclusions of the centers of the respective groups. Clearly Q8 and D8 are
not isomorphic! Conclusion: there is no map D8 \toQ8 that makes the above diagram commute!!!
The moral of the story is: don’t try to apply the 5-lemma to show that two objects are isomor-
phic unless you already have a candidate isomorphism map.
The goal of the next exercise is to give you practice disassembling a long exact sequence into
short exact sequences.
**Definition 2.1**. Let C be a class of A-modules. A function λ: C \toZ is additive if, for each short
exact sequence 0
$$
/ M′
$$
/ M
$$
/ M′′
$$
/ 0 of A-modules, we have
$$
λ(M′) -λ(M) + λ(M′′) = 0.
$$
For example, If A = k is a field, and C is the class of all finite dimensional k-vector spaces V ,
then V \mapstodimk V is additive (rank-nullity theorem).
**(6)** Let 0
/ M0
/ M1
/ · · ·
/ Mn
/ 0 be an exact sequence of A-modules
in which all the Mi and all the kernels of the maps belong to C. Show that if λ is an additive
function, then
n
X
i=0
$$
(-1)iλ(Mi) = 0.
$$
1A morphism between exact sequences is a collection of maps f ′, f and f ′′ as above such that the two squares in the
diagram commute.
