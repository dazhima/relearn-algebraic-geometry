# Lecture 27 — Going up

*MATH 464, Rice University, Spring 2020 · April 1, 2020*

---

## 1. Going up
Recall the motivating question introduced last time: Suppose that A \subseteqB is a ring ex-
tension, and let p be a prime ideal of A. Is there a prime ideal q of B that restricts to p?
I.e., A ∩q = p? Since the map from A to B is an inclusion, we are asking that the con-
traction of q to A be p. In other words, is the induced morphism Spec B \toSpec A surjective?
We will see that integrality is the notion necessary to settle this question. To prove the
going-up theorem, we need a few properties of integral extensions which are worth knowing
in and of themselves.
**Lemma 1.1**. Let A \subseteqB be an integral ring extension. Let b \subseteqB be an ideal and set
$$
a = A \capb. Then B/b is integral over A/a.
$$
*Proof.* Let ¯x be an element of B/b and let x \inB be any lift of ¯x to B. By hypothesis, there
is a relation of the form
$$
xn + an-1xn-1 + \cdot \cdot \cdot + a0 = 0
$$
ai \inA.
Reducing modulo b we get a witness integrality relation for ¯x.
$\square$
**Lemma 1.2**. Let A \subseteqB be an integral ring extension. Let S \subseteqA be a multiplicatively
closed subset. Then S-1B is integral over S-1A.
*Proof.* Let x/s be an element of S-1B, with x \inB and s \inS. By hypothesis, there is a
relation of the form
$$
xn + an-1xn-1 + \cdot \cdot \cdot + a0 = 0
$$
ai \inA.
Dividing this relation by sn we obtain
x
s
n
$$
+ an-1
$$
s
x
s
n-1
$$
+ \cdot \cdot \cdot + a0
$$
sn = 0
ai
$$
sn-i \inS-1A,
$$
which is a witness integrality relation for x/s over the ring S-1A.
$\square$
The following will also be useful to us when we prove the weak Nullstallensatz.
**Lemma 1.3**. Let A \subseteqB be an integral ring extension of domains. Then B is a field if and
only if A is a field.

*Proof.* ( =$\Rightarrow$) Let x \inA \ {0}. Then x \inB \ {0}, and since B is a field, we have x-1 \inB.
By hypothesis there is a relation of the form
$$
(x-1)n + an-1(x-1)n-1 + \cdot \cdot \cdot + a0 = 0
$$
ai \inA.
Multiplying by xn we obtain
$$
1 + x(an-1 + \cdot \cdot \cdot + a0xn-1) = 0
Thus -(an-1 + \cdot \cdot \cdot + a0xn-1) is a multiplicative inverse for x, and it is visibly in A, so A is
$$
a field.
( ⇐= ) Let x \inB \ {0}. Since B is integral, there is a relation of the form
$$
xn + an-1xn-1 + \cdot \cdot \cdot + a0 = 0
$$
ai \inA.
Since B is a domain, we may assume, without loss of generality, that a0 \neq 0 (if it were 0, we
could cancel out whatever power of x divides the left hand side of the above relation). But
then
$$
x(xn-1 + an-1xn-2 + \cdot \cdot \cdot + a1) = -a0
and since A is a field, -(xn-1 + an-1xn-2 + \cdot \cdot \cdot + a1)/a0 is a multiplicative inverse for x.
$$
$\square$
**Lemma 1.4**. Let A \subseteqB be an integral ring extension. Let q \inSpec B and set p = A ∩q \in
Spec A. Then q is maximal if and only if p is maximal.
*Proof.* By Lemma 1.1, the extension B/q is integral over A/p, and both rings are domains
since p and q are prime. By Lemma 1.3 B/q is a field if and only if A/p is a field.
$\square$
**Theorem 1.5** *(Baby Going up/Lying Over Theorem).* Let A \subseteqB be an integral ring
extension, and let p be a prime ideal of A. Then there exists a prime ideal q in B such that
$$
A \capq = p.
$$
*Proof.* The idea is to localize the situation. By Lemma 1.2, Bp is integral over Ap, and the
latter is a local ring. We have a commutative square
A
i
/
α

B
β

Ap
ip
/ Bp
Let n be a maximal ideal of Bp. Then by Lemma 1.4, m := Ap ∩n is a maximal ideal of Ap;
this latter ring being local, we must have m = pAp. Take q = β-1(n). By the commutativity
$$
of the above square, we have A \capq = α-1(m) = p.
$$
$\square$
**Corollary 1.6** *(Going up).* Let A \subseteqB be an integral ring extension. Let
$$
p1 \subseteq\cdot \cdot \cdot \subseteqpn
$$
be a chain of prime ideals of A, and let
$$
q1 \subseteq\cdot \cdot \cdot \subseteqqm
$$

be a chain of prime ideals of B, with m < n and such that A ∩qi = pi. Then this last chain
can be extended to a chain of prime ideals of B such that A ∩qi = pi for i = 1, . . . , n.
*Proof.* An easy induction reduces us to the case where m = 1 and n = 2. By Lemma 1.1,
the extension B/q1 is integral over A/p1. Apply the Baby version of Going up to the ideal
p2 \subseteqA/p1. This gives a prime ideal q2 \subseteqB/q1 such that A/p1 ∩q2 = p2. The ideal q2
corresponds to a prime ideal q2 of B containing q1, and it is easy to check that A∩q2 = p2.
$\square$
I point out the following theorem mainly to make you aware that there is a corresponding
result for extending descending chains of ideals. You’ll notice that there are a number of
additional hypotheses, and the proof turns out to be more technical than that of the Going
Up Theorem.
If you’re interested, you can read more (including the proof) in Ch. 5 of
Atiyah-Macdonald.
**Theorem 1.7** *(Going Down).* Let A \subseteqB be an integral ring extension of integral domains
with A normal. Let
p1 \supseteq· · · \supseteqpn
be a chain of prime ideals of A, and let
q1 \supseteq· · · \supseteqqm
be a chain of prime ideals of B, with m < n and such that A ∩qi = pi. Then this last chain
can be extended to a chain of prime ideals of B such that A ∩qi = pi for i = 1, . . . , n.
