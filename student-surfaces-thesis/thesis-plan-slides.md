# From black boxes to a thesis

---

## Where he stands

**Claim.** He already has the maturity Hartshorne IV–V assumes — what's missing is mileage on real objects, not more theorems. {result}

- Background already in hand
  - Atiyah–Macdonald, do Carmo *Riemannian Geometry*, Bott–Tu, Huybrechts ch.1, affine schemes
    - do Carmo gives curvature intuition before he ever computes a self-intersection number; Bott–Tu gives Čech-de Rham and spectral sequences before he needs them for cohomology
- What's actually missing
  - Not theory — the experience of deciding what's true by playing with a concrete example
    - This is what "research obstruction" means in practice, and it's exactly what living inside Chapters IV–V trains

---

## The bet: geometry before machinery

**Claim.** Chapters IV and V are where Hartshorne's abstractions finally cash out into curves, surfaces, and numbers you can compute. {result}

- Chapter IV: curves — genus, Riemann–Roch, elliptic curves, embeddings
- Chapter V: surfaces — intersection theory, blow-ups, ruled surfaces, cubic surfaces, classification
  - Read II–III straight through first and a year gets spent proving lemmas before a single interesting surface appears
    - Read IV–V first, with II–III as reference, and week one already has a real object on the table

---

## The method: black-box-first

**Claim.** Name the gap, keep moving, come back armed — this is not a shortcut, it's how Hartshorne itself is built. {result}

- Hartshorne V.1 states the intersection-number axioms and uses them immediately
  - Self-intersection of a line in $\mathbb{P}^2$ is $1$
    - The axioms are trusted before a single Čech complex is computed — the construction comes *later*, in V.1's own cohomological proof (∗)
- Every black box gets one line in a shared log
  - statement used → where it was needed → which route will unlock it later

---

## Two routes, one comparison

**Claim.** The thesis is not "read Hartshorne" — it's the comparison of two independent proofs of the same black box. {result}

- Student leads the algebraic route
  - Čech cohomology, Serre duality via residues, Riemann–Roch, intersection numbers via deformation to the normal cone
    - Already strong in homological algebra and spectral sequences — closer to review than new material for him
- Yan leads the analytic/Hodge route
  - Dolbeault cohomology, harmonic representatives, Chern–Weil curvature
    - Picks up exactly where his Huybrechts ch.1 stopped
- It runs both directions — the student teaches Yan homological algebra along the way {result}

---

## Tomorrow — first black box (M0)

**Claim.** One board, one axiom system, one number — that's the whole first session. {result}

- Put V.1's five intersection-number axioms on the board
  - Verify them on one example: a line $L \subset \mathbb{P}^2$ satisfies $L \cdot L = 1$
    - Nothing here needs cohomology yet — axioms alone already pin down the geography
- State Riemann–Roch for curves without proof
  - Connect it immediately to the degree–genus formula for a plane curve of degree $d$
    $$g = \frac{(d-1)(d-2)}{2}$$
- Assign for next time
  - Read V.1 and IV.1 (statements only); start the black-box log; bring 2–3 surfaces that look interesting

---

## Chapter IV fast pass — curves

**Claim.** Curves are the training ground: every black box here has a clean picture and a clean number attached. {result}

- Riemann–Roch used immediately, not proved
  - Compute $h^0$ for line bundles on $\mathbb{P}^1$ and on an elliptic curve
    - The gap between the naive count and the Riemann–Roch answer *is* the first real black box (Serre duality's correction term)
- Degree–genus, Hurwitz, elliptic curves as worked examples
  - Elliptic curves are the natural bridge onward — moduli, arithmetic geometry, the material a master's-level course builds on
    - (∗) if he wants a stretch goal later, this is where a second, more ambitious semester would start

---

## Chapter V fast pass — surfaces

**Claim.** This is the actual center of gravity — the black boxes that make surfaces feel real, and the objects worth a thesis. {result}

- Blow-ups and exceptional divisors
  - Already have the algebraic machine on file: `deformation-to-normal-cone`, Rees algebra
    - The picture do Carmo never gave him — what curvature does when you blow up a point
- Cubic surfaces and the 27 lines
  - A single classical object carries intersection theory, the canonical class, and a Galois action on the 27 lines by the Weyl group $W(E_6)$
    - (∗) a 19th-century enumerative fact that encodes one of the deepest exceptional Lie groups — strong enough to anchor a real thesis by itself
- Ruled and del Pezzo surfaces, Castelnuovo's criterion
  - Points straight at Enriques–Kodaira classification — the natural horizon just past the thesis, squarely master's-level material

---

## Closing the loop (M4–M6)

**Claim.** Once IV–V's geography is built, the black-box log becomes the thesis's table of contents. {result}

- M4 — compile the ledger
  - Expect: Serre duality, finiteness of cohomology, Riemann–Roch's own proof, adjunction, existence of the intersection pairing
- M5 — unlock 2–3 of them from both sides
  - Algebraic route (student) and analytic route (Yan), checked against each other
- M6 — write the comparison, anchored on one surface
  - Not an exposition of Hartshorne, but a documented, cross-checked understanding of why the black boxes are true

---

## Three live options for the anchor

**Claim.** Any of these is a legitimate undergraduate thesis; the choice is his, made together after M3. {result}

- Cubic surfaces & the 27 lines
  - Self-contained, classical; the $W(E_6)$ connection gives it real depth without more machinery
- Hirzebruch / ruled surfaces
  - $\mathbb{P}^1$-bundles — connects directly to his do Carmo curvature background and to existing bricks (`relative-canonical-bundle`, `direct-image`)
- Blow-ups & minimal models
  - Broadest and most "research obstruction" flavored; longest runway, best with more than one semester

---

## Why this is promising

**Claim.** Done well, this thesis sits right at the entrance to first-year master's algebraic geometry — that's the point. {result}

- It produces a real deliverable, not just reading notes
  - A cross-checked, two-proof understanding of the load-bearing theorems behind one concrete surface
- It uses what he already has instead of asking for more of it
  - do Carmo and Bott–Tu stop being background he once read and become the analytic lens he applies himself
- It leaves an obvious next step
  - Classification of surfaces, moduli of curves, or K3 surfaces — whichever direction his master's takes, this thesis is the on-ramp
