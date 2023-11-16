# In Class Questions

## 1. Octahedral Crystal Field Splitting for $Ti^{3+}$

Titanium(III) salts form the complex $Ti(H_2O)_6^{3+}$, when dissolved in water. The complex has an octahedral geometry that approximates $O_h$ symmetry. Shown below is the electronic absorption spectrum of $Ti(H_2O)_6^{3+}$ in water. The spectrum is dominated by a single band.

![Ti3abs](/assets/Ti3abs.png)

#### Qualitative electronic structure of $Ti(H_2O)_6^{3+}$

a. Using the terminology of ligand field theory, (weak field / strong field / $\sigma$-donor / $\pi$-donor / $\pi$-acceptor), describe the valence orbitals of the $Ti^{3+}$ ion before and after complexation with water. By "before" include both the free ion form and a hypothetical octahedral complex with the original halide ligands.

b. Draw a simple crystal field splitting diagram for the $Ti^{3+}$ ion in an octahedral field. Label the orbitals with their symmetry labels. You do not need to draw or label any ligand based orbitals. Indicate what you expect the major contribution to the bonding to be by your symmetry labels of the $e_g$ and $t_{2g}$ orbitals.

#### Quantifying the Crystal Field Splitting

c. The absorption spectrum of $Ti(H_2O)_6^{3+}$ in water is shown above. The spectrum is dominated by a single band. What is the wavelength of this band in nm? What color would you expect the complex to be?

#### Electronic Structure Analysis

d. To describe the nature of the absorption spectrum from a state picture we can sketch a version of a Tanabe-Sugano Diagram. Make a T-S Diagram where you plot $Energy vs. \Delta_o$ and label the states with their symmetry labels. Draw a line on the diagram to indicate the transition you see in the absorption spectrum. Draw electron filling diagrams for the spherical, ground state, and excited state configurations.

e. The spectrum is in units of $\epsilon$ (M$^{-1}$ cm$^{-1}$). Is this a weakly or strongly absorbing transition? Justify your answer using selection rules.

## 2. Term Symbols in the Strong Field Limit for $d^2$ Configurations in $O_h$

When we have multiple electrons that are strongly coupled to the crystal field as opposed to each other, it can be convenient to form our symmetry-adapted states in the basis of the crystal field eigenstates. For the $d^2$ case of $O_h$ symmetry, we have three possible ways to couple two spins to the crystal field. The three possible states are $(t_2g)^2$, $(t_2g)^1(e_g)^1$, and $(e_g)^2$. The term symbols for these states are given in the table below.

#### The $(t_2g)^1(e_g)^1$ Case: Finding the Term Symbols

If we confine the two electrons to separate orbitals, we can use the same procedure we used for the $d^1$ case to find the term symbols for the $(t_2g)^1(e_g)^1$ case. We use the one electron term symbols for the $t_{2g}$ and $e_g$ orbitals and then couple the two electrons to get the term symbols for the $(t_2g)^1(e_g)^1$ case. The $O_h$ character table is shown below.

| $O_h$ | $E$ | $8C_3$ | $6C_2$ | $6C_4$ | $3C_2=(C_4)^2$ | $i$ | $6S_4$ |$8S_6$ | $3\sigma_h$ | $6\sigma_d$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $A_{1g}$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| $A_{2g}$ | 1 | 1 | -1 | -1 | 1 | 1 | -1 | 1 | 1 | -1 |
| $E_g$ | 2 | -1 | 0 | 0 | 2 | 2 | 0 | -1 | 2 | 0 |
| $T_{1g}$ | 3 | 0 | -1 | 1 | -1 | 3 | 1 | 0 | -1 | -1 |
| $T_{2g}$ | 3 | 0 | 1 | -1 | -1 | 3 | -1 | 0 | -1 | 1 |
| $A_{1u}$ | 1 | 1 | 1 | 1 | 1 | -1 | -1 | -1 | -1 | -1 |
| $A_{2u}$ | 1 | 1 | -1 | -1 | 1 | -1 | 1 | -1 | -1 | 1 |
| $E_u$ | 2 | -1 | 0 | 0 | 2 | -2 | 0 | 1 | -2 | 0 |
| $T_{1u}$ | 3 | 0 | -1 | 1 | -1 | -3 | -1 | 0 | 1 | 1 |
| $T_{2u}$ | 3 | 0 | 1 | -1 | -1 | -3 | 1 | 0 | 1 | -1 |
|$\Gamma = (t_{2g})^1 \otimes (e_g)^1$ |  |  |  |  |  |  |  |  |  |  |
|$\Gamma = (e_g)^1 \otimes (e_g)^1$ |  |  |  |  |  |  |  |  |  |  |
|$\Gamma = (t_2g)^1 \otimes (t_{2g})^1$ |  |  |  |  |  |  |  |  |  |  |

