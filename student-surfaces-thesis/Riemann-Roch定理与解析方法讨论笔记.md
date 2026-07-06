
# Riemann-Roch 定理与代数几何中的解析方法

> 讨论背景:紧黎曼面上的 Riemann-Roch 定理(对应 Hartshorne GTM52 第四章 Curves 的相关内容),重点关注了除子、线丛、Riemann-Roch 公式,以及贯穿其中的解析方法(Kodaira 嵌入定理、上同调阻碍、Mittag-Leffler 问题)。

---

## 1. 除子(Divisor)与主除子

设 $X$ 是紧黎曼面(等价地,亏格 $g$ 的光滑射影代数曲线)。

**除子**是 $X$ 上点的形式有限和:
$$D = \sum_i n_i p_i, \quad n_i \in \mathbb{Z}, \ p_i \in X$$

**度数**定义为 $\deg D = \sum_i n_i$。

对一个亚纯函数 $f: X \to \mathbb{P}^1$(不恒为零),定义它的除子
$$\operatorname{div}(f) = \sum_{p} \operatorname{ord}_p(f) \cdot p$$
这样的除子称为**主除子(principal divisor)**。

### 引理(全纯映射的局部标准型)

设 $f: X \to Y$ 是两个黎曼面之间的非常值全纯映射,$p \in X$,$f(p) = a$。则存在以 $p$ 为原点的局部坐标 $z$ 和以 $a$ 为原点的局部坐标 $w$,使得 $f$ 局部写作
$$w = z^e$$
其中正整数 $e = e_p(f)$(称为 $f$ 在 $p$ 处的**局部重数**或**分歧指数**)由 $f$ 在 $p$ 处唯一决定。当 $a \neq \infty$ 时 $e_p(f) = \operatorname{ord}_p(f - a)$;当 $a = \infty$ 时 $e_p(f) = \operatorname{ord}_p(1/f)$。

**证明**:在任一局部坐标下 $f$ 可写作幂级数 $f(z) - a = c_e z^e + c_{e+1}z^{e+1} + \cdots$($c_e \neq 0$,$e < \infty$ 因为 $f$ 非常值,由解析延拓/恒等定理 $f-a$ 不能恒为零)。因子提取 $e$ 次方根:$u(z) := (c_e + c_{e+1}z + \cdots)^{1/e}$ 在原点附近全纯且非零(被开方的函数在小邻域内不取零值,可取全纯单值分支)。令 $\tilde z := z\cdot u(z)$,则 $\tilde z$ 在原点处的导数为 $u(0) = c_e^{1/e} \neq 0$,由反函数定理它是一个合法的局部坐标变换,且 $f - a = \tilde z^{\,e}$。$\blacksquare$

### 定义:$n_f(a)$

对 $a \in \mathbb{P}^1$,由 $X$ 紧、$f$ 非常值可知 $f^{-1}(a)$ 是离散闭集,从而有限,定义
$$n_f(a) := \sum_{p \in f^{-1}(a)} e_p(f)$$
即"按重数计数的原像个数"。

### 命题 1.0($n_f$ 是常数)

$n_f(a)$ 不依赖于 $a \in \mathbb{P}^1$,把这个公共值记作 $\deg f$。

**证明**:固定 $a$,设 $f^{-1}(a) = \{p_1,\dots,p_k\}$,$e_i := e_{p_i}(f)$。由局部标准型引理,取两两不交的邻域 $D_i \ni p_i$ 及 $V_i \ni a$,使 $f|_{D_i}: D_i \to V_i$ 在坐标下就是 $z_i \mapsto z_i^{e_i}$。

集合 $X \setminus \bigcup_i D_i$ 是紧集且不含 $f^{-1}(a)$ 中的点,故 $f(X\setminus\bigcup D_i)$ 是不含 $a$ 的紧集(从而闭集)。令
$$V := \Big(\bigcap_i V_i\Big) \setminus f\Big(X\setminus\bigcup_i D_i\Big),$$
这仍是 $a$ 的开邻域,且满足 $f^{-1}(V) \subset \bigcup_i D_i$(即 $V$ 外没有别的原像点跑进来)。

