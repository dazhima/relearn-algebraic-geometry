# Lecture 19 — Localization continued

*MATH 464, Rice University, Spring 2020 · February 28, 2020*

---

## 1. Localization continued
Given an A-module homomorphism f : M \toN, we define an S-1A-module homomor-
$$
phism S-1f : S-1M \toS-1N by m
$$
s
\mapstof(m)
s
$$
.
It is easy to check that S-1(g ◦f) =
$$
(S-1g) ◦(S-1f) and that S-1 idM = idS-1M. Hence, we may think of S-1 as a functor from
the category of A-modules to the category of S-1A-modules.
**Proposition 1.1**. The functor S-1 is exact.
*Proof.* Let M
$$
f-\toM
$$
g-\toM ′′ be an exact sequence of A-modules. We must show that the
sequence
S-1M
S-1f
$$
---\toS-1M
$$
S-1g
$$
---\toS-1M ′′
is exact. We have g ◦f = 0 \RightarrowS-1g ◦S-1f = S-10 = 0 so that \operatorname{im} S-1f \subseteqker S-1g.
$$
Now let m
$$
s \inker S-1g, so that g(m)
$$
s
= 0 in S-1M ′′. This means there exists t \inS such
$$
that tg(m) = 0 in M ′′. But g is an A-module homomorphism, so g(tm) = 0, and hence
tm = f(m′) for some m′ \inM ′. So in S-1M we have
$$
m
$$
s = f(m′)
$$
ts
$$
= S-1f
$$
m′
ts

$$
\inim S-1f.
Hence \ker S-1g \subseteqim S-1f.
$$
$\square$
This proposition has important consequences:
$$
(1) If M ′ \subseteqM is a submodule, then S-1M ′ is naturally a submodule of S-1M.
(2) S-1(M/N) \simeq S-1M/S-1N as S-1A-modules (apply S-1 to the sequence 0 \toN \to
M \toM/N \to0).
(3) S-1(M\oplusN) \simeq S-1M\oplusS-1N (apply S-1 to the sequence 0 \toM \toM\oplusN \toN \to0
$$
and build a section).
**Corollary 1.2**. Localization preserves finite intersections: i.e., if M1 . . . , Mn \subseteqM are
submodules, then
n\
i=1
$$
S-1Mi = S-1
$$
 n\
i=1
Mi


*Proof.* The module ∩iMi is the kernel of the map M \to$\oplus$iM/Mi. Hence S-1∩i Mi

is the
$$
kernel of S-1M \toS-1\oplusi M/Mi
$$

$$
= \oplusiS-1M/Mi = \oplusiS-1M/S-1Mi. But this kernel is
visibly \capiS-1Mi as well.
$$
$\square$
Localization interacts as nicely as one might hope with tensor products.
**Proposition 1.3**. The S-1A-modules S-1M and S-1A$\otimes$A M are isomorphic. In fact, there
is a unique isomorphism
$$
f : S-1A \otimesA M \toS-1M
such that (a/s) \otimesm 7\toam/s
$$
*Proof.* The map S-1A × M \toS-1M sending (a/s, m) \mapstoam/s is A-bilinear, so we have
$$
an A-module map f : S-1A \otimesA M \toS-1M as in the proposition. The map f is clearly
$$
surjective.
I claim that every element of S-1A $\otimes$A M can be written in the form 1
s $\otimes$m. To see this
start with an element P
$$
i(ai/si) \otimesmi \inS-1A \otimesA M. Let s = \mathbb{Q}
$$
i si and ti = Q
i̸=j sj. Then
X
i
ai
si
$$
\otimesmi =
$$
X
i
aiti
s
$$
\otimesm =
$$
X
i
$$
s \otimesatim = 1
$$
s $\otimes$
X
i
atim.
Now suppose that f((1/s) $\otimes$m) = 0. Then m/s = 0 so there is a t \inS such that tm = 0.
But then
$$
s \otimesm = t
st \otimesm = 1
st \otimesmt = 1
ts \otimes0 = 0.
$$
Hence the map f is injective.
$\square$
**Corollary 1.4**. The module S-1A is flat over A.
*Proof.* If 0 \toM ′
$$
f-\toM is injective, then the map id \otimesf : S-1A \otimesA M ′ \toS-1A \otimesA M
$$
coincides, via the above isomorphism, with the map S-1M ′ \toS-1M obtained by applying
$$
the functor S-1. Since S-1 is exact, the map id \otimesf is injective.
$$
$\square$
Another useful consequence of this proposition is the following.
**Proposition 1.5**. There is a unique isomorphism of S-1A-modules f : S-1M$\otimes$S-1AS-1N \to
$$
S-1(M \otimesA N) sending (m/s)\otimes(n/t) 7\to(m\otimesn)/st. In particular, if p \subseteqA is a prime ideal,
$$
then we obtain a natural isomorphism of Ap-modules
$$
(M \otimesA N)p = Mp \otimesAp Np.
$$
*Proof.* Exercise.
$\square$
### 1.1. Localization and Hom. Localization interacts quite well with Hom in special cases.
Suppose that B is an A-algebra. Recall from the homework that the natural map
$$
B \otimesA HomA(M, N) \toHomB(M \otimesA B, N \otimesA B)
1 \otimesf 7\tof \otimesidB
$$

is an isomorphism of B-modules when B is flat over A and M is finitely presented. So take
B = S-1A and suppose that M is finitely presented. Then we obtain
$$
S-1 HomA(M, N) \simeq HomS-1(A) \operatorname{Hom}(S-1M, S-1N).
$$
---
## 2. Local Properties
A property P of an A-module M is said to be a local property if
$$
M satisfies P \LongleftrightarrowMp satisfies P for all p \inSpec(A).
$$
Likewise for maps of modules: a P is a local property of a module map f : M \toN if
$$
f : M \toN satisfies P \Longleftrightarrowfp : Mp \toNp satisfies P for all p \inSpec(A).
$$
Knowing that a property is local is a sort of blessing: it means that to check if M has P
we only need to check if each localization Mp has P. The localized modules often have
a “simple” structure; the problem of checking whether Mp has P may be genuinely more
tractable, at least in terms of book-keeping.
**Proposition 2.1** *(Being zero is a local property).* Let M be an A-module. The following
are equivalent:
(1) M = 0
$$
(2) Mp = 0 for every prime ideal p \subseteqA.
(3) Mm = 0 for every maximal ideal m \subseteqA.
$$
*Proof.* It is clear that (1)
$$
\Rightarrow
$$
(2)
$$
\Rightarrow
$$
(3). Suppose that (3) holds but that M \neq 0.
Let 0 \neq x \inM; the ideal Ann(x) is contained in some maximal ideal m of A. Consider
x/1 \inMm. Since Mm = 0, we know that ax = 0 for some a \inA -m. This contradicts the
inclusion Ann(x) \subseteqm.
$\square$
