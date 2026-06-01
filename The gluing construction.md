Let $X$ be a topological space, $\bigcup_{i\in I}U_i$ be an open cover of $X$. Let $\mathcal{F}_i$ be a sheaf on $U_i$ for every $i$. Then if for every pair $i,j$, there is an isomorphism $\phi_{ij}:\mathcal F_i|_{U_i\cap U_j}\to \mathcal F_j|_{U_i\cap U_j}$ satisfying the *cocycle condition*:
* $\phi_{ij}\circ \phi_{jk} = \phi_{ik}$ on $U_i\cap U_j\cap U_k$;
Then there exists a sheaf $\mathcal F$ on $X$ that is *unique up to unique isomorphism* such that for every $i$ there is an isomorphism $\mathcal{F}_{U_i}\simeq \mathcal{F}_i$.

Example: 

1. a line bundle/vector bundle.
	Let $X$ be a complex manifold. A line bundle $L$ on $X$ is given by the following gluing construction:
	* An open cover $\bigcup_{i}U_i$ of $X$;
	* On every $U_i$, the sheaf of holomorphic functions $\mathcal{F_i} = \mathscr{O}(U_i)$ resp. sheaf of holomorphic maps $U_i\to \mathbb{C}^r$.
	* On $U_i\cap U_j$, a map $F_j|_{U_i\cap U_j}\to \mathcal{F_i}|_{U_i\cap U_j}$, $f_j(x) \mapsto g_{ij}(x)f_j(x)$. Note that this is an isomorphism of sheaves because $g_{ij}(x)$ is nozero. In the vector bundle case $g_{ij}$ are $GL_n$ -valued
	* It automatically satisfies the cocycle condition because it is a linear map on fibers.


2. The tatological sheaf on projective space $\mathbb{P}^n$.
	* Cover $\mathbb{P}^n$ by affine coordinates $U_i:=[y_i\neq 0]$.
	* On $U_i\cap U_j$, $g_{ij}(x) = \frac{x_i}{x_j}$.
		* A section on $U_i$ is a function to the line above by the point $(x_{0/i},\dots,x_{n/i})$. The line is parametrized by $x_i(x_{0/i},\dots,x_{n/i})$ on $U_i$ and by $x_j(x_{0/j},\dots,x_{n/j})$ on $U_j$. It follows that given its value on $U_j$, to obtain the value on $U_i$ one needs to devide by $x_j$ then multiply by $x_i$. That's how the $g_{ij}$ be obtained.

3. The tatological sheaf $\mathscr{O}_{\mathbb{P}(V)}(-1)$ on a projective bundle $\mathbb{P}(V)$.
	Let $V$ be a vector bundle on $X$, $\mathbb{P}(V)$ be its projective bundle.
	* Let $U_\alpha$ be the open cover of $X$ by trivial neighbourhoods of $V$.
		* The projective bundle is covered by affine coordinates $U_{\alpha/i}$.
		* On each $U_{\alpha/i}$ associate the sheaf 

