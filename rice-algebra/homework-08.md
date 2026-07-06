# Homework 08

*MATH 464, Rice University, Spring 2020 · Due: Wednesday, April 1st, by 5pm. Each exercise is worth 10 points*

---

Due date: Wednesday, April 1st, by 5pm. Each exercise is worth 10 points.
Math 464 students should turn in complete problems worth a total of at least 40 points (e.g.,
problems (1), (3), (4), and (6)) but should carefully read and understand the statements of all eight
problems.
Math 564 students should do ALL the exercises.
Unless otherwise indicated, A is a commutative ring, with unit.
---
## 1. Localization
**(1)** (Local splitting criterion for exact sequences) Let 0 \toM′ \toM \toM′′ \to0 be an exact
sequence of A-modules.
(a) Show that the sequence splits if and only if the map HomA(M′′, M) \toHomA(M′′, M′′),
induced by the right hand map of the sequence, is surjective.
(b) Suppose that our sequence is locally split, in the sense that 0 \toM′
$$
p \toMp \toM′′
$$
p \to0
is a split exact sequence of Ap-modules for any prime ideal p \subseteqA. Assume that M′′ is
finitely presented. Show that the original exact sequence is split. [Hint: use part (a) and
your knowledge of how localization behaves with Hom.]
**(2)** (a) Show that if for every p \inSpec A, the localization Ap has no nonzero nilpotent elements,
then A has no nonzero nilpotent elements.
(b) Suppose that Ap is an integral domain for all p \inSpec A. Is A an integral domain?
**(3)** (Torsion-freeness is a “local property” over integral domains) Let S be a multiplicatively closed
subset of an integral domain A. Show that T(S-1M) = S-1T(M). Deduce that the following
are equivalent:
(i) M is torsion-free.
(ii) Mp is torsion-free for every p \in$\operatorname{Spec}(A)$.
(iii) Mm is torsion-free for every m \inMaxSpec(A).
---
## 2. Support of a module
**(4)** The support of an A-module M is the set
$$
Supp(M) := {p \inSpec A : Mp \neq 0}.
(a) For an ideal a \subseteqA, show that V (a) = Supp(A/a).
$$
(b) Let
$$
0 \toM′ \toM \toM′′ \to0
$$
be a short exact sequence of A-modules. Show that
$$
Supp(M) = Supp(M′) \cupSupp(M′′).
$$
Conclude that if M = L
$$
i\inI Mi, then Supp(M) = S
$$
i\inI Supp(Mi).
(c) If M is a finitely generated A-module, then show that Supp(M) = V (Ann(M)). This
means that Supp(M) is a closed subset of $\operatorname{Spec}(A)$.
---
## 3. Primary Decompositions
Continuing our story on aﬃne algebraic geometry, recall that the algebraic variety in Cn cut out
by the zero-set
$$
f1(x1, . . . , xn) = \cdot \cdot \cdot = fm(x1, . . . , xn) = 0,
$$
where the fi(x1, . . . , xn) are polynomials, is represented in algebraic geometry by the space
$$
X := \operatorname{Spec} \mathbb{C}[x1, . . . , xn]/(f1, . . . , fm).
$$
In fact, by the Hilbert Nullstellensatz, the maximal ideals of the ring C[x1, . . . , xn]/(f1, . . . , fm) are
of the form
$$
(¯x1 -a1, . . . , ¯xn -an),
where (a1, . . . , an) \inCn and fi(a1, . . . , an) = 0 for all i.
$$
These maximal ideals give what algebraic geometers call the closed points of X. The remaining
prime, nonmaximal ideals of C[x1, . . . , xn]/(f1, . . . , fm) are also very important in algebraic geom-
etry: they keep track of subvarieties of X of positive dimension. The following exercise says that
an algebraic variety of the form above always has finitely many irreducible components.
**(5)** Let a \subseteqA be a decomposable ideal in A (i.e., an ideal in A that has a primary decomposition).
Show that $\operatorname{Spec}(A/a)$ has finitely many irreducible components.
The following exercise is just calisthenics with primary decompositions.
**(6)** Let p1 = (x, y), p2 = (x, z), and m = (x, y, z) be ideals in the polynomial ring C[x, y, z]. Let
a = p1p2. Show that p1 ∩p2 ∩m2 is a minimal primary decomposition for a.