a. Using the $O_h$ group character table, find a reducible representation describing how the two electrons ($\Gamma = (t_{2g})^1 \otimes (e_g)^1$) transform under $O_h$. Does the dimensionality of this representation make sense for the physical situation you are modeling? (Hint: For now ignore the spin of the electrons and just consider the number of electrons and the number of orbitals.)

Total Orbital Symmetry:
$$
\begin{align*}
\Gamma_{\text{orb}} &= (t_2g)^1 \otimes (e_g)^1 \\
&= (2)(3) \quad (-1)(0) \quad (0)(1) \quad (0)(-1) \quad (2)(-1) \\
&\quad (2)(3) \quad (0)(-1) \quad (-1)(0) \quad (2)(-1) \quad (0)(1) \\
&= 6 \quad 0 \quad 0 \quad 0 \quad -2 \quad 6 \quad 0 \quad 0 \quad -2 \quad 0 \\
&= T_{1g} \oplus T_{2g}
\end{align*}
$$

b. Reduce this representation to give the term symbols for the $(t_2g)^1(e_g)^1$ case.

c. Now consider the possible spin states for the two electrons. What are they and what are their multiplicities?

d. The product of the spin and orbital degeneracies gives the total degeneracy of the state. What are the total degeneracies of the states in the $(t_2g)^1(e_g)^1$ case?

e. Combine the each possible spin with each orbital term from part b to give the full set of symbols for the $(t_2g)^1(e_g)^1$ case (make sure your degeneracies are match part d!)

#### The $(e_g)^2$ Case: Finding the Orbital Terms

f. Follow the previous procedure to find the orbital terms for the $(e_g)^2$ case. Find the reducible representation for the $(e_g)^2$ case. Reduce this representation to give the term symbols for the $(e_g)^2$ case.

Total Orbital Symmetry:
$$
\begin{align*}
\Gamma_{\text{orb}} &= (e_g)^1 \otimes (e_g)^1 \\
&= (2)(2) \quad (-1)(-1) \quad (0)(0) \quad (0)(0) \quad (2)(2) \quad (2)(2) \\
&\quad (0)(0) \quad (-1)(-1) \quad (2)(2) \quad (0)(0) \\
&= 4 \quad 1 \quad 0 \quad 0 \quad 4 \quad 4 \quad 0 \quad 1 \quad 4 \quad 0 \\
&= A_{1g} \oplus A_{2g} \oplus E_g
\end{align*}
$$

g. Once again, we can have two possible spin states for the two electrons. Use the spin and orbital degeneracies you get from the same method you used previously to argue that there will be a Pauli violation in the $(e_g)^2$ case if every spin and orbital combination is used.

#### Descent of Symmetry in the Strong Field Limit for $(e_g)^2$ Configurations in $O_h$

Descent of Symmetry Table for $O_h \rightarrow C_{2h}$

| $O_h$ | $O$ | $T_d$ | $D_{4h}$ | $D_{2d}$ | $C_{4v}$ | $C_{2h}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $A_{1g}$ | $A_1$ | $A_1$ | $A_{1g}$ | $A_1$ | $A_1$ | $A_g$ |
| $A_{2g}$ | $A_2$ | $A_2$ | $B_{1g}$ | $B_1$ | $B_1$ | $B_g$ |
| $E_g$ | $E$ | $E$ | $A_{1g}+B_{1g}$ | $A_1+B_1$ | $A_1+B_1$ | $A_g+B_g$ |
| $T_{1g}$ | $T_1$ | $T_1$ | $A_{2g}+E_g$ | $A_2+E$ | $A_2+E$ | $A_g+2B_g$ |
| $T_{2g}$ | $T_2$ | $T_2$ | $B_{2g}+E_g$ | $B_2+E$ | $B_2+E$ | $2A_g+B_g$ |

h. Use the table above to remove the orbital degeneracies from the $(e_g)^2$ case. What are the term symbols for the $(e_g)^2$ case in the highest symmetry group with no orbital degeneracies?

Answer:

- The orbital splitting in $O_h$ is $e_g$ but if we lower the symmetry to $D_{4h}$ we can split the $e_g$ orbitals into $a_{1g}$ and $b_{1g}$ orbitals. We could look at a character table to see that this corresponds to the splitting of the $d_z^2$ and $d_{x^2-y^2}$ orbitals which will have $a_{1g}$ and $b_{1g}$ symmetry respectively.

With the symmetry lowered, now let's go back to adding in our two electrons. There are now different ways to do this that we can tell apart due to the lower symmetry. The possibilities are now:

