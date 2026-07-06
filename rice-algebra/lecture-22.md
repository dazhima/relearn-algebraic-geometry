# Lecture 22 — Composition series (continued)

*MATH 464, Rice University, Spring 2020 · March 6, 2020*

---

## 1. Composition series (continued)
### 1.1. Questions from last time.
(1) What modules admit composition series?
(2) Does every composition series of M have the same length?
(3) Is there an analog of Jordan-H¨older for modules of finite length?
(4) If we work with vector spaces, what is the relation between length and dimension?
### 1.2. Answers! First, we’ll show that every composition series has the same length. Write
ℓ(M) for the length of the shortest composition series of M (with the convention that ℓ(M) =
+∞if M does not have a composition series.)
**Proposition 1.1**. Suppose that M has a composition series. Then every composition series
of M has length ℓ(M), and every chain of submodules can be extended to a composition
series.
*Proof.* First, we’ll show that if N \subsetM is a proper submodule, then ℓ(N) < ℓ(M). Let
$$
M = M0 ⊃M1 ⊃\cdot \cdot \cdot ⊃Mn = 0
$$
be a composition series for M of minimal length n = ℓ(M) and consider the chain of sub-
modules of N given by
$$
N = N \capM0 ⊃N \capM1 ⊃\cdot \cdot \cdot ⊃N \capMn = 0.
Write Ni = N \capMi. Then Ni-1/Ni \subseteqMi-1/Mi, so either Ni-1/Ni = Mi-1/Mi or Ni-1 = Ni.
$$
Removing repeated terms in the chain (Ni) we see that ℓ(N) ≤ℓ(M) and equality is only
$$
possible if Ni-1/Ni = Mi-1/Mi for i = 1, . . . , n. For i = n we get Mn-1 = Nn-1; hence for
i = n -1 get Mn-2 = Nn-2, and so on until M0 = N0, i.e., M = N.
$$
Consequently, every chain of M has length at most ℓ(M): if
$$
M = M0 ⊃M1 ⊃\cdot \cdot \cdot ⊃Mk = 0
is a chain of length k, then ℓ(M) > ℓ(M1) > \cdot \cdot \cdot > ℓ(Mk) = 0, and so ℓ(M) \geqk. If this
$$
chain is a composition series, then we also have ℓ(M) ≤k by definition of ℓ(M) and hence
ℓ(M) = k (thus every composition series has length ℓ(M)). If the chain is not a composition

series, then its length is < ℓ(M). It is therefore not a maximal chain and we may insert
modules in it until its length in ℓ(M).
$\square$
Now we can answer the question of which modules have composition series.
**Proposition 1.2**. An A module M has a composition series if and only if it is Noetherian
and Artinian.
*Proof.* (=$\Rightarrow$): Every chain of submodules of M has bounded length so M satisfies a.c.c. and
d.c.c.
(⇐=): We construct a composition series as follows. Since M0 := M is Noetherian, it has a
maximal proper submodule M1. The set of submodules of M1 also has a maximal element
M2. Thus M0 ⊃M1 ⊃M2. Keep going. The process will stop because of the d.c.c. The
resulting chain is maximal by construction, so it is a composition series.
$\square$
Thus, the length of Noetherian and Artinian module is a well-defined integer. A module
with a finite composition series is known as a module of finite length.
Next, we’ll show a generalization of the Chinese remainder theorem that includes the
Jordan-H¨older theorem: the quotients of a composition series of M, counted with multiplic-
ity, are an invariant of M.
**Theorem 1.3**. Let M be a module of finite length, and let (Mi) denote a composition series
of M. Let p be a prime ideal of A. Then the sum of the localization maps M \toMp gives
an isomorphism of A-modules
α: M
$$
∼-\to
$$
M
p
Mp
where p runs over the maximal ideals of A such that Mi-1/Mi \simeq A/p for some i. In addition,
the number of Mi-1/Mi isomorphic to A/p is equal to the length of Mp as an Ap-module,
and is thus independent of the composition series chosen.
**Example 1.4**. Let’s go back to Z/12Z as a Z-module and see what this theorem says. Recall
we have the composition series
$$
\mathbb{Z}/12Z ⊃\mathbb{Z}/6Z ⊃\mathbb{Z}/3Z ⊃0
$$
The quotients in this composition series are Z/2Z (with multiplicity 2) and Z/3Z. Thus,
the prime ideals p \subsetZ that the proposition asks us to consider are 2Z and 3Z. What is
(Z/12Z)2Z? Localizing at 2Z means inverting odd numbers, so 12Z2Z = 4Z2Z (as sets!—write
each of them out to see this). Every odd number in Z/4Z is already invertible, so
$$
(\mathbb{Z}/12Z)2Z \simeq(Z2Z/12Z2Z) = (Z2Z/4Z2Z) \simeq(\mathbb{Z}/4Z)2Z = \mathbb{Z}/4Z,
and the localization map \mathbb{Z}/12Z \toZ/4Z is just n + 12Z 7\ton + 4Z. Similarly, (\mathbb{Z}/12Z)3Z =
$$
Z/3Z. The isomorphism in the theorem is just
$$
\mathbb{Z}/12Z \toZ/4Z \oplusZ/3Z
n + 12Z 7\to(n + 4Z, n + 3Z).
$$

This is the isomorphism from the Chinese remainder theorem! Also note that the length of
(Z/12Z)2Z = Z/4Z as a Z2Z module is 2, so there are two quotients in any composition series
$$
of \mathbb{Z}/12Z that are isomorphic to \mathbb{Z}/2Z. Similarly, the length of (\mathbb{Z}/12Z)3Z = \mathbb{Z}/3Z as a Z3Z
$$
module is 1, so there is one quotient in any composition series of Z/12Z that is isomorphic
to Z/3Z.
To prove Theorem 1.3, we need to know what simple modules look like. The following
lemma is also useful in other contexts.
**Lemma 1.5**. Let M \neq 0 be a simple A-module. Let p := Ann(M) \subseteqA be the annihilator
ideal of M. Then M ≃A/p as A-modules, and p is maximal. In addition, if m is a maximal
ideal of A, then
$$
Mm \simeq(A/p)m =
$$
(
M
if m = p
otherwise.
We’ll prove this lemma plus the theorem next time.