对任意 $a' \in V$,考察每个 $D_i$ 的贡献:
- 若 $a' = a$(即 $w_i = 0$):方程 $z_i^{e_i} = 0$ 只有 $z_i=0$ 一个解,局部重数 $e_i$,贡献 $e_i$。
- 若 $a' \neq a$(即 $w_i \neq 0$):方程 $z_i^{e_i} = w_i$ 在 $D_i$ 内恰有 $e_i$ 个互异解(相差单位根),每个解处 $f$ 局部双全纯(导数非零),重数为 $1$,共贡献 $e_i \times 1 = e_i$。

两种情形贡献都是 $e_i$,求和得 $n_f(a') = \sum_i e_i = n_f(a)$ 对所有 $a' \in V$ 成立,即 $n_f$ 在 $a$ 处局部常值。由 $a$ 的任意性 $n_f$ 处处局部常值,而 $\mathbb{P}^1$ 连通,故 $n_f$ 是常数。$\blacksquare$

### 命题 1.1(主除子的度数为零)

若 $f$ 是紧黎曼面 $X$ 上非零的亚纯函数,则 $\deg(\operatorname{div} f) = 0$。

**证明**:视 $f: X \to \mathbb{P}^1$。取 $a=0$ 和 $a=\infty$:
$$n_f(0) = \sum_{p:\,f(p)=0} \operatorname{ord}_p(f), \qquad n_f(\infty) = \sum_{p:\,f(p)=\infty} \operatorname{ord}_p(1/f) = \sum_{p:\,f(p)=\infty} \big(-\operatorname{ord}_p(f)\big)$$
前者恰是 $\operatorname{div}(f)$ 里所有正系数项之和(零点计数),后者恰是所有负系数项绝对值之和(极点计数)。由命题 1.0,$n_f(0) = n_f(\infty) = \deg f$,所以
$$\deg(\operatorname{div} f) = n_f(0) - n_f(\infty) = 0. \qquad\blacksquare$$

(这个证明本质上就是留数定理 $\frac{1}{2\pi i}\oint \frac{f'}{f}dz = 0$ 的几何展开版:$n_f(a)$ 的局部常值性正是辐角原理在紧曲面上的体现。)

### 反例警示:度数为零 $\not\Rightarrow$ 主除子

当 $g \geq 1$ 时,$\deg D = 0$ 只是 $D$ 为主除子的**必要条件**,不是充分条件。真正的判据是:

> **Abel 定理**:$D$ 是主除子 $\iff$ $\deg D = 0$ 且 $D$ 在 **Abel-Jacobi 映射** $X \to J(X) = \mathbb{C}^g/\Lambda$ 下打到零点。

当 $g=0$(即 $X \cong \mathbb{P}^1$)时 $J(X)$ 是一个点,条件自动满足,这就是为什么在 $\mathbb{P}^1$ 上"度数为零"和"主除子"看起来是一回事——但这是低亏格的特殊现象。

---

## 2. 从除子到线丛:$\mathcal{O}(D)$ 与 $L(D)$

与其直接定义 $L(D) = \{f : \operatorname{div}(f) + D \geq 0\} \cup \{0\}$,更本质的方式是从**可逆层(线丛)的截面**出发去理解这个定义为什么"恰好长这样"。

### 构造

给定除子 $D = \sum n_i p_i$,在每个 $p_i$ 附近取局部坐标 $z$,令局部生成元 $f_{p_i} = z^{-n_i}$,满足 $\operatorname{div}(f_{p_i}) = D$(局部)。定义层
$$\mathcal{O}(D)(U) = \{f \text{ 在 } U \text{ 上亚纯} : \operatorname{div}(f) + D \geq 0 \text{ 在 } U \text{ 上}\} \cup \{0\}$$

**为什么是这个不等式**:条件 $\operatorname{div}(f) + D \geq 0$ 在 $p_i$ 处等价于 $f \cdot f_{p_i}$ 在 $p_i$ 处全纯——也就是说 $f$ 关于局部生成元 $f_{p_i}^{-1}$ 的"坐标表示"是正则的。这正是"$\mathcal{O}(D)$ 的局部截面"该有的样子。

不同局部生成元的比值 $g_{ij} = f_{p_i}/f_{p_j}$ 在重叠处处处非零全纯,构成转移函数,验证了 $\mathcal{O}(D)$ 确实是一条**全纯线丛**对应的层。

于是
$$L(D) := H^0(X, \mathcal{O}(D))$$
是这条线丛的整体全纯截面空间,$l(D) := \dim_{\mathbb{C}} L(D)$。

### 推广:任意维复流形上的除子与 $\mathcal{O}(D)$

上面的构造是黎曼面(复维数 $1$)的情形,同样的想法可以逐字推广到任意维紧复流形 $X$($\dim_{\mathbb{C}} X = n$)。

**Weil 除子**:$X$ 上不可约解析超曲面(即余维数为 $1$ 的不可约解析子集)的形式有限整系数和
$$D = \sum_i n_i V_i, \quad n_i \in \mathbb{Z}.$$
在 $n=1$ 时超曲面就是点,回到第 1 节的定义。

**局部方程与 Cartier 数据**:因为 $X$ 光滑,每个不可约超曲面 $V_i$ 局部上都是单个全纯函数的零点集(光滑流形上余维 $1$ 解析集局部由一个函数生成对应的素理想),所以 Weil 除子 $D$ 总能用 **Cartier 数据**描述:存在开覆盖 $\{U_\alpha\}$ 和亚纯函数 $f_\alpha \in \mathcal{M}^*(U_\alpha)$(不恒为零的亚纯函数),使
$$D|_{U_\alpha} = \operatorname{div}(f_\alpha), \qquad g_{\alpha\beta} := \frac{f_\alpha}{f_\beta} \in \mathcal{O}^*(U_\alpha \cap U_\beta)$$
(即 $g_{\alpha\beta}$ 在重叠处处处非零全纯)。这与第 2 节里 $f_{p_i} = z^{-n_i}$ 的角色完全一致,只是局部生成元不再局限于单点邻域。

**转移函数与线丛**:$\{g_{\alpha\beta}\}$ 自动满足上循环条件 $g_{\alpha\beta}g_{\beta\gamma} = g_{\alpha\gamma}$(都等于 $f_\alpha/f_\gamma$),于是定义出一条全纯线丛,记作 $\mathcal{O}_X(D)$。

**作为层的定义**:把 $\mathcal{O}(D)$ 定义为亚纯函数层 $\mathcal{M}_X$ 的子层,逐点用局部方程测试正则性:
$$\mathcal{O}(D)(U) := \{h \in \mathcal{M}(U) : h \equiv 0,\ \text{或对每个 } \alpha,\ h\cdot f_\alpha \in \mathcal{O}(U \cap U_\alpha)\}.$$
等价地,记 $\operatorname{mult}_p(D)$ 为 $D$ 在 $p$ 处的重数(即局部方程 $f_\alpha$ 在 $p$ 处的阶,只依赖 $D$ 不依赖 $\alpha$ 的选取),则
$$\mathcal{O}(D)(U) = \{h \in \mathcal{M}(U) : \operatorname{ord}_p(h) \ge -\operatorname{mult}_p(D)\ \ \forall p \in U\} \cup \{0\}.$$

**良定义性(不依赖覆盖选取)**:若 $hf_\alpha \in \mathcal{O}(U\cap U_\alpha)$,由 $f_\beta = f_\alpha/g_{\alpha\beta}$ 及 $g_{\alpha\beta}$ 处处非零全纯,
$$hf_\beta = \frac{hf_\alpha}{g_{\alpha\beta}}$$
仍然全纯(全纯函数除以处处非零全纯函数还是全纯函数)。所以"$hf_\alpha$ 全纯"这一条件在重叠区域上与 $\alpha$ 的选取无关,粘合自洽,$\mathcal{O}(D)$ 是良定义的层。

**典范亚纯截面**:局部数据 $\{f_\alpha^{-1}\}$ 恰好拼成 $\mathcal{O}(D)$ 的一个整体亚纯截面 $s_D$(在 $U_\alpha$ 的平凡化下 $s_D$ 对应常数函数 $1 \in \mathcal{M}(U_\alpha)$,而"分母"就是 $f_\alpha$),满足
$$\operatorname{div}(s_D) = D.$$
反过来,线丛 $L$ 上任意不恒为零的整体亚纯截面 $s$ 都有除子 $\operatorname{div}(s)$,并且 $\mathcal{O}(\operatorname{div}(s)) \cong L$——这就是 Weil 除子与线丛之间字典的核心。

**整体截面空间**:定义逐字不变,
$$L(D) := H^0(X, \mathcal{O}(D)), \qquad l(D) := \dim_{\mathbb{C}} L(D),$$
即整体亚纯函数 $h$ 使 $\operatorname{div}(h) + D \ge 0$ 处处成立(加上零函数)。高维时这样的 $h$ 可能很少甚至只有 $0$,这正是高维几何比曲线复杂之处——没有像 Riemann-Roch 这样简单的封闭公式(高维版本 Hirzebruch-Riemann-Roch 需要 Todd 类、Chern 特征等工具)。

**两个特例**(后面会用到):
- 若 $D \ge 0$(有效除子),则 $\mathcal{O}_X \subset \mathcal{O}(D)$(常数函数 $1$ 满足 $\operatorname{div}(1)+D = D \ge 0$)。
- 若 $D = V$ 是光滑既约超曲面,则 $\mathcal{O}(-V)$ 恰是 $V$ 的理想层 $\mathcal{I}_V \subset \mathcal{O}_X$(在 $V$ 上取值为零的全纯函数),给出短正合列
$$0 \to \mathcal{O}(-V) \to \mathcal{O}_X \to \mathcal{O}_V \to 0.$$
这是第 5 节正合列 $0\to\mathcal O(D)\to\mathcal O(D+p)\to\mathbb C_p\to 0$ 的高维版本:单点 $p$ 换成超曲面 $V$,skyscraper sheaf 换成 $\mathcal{O}_V$。

---

## 3. Riemann-Roch 定理与典范除子 $K$

### 典范除子

取任意非零亚纯 1-形式 $\omega$(比如局部写作 $\omega = f(z)\,dz$),定义 $K = \operatorname{div}(\omega)$。不同亚纯 1-形式的除子彼此线性等价(相差一个主除子,因为两个亚纯 1-形式的比值是亚纯函数),所以 $K$ 作为**线性等价类**是良定义的,称为**典范除子类**。

- $\deg K = 2g-2$。

  **Riemann–Hurwitz 公式**(标准拓扑结果,证明依赖三角剖分/Euler 示性数的可加性,从略):对紧黎曼面间次数为 $d=\deg f$ 的非常值全纯映射 $f:X\to Y$(记号见第 1 节的 $n_f$、$e_p(f)$),
  $$2g_X - 2 = d(2g_Y - 2) + \sum_{p\in X}\big(e_p(f)-1\big),$$
  求和实际只在有限个**分歧点**($e_p(f)>1$)处非零,$R:=\sum_p(e_p(f)-1)\,p$ 称为**分歧除子**。

  **用它计算 $\deg K$**:任取非常值亚纯函数 $f:X\to\mathbb{P}^1$,$d=\deg f$。取 $\omega := f^*(dz)$,由于任意两个亚纯 $1$-形式的除子相差一个主除子(比值是亚纯函数),$\deg(\operatorname{div}\omega)=\deg K$ 不依赖 $\omega$ 的选取。

  先在 $\mathbb{P}^1$ 上直接验证:$z=\infty$ 处坐标 $u=1/z$,$dz = -u^{-2}du$ 有 $2$ 阶极点,故 $\operatorname{div}(dz) = -2\cdot\infty$,度数为 $-2$。

  再用局部标准型($f$ 在分歧点 $p$ 处形如 $z\mapsto z^{e_p}$)逐点比较:$d(z^{e_p}) = e_p z^{e_p-1}dz$,比起简单拉回 $\operatorname{div}(dz)$ 多出恰好 $e_p-1$ 阶零点,即
  $$\operatorname{div}(\omega) = f^*\big(\operatorname{div}(dz)\big) + R.$$
  由命题 1.0($n_f\equiv d$)可知拉回除子的度数满足 $\deg\big(f^*\operatorname{div}(dz)\big) = d\cdot\deg(\operatorname{div}\,dz) = -2d$,所以
  $$\deg K = \deg(\operatorname{div}\,\omega) = -2d + \deg R = -2d + \sum_p(e_p-1),$$
  这恰是 Riemann–Hurwitz 公式右边(取 $g_Y=0$),等于 $2g_X - 2$。$\blacksquare$

- $l(K) = g$:全纯 1-形式空间的维数就是亏格,这是亏格的一个等价定义。

  **Hodge 理论视角**:$H^0(X,K) = L(K)$ 就是全纯 $1$-形式($(1,0)$-形式)空间 $H^{1,0}(X)$。Hodge 分解给出
  $$H^1(X,\mathbb{C}) = H^{1,0}(X) \oplus H^{0,1}(X), \qquad H^{0,1}(X) = \overline{H^{1,0}(X)}$$
  两个求和项互为复共轭,维数相等;而拓扑上 $\dim_{\mathbb{C}} H^1(X,\mathbb{C}) = 2g$(因为 $H_1(X,\mathbb{Z}) \cong \mathbb{Z}^{2g}$,$g$ 个洞每个贡献一对生成元)。所以 $\dim H^{1,0}(X) = g$,即 $l(K)=g$——这与"拓扑亏格"的定义自动吻合,不依赖 RR 公式。

### Riemann-Roch 定理

$$l(D) - l(K-D) = \deg D + 1 - g$$

### 小推论:$l(K) = g$ 的自洽验证

代入 $D = K$:$l(K) - l(0) = \deg K + 1 - g = (2g-2)+1-g = g-1$。又 $l(0)=1$(常数函数),故 $l(K) = g$。$\blacksquare$(这只是自洽性检验,不是独立证明,因为 $l(K)=g$ 本身常作为 $g$ 的定义之一。)

---

## 4. Ample 线丛:代数判据与解析判据(Kodaira 嵌入定理)

**问题**:单点对应的线丛 $\mathcal{O}(p)$ 是否 ample?

### 代数定义
$L$ ample $\iff$ 存在 $n \gg 0$ 使 $L^{\otimes n}$ very ample(即 $H^0(X,L^{\otimes n})$ 给出到射影空间的嵌入)。

### 解析对应物:曲率正定性

给线丛 $L$ 配一个 Hermitian 度量 $h$,诱导曲率形式
$$\Theta_h = -\partial\bar\partial \log h$$
若能选到 $h$ 使 $i\Theta_h$ 处处正定,称 $L$ 为**正线丛**。

**局部公式与良定义性**:取 $L$ 在 $U$ 上的局部非零全纯截面 $s$(局部平凡化),$h(s,s) =: |s|_h^2 > 0$ 是 $U$ 上的正光滑函数,定义
$$\Theta_h|_U := -\partial\bar\partial \log|s|_h^2,$$
这是 $U$ 上的实 $(1,1)$-形式。换一个局部截面 $s' = g\cdot s$(g 是转移函数,处处非零全纯)时,$|s'|_h^2 = |g|^2|s|_h^2$,而 $\log|g|^2 = \log g + \log\bar g$ 是局部调和函数($\bar\partial\log g = 0$ 因为 $\log g$ 全纯,故 $\partial\bar\partial\log g = 0$,共轭项同理),从而 $\partial\bar\partial\log|g|^2 = 0$。所以 $\Theta_h$ 与局部截面的选取无关,拼成 $X$ 上整体良定义的 $(1,1)$-形式。

在黎曼面上"$i\Theta_h$ 正定"就是说 $\frac{i}{2\pi}\Theta_h$ 是与复结构定向一致的正体积形式(处处不为零的正 $2$-形式)。

### Kodaira 嵌入定理
$$L \text{ ample(代数)} \iff L \text{ 存在正曲率 Hermitian 度量(解析)}$$

### 必要条件:度数为正

由陈类公式 $c_1(L) = \frac{i}{2\pi}\Theta_h$,对 $X$ 积分得 $\int_X c_1(L) = \deg L$。若 $L$ 正,则 $\deg L > 0$。**这只是必要条件**,单点 $\mathcal{O}(p)$ 满足 $\deg = 1 > 0$,但这不足以保证 ample。

### 结合两种方法:$n$ 充分大时的快速论证

考虑 $D = np$,想证明 $n$ 充分大时 $\mathcal{O}(np)$ ample(甚至 very ample)。

**第一步(解析/度数论证,清场)**:当 $n$ 充分大时,
$$\deg(np) = n > 2g-2 = \deg K \implies \deg(K - np) < 0 \implies l(K-np) = 0$$
(度数为负的除子在 $g\geq 1$ 时没有非零全纯截面——负度数线丛不可能有超过一维... 严格说是没有非零截面,因为非零截面的除子度数应 $\geq 0$。)

**第二步(代数,坍缩 RR 公式)**:此时 RR 公式直接给出精确值
$$l(np) = n+1-g$$
不再需要逐点计算。

**第三步**:有了这个线性公式,验证 base-point-free、分离切向量就变成简单的维数比较,可以推出经典结论:$n \geq 2g+1$ 时 $\mathcal{O}(np)$ very ample。

> **相关定义**:
> - **无基点(base-point-free)**:对每个 $q\in X$,存在 $s\in H^0(X,L)$ 使 $s(q)\neq 0$(整体截面在 $q$ 处不同时为零)。此时可取 $H^0(L)$ 的一组基 $s_0,\dots,s_N$,定义映射 $\phi_L: X\to\mathbb{P}^N$,$q\mapsto[s_0(q):\cdots:s_N(q)]$。
> - **very ample**:$\phi_L$ 是一个闭嵌入,等价于同时**分离点**($q\neq q'\Rightarrow$ 存在截面在恰一点处为零)与**分离切向量**($\phi_L$ 在每点处的微分单射,即局部坐标 $z$ 附近存在截面 $s,s'$ 使 $s(q)=0,\ \operatorname{ord}_q(s)=1$ 而 $s'(q)\neq0$)。
>
> 上面第一步已把 $l(K-np)=0$ 归零,第二步给出 $l(np)=n+1-g$ 的精确维数,第三步就是用这些维数去逐点验证"分离点/分离切向量"这两个条件——例如分离两点 $q,q'$ 需要 $l(np-q-q') = l(np)-2$(即存在只消没在 $q,q'$ 处的差别),这类维数不等式可以直接由 RR 公式代入验证。

> **要点**:解析方法(曲率正性 $\Rightarrow$ 度数正 $\Rightarrow$ Serre 对偶消没)负责定性地把 RR 公式里难算的 $l(K-D)$ 项清零;代数方法(RR 公式本身)负责定量地给出精确维数。二者结合远比单独使用任何一种更高效。

---

## 5. $L(D)$ 的阻碍:$H^1$ 上同调群

### 长正合列与连接同态

考虑短正合列(在点 $p$ 处允许多一阶极点):
$$0 \to \mathcal{O}(D) \to \mathcal{O}(D+p) \to \mathbb{C}_p \to 0$$
其中 $\mathbb{C}_p$ 是 $p$ 处的 **skyscraper sheaf**:定义为 $\mathbb{C}_p(U) = \mathbb{C}$(若 $p\in U$)或 $0$(若 $p\notin U$),限制映射在含 $p$ 的开集之间取恒等、否则取零映射;茎 $(\mathbb{C}_p)_q$ 在 $q=p$ 处是 $\mathbb{C}$,在别处是 $0$——它是"层的信息完全集中在一点"的最简单例子。上面的映射 $\mathcal{O}(D+p)\to\mathbb{C}_p$ 具体是取局部 Laurent 展开在 $p$ 处新允许的那一阶系数(即 $f\mapsto (z^{n_p+1}f)(p)$,$n_p$ 是 $D$ 在 $p$ 处的系数),核恰为 $\mathcal{O}(D)$。取长正合列:
$$0 \to H^0(\mathcal{O}(D)) \to H^0(\mathcal{O}(D+p)) \to \mathbb{C} \xrightarrow{\delta} H^1(\mathcal{O}(D)) \to H^1(\mathcal{O}(D+p)) \to 0$$

### 命题 5.1(阻碍即 $H^1$)

$l(D+p) = l(D) + 1$ 当且仅当连接同态 $\delta: \mathbb{C} \to H^1(\mathcal{O}(D))$ 为零映射。

**证明**:由长正合列的正合性,
$$l(D+p) - l(D) = \dim \operatorname{im}(H^0(\mathcal{O}(D+p)) \to \mathbb{C})$$
这个像要么是 $0$,要么是 $\mathbb{C}$(整个 1 维空间),取决于 $\delta$ 是否为零映射(正合性:$\operatorname{im}(H^0(D+p)\to\mathbb{C}) = \ker \delta$)。若 $\delta = 0$,则 $\ker\delta = \mathbb{C}$,即 $l(D+p)-l(D)=1$;若 $\delta \neq 0$(此时 $\delta$ 作为 $\mathbb{C}\to H^1$ 的线性映射必是单射),则 $\ker\delta = 0$,$l(D+p) = l(D)$。$\blacksquare$

直观上:"想在 $p$ 处多允许一个极点"这个愿望,能否被一个真实的亚纯函数实现,取决于这个操作是否落在 $H^1(\mathcal{O}(D)) \to H^1(\mathcal{O}(D+p))$ 的核里——这就是 $H^1$ 作为**阻碍**的含义,是同调代数里"连接同态非零 $\Leftrightarrow$ 障碍存在"这一标准套路在此的体现。

### Čech 上同调实现

上面的 $H^1(X,\mathcal O(D))$ 是导出函子(内射消解)意义下定义的层上同调,比较抽象。在黎曼面上可以把它换成完全具体的 **Čech 上同调**,阻碍类 $\delta(c)$ 也随之变成一个可以直接写下来的"粘不上"的差。

**Leray 定理**(一般拓扑事实,证明略):若开覆盖 $\mathfrak U=\{U_i\}$ 使得所有有限交 $U_{i_0\cdots i_k}$ 上 $\mathcal F$ 的高阶上同调都消没($H^q(U_{i_0\cdots i_k},\mathcal F)=0$,$\forall q>0$),则限制映射诱导自然同构
$$\check H^p(\mathfrak U,\mathcal F)\;\cong\;H^p(X,\mathcal F).$$

**黎曼面上此条件总能满足**:任意黎曼面的开子集本身仍是黎曼面,非紧则是 Stein 流形(第 6 节),从而 $H^{q>0}(\,\cdot\,,\mathcal O)=0$;局部化后 $\mathcal O(D)$ 与 $\mathcal O$ 同构,所以同样消没。于是只要取 $X$ 的坐标圆盘覆盖(或任意由非紧开集组成的覆盖),有限交仍是开黎曼面,消没条件自动成立,从而
$$H^1(X,\mathcal O(D)) \cong \check H^1(\mathfrak U,\mathcal O(D)) = Z^1(\mathfrak U,\mathcal O(D))\big/B^1(\mathfrak U,\mathcal O(D)),$$
其中 $Z^1$ 是满足上循环条件 $f_{ij}+f_{jk}=f_{ik}$ 的族 $\{f_{ij}\in\mathcal O(D)(U_i\cap U_j)\}$,$B^1$ 是形如 $f_{ij}=h_i-h_j$($h_i\in\mathcal O(D)(U_i)$)的上边缘。

**把 $\delta(c)$ 写成具体的 Čech 类**:取最简单的两元覆盖 $\mathfrak U=\{U_0,U_1\}$,$U_0$ 是 $p$ 处一个小坐标圆盘(坐标 $z$),$U_1=X\setminus\{p\}$(两者都是开黎曼面,消没条件成立)。设 $D$ 在 $p$ 处的系数为 $n_p$,对给定 $c\in\mathbb C$,令
$$g:=\frac{c}{z^{\,n_p+1}}\ \in\ \mathcal O(D+p)(U_0),\qquad g\notin\mathcal O(D)(U_0)\ (\text{若 }c\ne0).$$
$\{g$ 在 $U_0$ 上、$0$ 在 $U_1$ 上$\}$ 是 $\mathcal O(D+p)$ 的一个 Čech $0$-上链;它在 $U_0\cap U_1$(即已经离开 $p$ 的区域)上的差
$$f_{01} := g|_{U_0\cap U_1} - 0 \ \in\ \mathcal O(D)(U_0\cap U_1)$$
自动是一个 $1$-上循环(只有一个重叠区域,循环条件平凡满足),它的类 $[f_{01}]\in\check H^1(\mathfrak U,\mathcal O(D))\cong H^1(X,\mathcal O(D))$ 就是长正合列里连接同态给出的 $\delta(c)$。

**$\delta(c)=0$ 的含义完全显式化**:$[f_{01}]$ 是上边缘 $\iff$ 存在 $h_0\in\mathcal O(D)(U_0)$、$h_1\in\mathcal O(D)(U_1)$ 使 $f_{01}=h_0-h_1$ 在 $U_0\cap U_1$ 上成立,即 $g-h_0=-h_1$。这时两侧在重叠处相等,可以粘合成一个整体函数 $F\in\mathcal O(D+p)(X)$(在 $U_0$ 上取 $g-h_0$,在 $U_1$ 上取 $-h_1$),并且因为 $h_0\in\mathcal O(D)(U_0)$ 在 $z^{-(n_p+1)}$ 这一阶系数为零,$F$ 在 $p$ 处的主部恰好保留了 $g$ 贡献的 $c/z^{n_p+1}$ 项。也就是说:**$\delta(c)=0$ 精确地等价于"存在整体亚纯函数,在 $p$ 处实现主部 $c/z^{n_p+1}$"**——这正是第 6 节 Mittag-Leffler 问题的原始表述,现在通过 Čech 语言,"上同调类非零"与"局部数据粘不成整体"这两句话变成了同一件事的两种写法。

(对照:第 3 节用 Dolbeault/Hodge 理论把 $H^1(X,\mathcal O)$ 等同于 $\overline{H^{1,0}(X)}$,是"光滑范畴"里的另一种具体实现;这里的 Čech 版本则是"组合/覆盖"意义下的具体实现。三者——导出函子上同调、Čech 上同调、Dolbeault 上同调——在紧黎曼面上给出同一个抽象群,只是计算方式不同。)

---

## 6. Mittag-Leffler 问题:开曲面 vs 紧曲面

**经典 Mittag-Leffler 问题**:给定一组点 $p_i$ 及各点处指定的"主部"(极点的奇异部分),是否存在整体亚纯函数,在每个 $p_i$ 处恰好实现给定主部?

- **开(非紧)黎曼面上**:问题**总是可解**。本质原因是非紧黎曼面是 **Stein 流形**,$H^1(X,\mathcal{O}) = 0$(Behnke-Stein 定理的推论)——按第 5 节的语言,阻碍群本身就是零,自然没有障碍。

  (**Stein 流形**粗略地说是"整体全纯函数足够丰富"的复流形,等价刻画包括:全纯凸;能被全纯函数分离任意两点(以及分离切向量);可全纯嵌入某个 $\mathbb{C}^N$。$\mathbb{C}^n$ 本身、非紧黎曼面、仿射代数簇都是 Stein 流形的例子;紧复流形除了有限集外都不是 Stein 流形——这也是为什么"阻碍消没"这件事在开、闭黎曼面上的表现截然相反。)

- **紧黎曼面上**:问题**不总是可解**。阻碍正是 $H^1(X,\mathcal{O})$,而由 Serre 对偶
$$H^1(X,\mathcal{O}) \cong H^0(X, K)^* $$
其维数恰为 $g$(亏格)。这把"经典 Mittag-Leffler 问题在紧曲面上失效"这一分析现象,和"$l(K)=g$"这一代数不变量直接联系了起来。

> 这一节把第 5 节的一般阻碍理论应用到 $D=0$(即 $\mathcal{O}(D)=\mathcal{O}_X$)这一最基础情形,同时把经典函数论问题重新翻译成了层上同调语言。

---