- $(a_{1g})^2$
- $(b_{1g})^2$
- $(a_{1g})^1(b_{1g})^1$

Now we are free to use the same procedure as before to find the term symbols for each of these cases since there can be no ambiguity here:

- $(a_{1g})^2$
  - $\Gamma_{\text{orb}} = (a_{1g})^2$ = $A_{1g}$
  - We cannot put two electrons in the same orbital ($d_z^2$) with the same spin so the only possibility is $S = 0$
  - Therefore, this is a singlet state with term symbol $^1A_{1g}$
- $(b_{1g})^2$
  - $\Gamma_{\text{orb}} = (b_{1g})^2$ = $B_{1g}$
  - We cannot put two electrons in the same orbital ($d_{x^2-y^2}$) with the same spin so the only possibility is $S = 0$
  - Therefore, this is a singlet state with term symbol $^1B_{1g}$
- $(a_{1g})^1(b_{1g})^1$
  - $\Gamma_{\text{orb}} = (a_{1g})^1(b_{1g})^1$ = $B_{1g}$
  - We can put two electrons in these orbitals ($d_z^2$, $d_{x^2-y^2}$) with either the same spin or opposite spin so we have $S = 1,0$ as possibilities.
  - Therefore, we have both a singlet and triplet state with term symbols $^1B_{1g}$ and $^3B_{1g}$

The next step will be to raise the symmetry back up to $O_h$

We have the following states in $D_{4h}$:

- $^1A_{1g}$
- $^1A_{1g}$
- $^1B_{1g}$
- $^3B_{1g}$

We know these states must correlate to the following states in $O_h$:

- $A_{1g}$
- $A_{2g}$
- $E_g$

| $O_h$ | $O$ | $T_d$ | $D_{4h}$ |
| :---: | :---: | :---: | :---: |
| $A_{1g}$ | $A_1$ | $A_1$ | $A_{1g}$ |
| $A_{2g}$ | $A_2$ | $A_2$ | $B_{1g}$ |
| $E_g$ | $E$ | $E$ | $A_{1g}+B_{1g}$ |

We can solve this problem by first recognizing that we only have one triplet state so our $E_g$ state must decompose into the $^1A_{1g}$ and $^1B_{1g}$ states. With these eliminated, we have only one possibility left for the $^1A_{1g}$ state which is the $A_{1g}$ state. This leaves the $^1B_{1g}$ state to be the $B_{1g}$ state. Our final term symbols when we re-ascend to $O_h$ are:

$$
\begin{align*}
D_{4h} &\rightarrow O_h \\
\hline
^1A_{1g} &\rightarrow ^1A_{1g} \\
^1B_{1g} + ^1A_{1g} &\rightarrow ^1E_g \\
^3B_{1g} &\rightarrow ^3A_{2g} \\
\end{align*}
$$

#### Descent of Symmetry in the Strong Field Limit for $(t_{2g})^2$ Configurations in $O_h$

i. Find all the term symbols that describe the orbital states possible for configurations of $(t_{2g})^2$ in $O_h$.

- Hint: There should be a total obital degeneracy of 9 for the $(t_{2g})^2$ case in $O_h$.

j. Once again, the orbital degeneracy is preventing us from determining if there are Pauli violations occuring. Find a symmetry that will remove all degeneracies from the $t_2g$ set of orbitals.

k. What are the key symmetry elements that you needed to remove to ensure there would be no degeneracies remaining?

- Hint: The $t_{2g}$ orbitals are $d_{xy}$, $d_{xz}$, and $d_{yz}$

l. You should now have split your $t_2g$ set into three, non-degenerate (though not necessarily unique) orbital symmetries. Show all ways that two electrons can be distributed among these three orbitals. What are the term symbols for each cases?

- Hint: There are six orbital combinations and three of these will have multiple spin combinations possible.)

m. You now have the symmetry-lowered term symbols with the proper spin states. Raise the symmetry back up to $O_h$ and find the final term symbols for the $(t_{2g})^2$ case.
    - Hint: There should only be one way to raise the symmetry back up to $O_h$ without violating the Pauli principle or misassigning the spin states.

n. Fill out the digram below with the term symbols you found for the $(t_{2g})^2$, $(e_g)^2$, and $(t_{2g})^1(e_g)^1$ cases. Label the states with their symmetry labels and order them according to their energies as well as you can according to the excitation energies and Hund's rules. Connect the weak-field side of the diagram to the strong field side of the diagram so that each state is represented as a continuous function of the crystal field strength.

![Correlation_Diagram](/assets/Correlation_Diagram_3k7d482d8.png)
