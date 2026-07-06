# Lecture 33 — Local Dedekind Domains

*MATH 464, Rice University, Spring 2020 · April 15, 2020*

---

## 1. Local Dedekind Domains
In this lecture, we are going to prove (most of) the defineorem for Dedekind domains. If
you’d like a reference for this material, see Ch. 3 of Algebraic Theory of Numbers by Samuel,
or Ch. 1 of Algebraic Number Theory by Neukirch.
We start with the local case.
**Theorem 1.1**. Let A be a Noetherian local domain of dimension 1. Write m for the maximal
ideal of A and let k = A/m be the residue field of A. The following are equivalent:
(1) A is a discrete valuation ring;
(2) A is integrally closed;
(3) the ideal m is principal;
$$
(4) dimk(m/m2) = 1;
$$
(5) every nonzero ideal of A is a power of m;
(6) there exists x \inA such that every ideal of A is of the form (xk) for some k ≥0.
*Proof.* 
(1) =$\Rightarrow$(2): Let K be the fraction field of A, and suppose that x \inA is integral over A, so
that x satisfies a relation of the form
(1)
$$
xn + a1xn-1 + \cdot \cdot \cdot + an = 0
$$
where the ai \inA. We want to show that x \inA. By hypothesis, A is a discrete valuation
ring. This means there is a function v: A \toZ ∪{∞} such that
$$
• v(x) \geq0 for all x \inA and v(x) = ∞\Longleftrightarrowx = 0;
• v(xy) = v(x) + v(y) for all x, y \inA;
• v(x + y) \geqmin{v(x), v(y)}.
This function can be extended to K by setting v(x/y) := v(x) -v(y) for x, y \inA, and A
$$
can be recovered from knowledge of K and the extended function v because
$$
A = {x \inK : v(x) \geq0}.
$$

If x as in (1) is in A already we are done. Otherwise, we must have v(x) < 0, so v(x-1) > 0
$$
and x-1 \inA. But then we can rewrite (1) as
x = -(a1 + a2x-1 \cdot \cdot \cdot + anx1-n)
$$
which shows that x \inA, a contradiction. Hence x \inA after all, and A is integrally closed.
(2)
$$
\Rightarrow
$$
(3): Let 0 \neq a \inm. In the homework, you showed that under the hypotheses
of the theorem, there is an n such that mn \subseteq(a) and mn-1 ̸\subseteq(a). Choose b \inmn-1 such
that b /\in(a), and let x = a/b \inK = Frac(A). Note that x-1 /\inA since b /\in(a). Since
A is integrally closed by hypothesis, it follows that x-1 is not integral over A. We claim
this means that x-1m ̸\subseteqm: otherwise, if x-1m \subseteqm, then we can construct the following
A-module endomorphism:
$$
φx-1 : m \tom
y 7\tox-1y
$$
By the Cayley-Hamilton theorem, φx-1 satisfies a monic polynomial relation
$$
(φx-1)n + a1(φx-1)n-1 + \cdot \cdot \cdot + an = 0
$$
where equality above occurs in EndA(m). Applying both sides to any nonzero c \inm we
obtain
$$
x-nc + a1x-n+1c + \cdot \cdot \cdot + anc = 0,
$$
where ai \inA. Since A is a domain and c \neq 0, we may divide the above relation by c
and conclude that x-1 is integral over A, which is a contradiction. Hence, we must have
x-1m ̸\subseteqm. To conclude, note that by definition of x we have x-1m \subseteqA, and since the
ideal x-1m is not contained in the unique maximal ideal of A, we must have x-1m = A, i.e.,
m = (x), as desired.
$$
(3) \Rightarrow(4) \Rightarrow(5) \Rightarrow(6): this was done in the homework.
$$
(6) =$\Rightarrow$(1): We construct a valuation on A as follows: for any a \inA. Note that m = (xk)
for some k, but since (xk) \subseteq(x), we must have m = (x), by maximality of m. You showed
in the homework that mn \neq mn+1 for all n, so for every 0 \neq a \inA, there is a unique k ≥0
such that (a) = (xk). Define v: A \toZ ∪∞by setting v(0) = ∞and v(a) = k, and check
that this is a discrete valuation.
$\square$
We are finally in a position to prove most of the defineorem:
**Theorem 1.2**. Let A be a Noetherian domain of dimension 1 (recall this last condition
means that every nonzero prime ideal is maximal). The following conditions are equivalent:
(1) A is integrally closed.
(2) Every primary ideal of A is a power of a prime ideal.
(3) The localization Ap at a nonzero p \inSpec A is a discrete valuation ring.

*Proof.* 
(1) $\Longleftrightarrow$(3): Since being integrally closed is a local property, we have
A is integrally closed
$$
\LongleftrightarrowAm is integrally closed for all m \inMaxSpec(A)
\LongleftrightarrowAp is integrally closed for all (0) \neq p \inSpec(A)
\LongleftrightarrowAp is a discrete valuation ring for all (0) \neq p \inSpec(A)
$$
(3)
$$
\Rightarrow
(2): Let q \subseteqA be primary, and set p := r(q).
$$
Recall that if S \subseteqA is a
multiplication subset, then there is a one-to-one correspondence between prime ideals of A
that don’t meet S and prime ideals of S-1A, given by p \mapstoS-1p. With a little eﬀort, one
extends this to a one-to-one correspondence
{S-1p-primary ideals of S-1A} \to{p-primary ideals of A that don’t meet S}
$$
q 7\toS-1q
$$
Now, Ap is a dvr by hypothesis, so every ideal in Ap is a power of the maximal ideal pAp.
This means that qp = pnAp for some n. But since the above correspondence is one-to-one,
and since S-1q = S-1pn (with S = A \ p), we must have q = pn, and hence every primary
ideal is a power of a prime ideal, as desired.
$\square$
To complete the proof, we would need to introduce the concept of fractional ideals. For a
proof of numerous equivalent conditions for a Dedekind domain, see Hungerford’s Algebra,
VIII.6.10.
