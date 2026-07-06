# Lecture 21 — Chain conditions (continued)

*MATH 464, Rice University, Spring 2020 · March 4, 2020*

---

## 1. Chain conditions (continued)
Recall that we introduced the following notion at the end of last class:
Let Σ be a set partially ordered by a relation ≤(i.e., ≤is reflexive, transitive, and x ≤y
$$
together with y \leqx imply x = y).
$$
**Proposition 1.1**. TFAE:
(1) Every increasing sequence x1 ≤x2 ≤· · · stabilizes (i.e., there is an N such that
$$
xn = xn+1 for all n \geqN).
$$
(2) Every non-empty subset of Σ has a maximal element.
*Proof.* Exercise.
$\square$
For example, we could take Σ to be the set of submodules of a fixed A-module M, partially
ordered by inclusion (i.e. ≤means \subseteq). Condition (1) above is the called the ascending chain
condition (a.c.c.). A module M satisfying this condition on its set of submodules is called
Noetherian. If instead, we take ≤to be \supseteqthen we get the descending chain condition (d.c.c),
and a module M satisfying this condition on its set of submodules is called Artinian.
Examples 1.2.
(1) A finite abelian group (as a Z-module) satisfies both a.c.c. and d.c.c.
(2) The ring Z, as a Z-module, satisfies a.c.c.
(it is a PID and (m) \subseteq(n) implies
$$
|n| \leq|m|), but not d.c.c.: for example, if a > 1 then (a) \supseteq(a2) \supseteq(a3) \supseteq\cdot \cdot \cdot does
$$
not stabilize.
(3) The Z-module G \subseteqQ/Z consisting of elements whose order is a power of a fixed prime
p satisfies d.c.c. but not a.c.c. To see this note that G has exactly one subgroup Gn
of order pn for each n ≥0, and G0 \subsetG1 \subsetG2 \subset· · · does not stabilize. Since the
Gn are the only proper subgroups of G, it is easy to see that d.c.c. is satisfied, by an
argument similar to that of Example (2).
(4) The ring k[x1, x2, · · · ], considered as a module over itself (so that submodule = ideal),
satisfies neither chain condition.
$$
(x1) \subset(x1, x2) \subset\cdot \cdot \cdot
$$

is an ascending chain that does not stabilize. On the other hand
(x1) ⊃(x2
1) ⊃· · ·
is a descending chain that does not stabilize.
Noetherian modules are more important than Artinian modules, because their submodules
are finitely generated:
**Proposition 1.3**. An A-module M is Noetherian if and only if every submodule of M is
finitely generated.
*Proof.* (=$\Rightarrow$). Let N \subseteqM be a submodule. Let Σ be the set of submodules of N that are
finitely generated; note that Σ \neq $\emptyset$since 0 \inΣ. By hypothesis, Σ has a maximal element
N0. If N0 ⊊N, then consider N0 + Ax for some x \inN \ N0. This is finitely generated and
contains N0, a contradiction. Thus N0 = N.
$$
(⇐=). Let M1 \subseteqM2 \subseteq\cdot \cdot \cdot be an ascending chain of M. Then N := S Mi is a submodule of
$$
M and is thus finitely generated, say by x1, . . . , xn, with xi \inMni. Let n = maxi ni. Then
N = Mn and the chain stabilizes.
$\square$
Noetherian and Artinian modules fit well together in exact sequences:
**Proposition 1.4**. Let 0 \toM ′
$$
f-\toM
g-\toM ′′ \to0 be an exact sequence of A-modules.
(1) M is Noetherian \LongleftrightarrowM ′ and M ′′ are Noetherian.
(2) M is Artinian \LongleftrightarrowM ′ and M ′′ are Artinian.
$$
*Proof.* We prove (1). Suppose that M is Noetherian. An ascending chain in M ′ (resp. M ′′)
gives rise to an ascending chain in M, which is stationary. Now suppose that M ′ and M ′′
are Noetherian. Take an ascending chain of submodules of M and produce ascending chains
in M ′ and M ′′ using f and g. Take n \inZ large enough so that both these chains stabilize;
then the chain for M must also be stable past n.
$\square$
**Corollary 1.5**. If Mi, 1 ≤i ≤n are Noetherian (resp. Artinian), then so is L Mi.
*Proof.* Induction on n, using the exact sequence
$$
0 \toMn \to
$$
n
M
i=1
Mi \to
n-1
M
i=1
Mi \to0.
and the Proposition.
$\square$
**Remark 1.6**. Note that the corollary is actually an if and only if, and you can again use
the proposition and induction to prove the converse. However, the direction stated in the
corollary tends to be more useful than the converse.
Let’s focus on the case where M = A, so that submodules = ideals. A ring A is said to
Noetherian (resp. Artinian) if it is so as an A-module, i.e., if it satisfies a.c.c. (resp. d.c.c.) on
ideals.

Examples 1.7.
$$
(1) A field is Noetherian and Artinian; ditto for \mathbb{Z}/nZ, n \neq 0.
$$
(2) Any PID is Noetherian because every ideal is finitely generated; e.g., Z is Noetherian,
k[x] is Noetherian.
(3) A subring of a Noetherian ring need not be Noetherian: the ring k[x1, x2, . . . ] is not
Noetherian, but it is a subring of its field of fractions!
A module M that is finitely generated over a Noetherian (resp. Artinian) ring A is Noe-
therian (resp. Artinian): M is a quotient of An (An is Noetherian by the Corollary 1.5 and
so M is Noetherian by Proposition 1.4).
---
## 2. Composition series
A chain of submodules of an A-module M is a sequence of the form
$$
M = M0 ⊃M1 ⊃\cdot \cdot \cdot ⊃Mn = 0
$$
(strict inclusions).
The length of the chain is n. A composition series of M is a maximal chain. This is equivalent
to saying that the quotient Mi-1/Mi is simple: i.e., it has no submodules except 0 and itself.
**Example 2.1**. Take M = Z/12Z as a Z-module. Then
$$
\mathbb{Z}/12Z ⊃2Z/12Z ⊃4Z/12Z ⊃0
$$
is a composition series. It’s usually written in the friendlier looking version:
$$
\mathbb{Z}/12Z ⊃\mathbb{Z}/6Z ⊃\mathbb{Z}/3Z ⊃0
$$
Here are two other composition series for the same module:
$$
\mathbb{Z}/12Z ⊃\mathbb{Z}/4Z ⊃\mathbb{Z}/2Z ⊃0
and
\mathbb{Z}/12Z ⊃\mathbb{Z}/6Z ⊃\mathbb{Z}/2Z ⊃0.
$$
Clearly, composition series are not unique! However, look at the quotients of the above
chains. Up to permutation and isomorphism the quotients are always Z/2Z, Z/2Z, Z/3Z.
This is a manifestation of the Jordan-H¨older theorem from finite group theory!
Here are some natural questions:
(1) What modules admit composition series? (Modules that are both Noetherian and
Artinian.)
(2) Does every composition series of M have the same length? (Yes.)
(3) Is there an analog of Jordan-H¨older for modules of finite length? (Yes.)
(4) If we work with vector spaces, what is the relation between length and dimension?
(They are equal.)
