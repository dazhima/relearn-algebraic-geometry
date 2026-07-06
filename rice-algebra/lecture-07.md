# Lecture 07 — Exact sequences (continued)

*MATH 464, Rice University, Spring 2020 · January 29, 2020*

---

## 1. Exact sequences (continued)
Last time we proved the following proposition.
**Proposition 1.1**. The sequence of A-modules
$$
0 \toM′
i-\toM
j-\toM′′
$$
is exact if and only if the induced sequence
$$
0 \toHomA(N, M′) i∗
-\toHomA(N, M)
$$
j∗
$$
-\toHomA(N, M′′)
$$
is exact for every A-module N.
This can be rephrased to say that exact sequences play nice with many functors. This is part of
the reason they are so useful. (Though one might say that the real fun begins when they don’t!)
Let me give you a concrete example. For any A-module N we can define two Hom-functors, as
follows. First we have the covariant functor
$$
HomA(N, -): A-Mod \toA-Mod
on objects: M 7\toHomA(N, M)
on morphisms: [M′
i-\toM] 7\to
$$

$$
i∗: HomA(N, M′) \toHomA(N, M), i∗(f) = i ◦f
$$

$$
.
$$
Next we have the contravariant functor
$$
HomA(-, N): A-Mod \toA-Mod
on objects: M 7\toHomA(M, N)
on morphisms: [M′
i-\toM] 7\to
$$

$$
i∗: HomA(M, N) \toHomA(M′, N), i∗(f) = f ◦i
$$

$$
.
$$
The forward direction of the proposition above (=$\Rightarrow$) says the functor HomA(N, -) takes left
exact sequences to left exact sequences. We say it is a left exact functor.
Similarly, one proves the following claim.
**Proposition 1.2**. The sequence of A-modules
M′
$$
i-\toM
j-\toM′′ \to0
$$
is exact if and only if the induced sequence
$$
0 \toHomA(M′′, N) i∗
-\toHomA(M, N)
$$
j∗
$$
-\toHomA(M′, N)
$$
is exact for every A-module N.

The forward direction of this last proposition (=$\Rightarrow$) is again summarized by the following slogan:
the contravariant functor HomA(-, N) is left exact.
---
## 2. The Snake Lemma
Now that we have gotten our hands dirty with exact sequences, we may as well prove a basic
theorem used ubiquitously in Mathematics.
**Lemma 2.1** *(Snake Lemma).* Suppose the following diagram of A-modules commutes and has exact
rows:
M′
i
/
f′

M
j
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
i′
/ N
j′
$$
/ N′′
$$
then there is a long exact sequence
$$
\ker f′ \toker f \toker f′′ d-\tocoker f′ \tocoker f \tocoker f′′
$$
I will define the map d for you, but it’s best if you prove this lemma for yourself.
For the
definition of d, say that m′′ \inker f′′. Since j is surjective, there is an m \inM such that j(m) = m′′.
$$
By the commutativity of the diagram, we have j′(f(m)) = f′′(j(m)) = f′′(m′′) = 0, so that
f(m) \inker j′ = \operatorname{im} i′. So pick n′ \inN′ such that i′(n′) = f(m), and define d(m′′) = n′ + \operatorname{im} f′. It’s
$$
important to check that this definition does not depend on the choices we made:
• First note that n′ is unique since i′ is injective.
• Suppose that m′′ = j(m1) = j(m2), so that j(m1 -m2) = 0. This means that m1 -m2 =
$$
i(m′) for some m′. Pick n′
$$
1 and n′
$$
2 so that i′(n′
1) = f(m1) and i′(n′
$$
2) = f(m2). We just
have to show that n′
$$
1 -n′
2 = 0 \incoker f′. For this, note that
i′(n′
1) = f(m1) = f(m2 + i(m′)) = f(m2) + f ◦i(m′) = i′(n′
2) + i′ ◦f′(m′) = i′(n′
2 + f′(m′)).
Since i′ is injective, we have n′
1 = n′
2 + f′(m′), which shows that n′
1 -n′
2 \inim f′, and so
$$
n′
$$
1 + \operatorname{im} f′ = n′
2 + \operatorname{im} f′ \incoker f′.
$$
This means that d is well-defined!
---
## 3. Finitely generated modules
To develop modules further, it will be advantageous to introduce some finiteness hypothesis. For
many mathematicians, the resulting theory is very useful and the hypotheses involved are not too
constraining.
**Definition 3.1**. An A-module M is free if M \simeq L
i\inI Mi for a collection of modules such that
$$
Mi \simeq A as A-modules. If I is a finite set of cardinality n, then M \simeq A \oplus\cdot \cdot \cdot \oplusA =: An, and we
$$
say that M is a finitely generated free A-module.

$$
Given a set {xi}i\inI \subseteqM, we can construct the map
$$
ξ :
M
i\inI
A(i) \toM
$$
ei = (. . . , 0, 1, 0, . . . ) 7\toxi
If the map ξ is surjective, we say the set {xi}i\inI is a system of generators for M, and the A-module
$$
ker ξ is called the module of relations. If I is finite, we say M is finitely generated. If in addition
ker ξ is itself finitely generated, we say M is finitely presented.
For a finitely presented module M we have an exact sequence of maps
$$
Ar φ-\toAg
ξ-\toM \to0,
$$
so the second map is surjective, and φ is given by an r×g matrix with entries in A where im φ = ker ξ.
