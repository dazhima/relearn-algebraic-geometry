The going-up theorem says if a subring $S\subset R$  satisfies $R$ is integrally dependent on $S$, then every prime ideal $\mathfrak{p}\in Spec S$ comes from above (i.e. given by $\mathfrak{p}'\cap S$ for some $\mathfrak{p}'\in Spec R$).  In particular, if $R$ is a field, then under this assumption $S$ must be a field, and converse is also true.

* Step 1: Reduce to the local case. Assume the theorem is true when $S$ is a local ring.
	* Recall 
		* Proposition 3.11(iii) of Atiyah-Macdonald: Let $A$ be a ring and $M$ be a multiplicative closed set. Let $j:A\to M^{-1}A$ be the localization map. Then prime ideals of $M^{-1}A$ is one-to-one correspondent (via $j^{-1}$) with prime ideals of $A$ that *don't meet $M$*.
		* Proposition 3.3 of Atiyah-Macdonald: the localization $A\to M^{-1}A$ is exact. In particular, $j$ preserves intersection.
	* Let $M$ be the multiplicative closed set $S- \mathfrak{p}$. Then consider the localizations $S_M$ and $R_M$. Now $S_M$ is a local ring with only one prime ideal $j(\mathfrak{p})$ (which is also maximal). Then by the local case of theorem $j(\mathfrak{p}) = j(\mathfrak{p}')\cap S_M$ for some $j(\mathfrak{p}')$ of $R_{M}$. 
	* The correspondence implies $\mathfrak{p}'$ of $R$ dosen't meet $S-\mathfrak{p}$. So $\mathfrak{p}'\cap S = (\mathfrak{p}'\cap \mathfrak p) \cup (\mathfrak{p}'\cap(S-\mathfrak{p})) = \mathfrak{p}\cup \emptyset = \mathfrak{p}$. 
* Step 2: Prove the local case. Assume $S$ is local ring and $\mathfrak{p}$ be its unique maximal ideal. 
	* For every ideal $I$ of $R$, $I\cap S$ is an ideal of $S$ thus $I\cap S\subset \mathfrak{p}$. 
	* Claim: If $I$ is any maximal ideal of $R$, then $I\cap S = \mathfrak{p}$. Note that the claim implies step 2 because maximal ideals are prime.
		* To verify the claim we must show that $I\cap S$ is a maximal ideal of $S$, or $S/(I\cap S)$ is a field. 
		* Therefore we just need to show this is the case under the intergral dependence assumption.
		* Note that $S/(I\cap S)$ is a subring of the field $R/I$ by correspondence theorem.  Moreover, $R/I$ is integral over $S/(S\cap I)$. (to see this, just take any monic polynomial mod $I$).
* Step 3: Verify the special case: If $R$ is a field, $S$ is a subring of $R$ such that $R$ is integrally dependent on $S$, then $S$ must be a field.
		Proof. We must show that every $s\in S$ is a unit. Since $R$ is a field, we have $\frac{1}{a}\in R$, thus $\frac{1}{a^n} = b_0 + b_1 \cdot \frac{1}{a} + \cdots + b_{n-1}\cdot \frac{1}{a^{n-1}}$. Multiply by $a^n$ both side we get $1 = b_0 a^n + b_1 a^{n-1} + b_{n-1}a = a\cdot \text{ something }$. So $a$ is a unit.
* We have successfully reduced the theorem to the particular case, and the "converse" follows from the theorem. So the proof is complete.

## Noether normalization

Let $k$ be a field, $A$ be a finitely generated $k$-algebra. Then there exists $y_1,\dots,y_r\in A$  algebraically independent over $k$ and $A$ is integral over $k[y_1,\dots,y_n]$.



 



