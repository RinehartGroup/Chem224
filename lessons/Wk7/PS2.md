# Chem 224 - Problem Set 2

Due Friday Dec. 1st, 2023

## 1. Octahedral Crystal Field Splitting for $Ti^{3+}$

Titanium(III) salts form the complex $Ti(H_2O)_6^{3+}$, when dissolved in water. The complex has an octahedral geometry that approximates $O_h$ symmetry. Shown below is the electronic absorption spectrum of $Ti(H_2O)_6^{3+}$ in water. The spectrum is dominated by a single band.

![Ti3abs](/assets/Ti3abs.png)

#### Qualitative electronic structure of $Ti(H_2O)_6^{3+}$

a. Using the terminology of ligand field theory, (weak field / strong field / $\sigma$-donor / $\pi$-donor / $\pi$-acceptor), describe the valence orbitals of the $Ti^{3+}$ ion before and after complexation with water. By "before" include both the free ion form and a hypothetical octahedral complex with the original halide ligands.

b. Draw a simple crystal field splitting diagram for the $\text{Ti}^{3+}$ ion in an octahedral field. Label the orbitals with their symmetry labels. You do not need to draw or label any ligand based orbitals. Indicate what you expect the major contribution to the interactions to be by adding a "*" to the $e_g$ and $t_{2g}$ orbitals when appropriate.

#### Quantifying the Crystal Field Splitting

c. The absorption spectrum of $Ti(H_2O)_6^{3+}$ in water is shown above. The spectrum is dominated by a single band. What is the wavelength of this band in nm? What color would you expect the complex to be?

#### Electronic Structure Analysis

d. To describe the nature of the absorption spectrum from a state picture we can sketch a version of a Tanabe-Sugano Diagram. Make a T-S Diagram where you plot Energy vs. $\Delta_O$ and label the states with their symmetry labels. Draw a line on the diagram to indicate the transition you see in the absorption spectrum. Draw electron filling diagrams for the spherical, ground state, and excited state configurations.

e. The spectrum is in units of $\epsilon$ (M$^{-1}$ cm$^{-1}$). Is this a weakly or strongly absorbing transition? Justify your answer using selection rules.

## 2. Term Symbols in the Strong Field Limit for $d^2$ Configurations in $O_h$

When we have multiple electrons that are strongly coupled to the crystal field as opposed to being strongly coupled to each other, it can be convenient to form our symmetry-adapted states in the basis of the crystal field eigenstates. For the $d^2$ case of $O_h$ symmetry, we have three possible ways to couple two spins to the crystal field. The three possible ways are $(t_2g)^2$, $(t_2g)^1(e_g)^1$, and $(e_g)^2$. 
#### The $(t_2g)^1(e_g)^1$ Case: Finding the Term Symbols

If we confine the two electrons to separate orbitals, we can use the same procedure we used for the $d^1$ case to find the term symbols for the $(t_2g)^1(e_g)^1$ case. We use the one electron term symbols for the $t_{2g}$ and $e_g$ orbitals and then couple the two electrons to get the term symbols for the $(t_{2g})^1(e_g)^1$ case:

$$
\Gamma_{O_h}(t_{2g} \otimes e_g) = \Gamma_{O_h}(t_{2g}) \otimes \Gamma_{O_h}(e_g) = T_{2g} \otimes E_g
$$

The $O_h$ character table is shown below.

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
|$\Gamma_{O_h}(t_{2g} \otimes e_g)$ |  |  |  |  |  |  |  |  |  |  |
|$\Gamma_{O_h}(e_g \otimes e_g)$ |  |  |  |  |  |  |  |  |  |  |
|$\Gamma_{O_h}(t_{2g} \otimes t_{2g})$ |  |  |  |  |  |  |  |  |  |  |

a. Using the $O_h$ group character table, find a reducible representation describing how the two electrons $\Gamma_{O_h}(t_{2g} \otimes e_g)$ transform under $O_h$. Does the dimensionality of this representation make sense for the physical situation you are modeling? (Hint: For now ignore the spin of the electrons and just consider the number of electrons and the number of orbitals.)

b. Reduce this representation to give the term symbols that result from the $\Gamma_{O_h}(t_{2g} \otimes e_g)$ case. (Hint: You should get two triply degenerate terms).

c. Now consider the possible spin states for two electrons in these configurations. What are they and what are their multiplicities?

d. The product of the spin and orbital degeneracies gives the total degeneracy of the state. What are the total degeneracies of the states with $\Gamma_{O_h}(t_{2g} \otimes e_g)$ symmetry?

e. Combine each possible spin with each orbital term from part b to give the full set of symbols for the $(t_2g)^1(e_g)^1$ case (make sure your degeneracies match part d!). Hint: You should get a total degeneracy of 24.

#### The $(e_g)^2$ Case: Finding the Orbital Terms

f. Follow the previous procedure to find the combined orbital symmetry terms for placing two electrons in the $e_g$ symmetry orbitals. Reduce this representation to give the orbital term symbols for the $(e_g)^2$ case.

g. Once again, we can have two possible spin states for the two electrons. What are they and what are their multiplicities?

#### Descent of Symmetry in the Strong Field Limit for $(e_g)^2$ Configurations in $O_h$

Descent of Symmetry Table for $O_h \rightarrow C_{2h}$

| $O_h$ | $O$ | $T_d$ | $D_{4h}$ | $D_{2d}$ | $C_{4v}$ | $C_{2h}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $A_{1g}$ | $A_1$ | $A_1$ | $A_{1g}$ | $A_1$ | $A_1$ | $A_g$ |
| $A_{2g}$ | $A_2$ | $A_2$ | $B_{1g}$ | $B_1$ | $B_1$ | $B_g$ |
| $E_g$ | $E$ | $E$ | $A_{1g}+B_{1g}$ | $A_1+B_1$ | $A_1+B_1$ | $A_g+B_g$ |
| $T_{1g}$ | $T_1$ | $T_1$ | $A_{2g}+E_g$ | $A_2+E$ | $A_2+E$ | $A_g+2B_g$ |
| $T_{2g}$ | $T_2$ | $T_2$ | $B_{2g}+E_g$ | $B_2+E$ | $B_2+E$ | $2A_g+B_g$ |

h. Use the Descent of Symmetry table above to remove the orbital degeneracies from the $(e_g)^2$ case. What point group do you need to descend to to ensure you have removed all of the degeneracies?

i. You should now have split your $e_g$ set into two, non-degenerate (though not necessarily unique) orbital symmetries. Show all ways that two electrons can be distributed among these two orbitals. What are the symmetries for each case? Reduce these representations to give the irreducible representations for each case in the 2 electron basis.

j. You now have the symmetry-lowered term symbols with the proper spin states. Raise the symmetry back up to $O_h$ and find the final term symbols for the $(e_g)^2$ case.
    - Hint: There should only be one way to raise the symmetry back up to $O_h$ without violating the Pauli principle or misassigning the spin states.

#### Descent of Symmetry in the Strong Field Limit for $(t_{2g})^2$ Configurations in $O_h$

k. Find all the term symbols that describe the orbital states possible for configurations of $(t_{2g})^2$ in $O_h$.

- Hint: There should be a total obital degeneracy of 9 for the $(t_{2g})^2$ case in $O_h$.

l. Once again, the orbital degeneracy is preventing us from determining if there are Pauli violations occuring. Find a symmetry that will remove all degeneracies from the $t_2g$ set of orbitals. What oint group do you need to descend to to ensure you have removed all of the degeneracies?

m. What are the key symmetry elements that you needed to remove to ensure there would be no degeneracies remaining?
  - Hint: The $t_{2g}$ orbitals are $d_{xy}$, $d_{xz}$, and $d_{yz}$

n. You should now have split your $t_2g$ set into three, non-degenerate (though not necessarily unique) orbital symmetries. Show all ways that two electrons can be distributed among these three orbitals. Reduce representations within the group symmetry (using the appropriate character table) to determine the term symbols for each case.
- Hint: There are six orbital combinations and three of these will have multiple spin combinations possible.

o. You now have the symmetry-lowered term symbols with the proper spin states. Raise the symmetry back up to $O_h$ and find the final term symbols for the $(t_{2g})^2$ case.
    - Hint: There should only be one way to raise the symmetry back up to $O_h$ without violating the Pauli principle or misassigning the spin states.

p. Fill out the diagram below with the term symbols you found for the $(t_{2g})^2$, $(e_g)^2$, and $(t_{2g})^1(e_g)^1$ cases. Label the states with their symmetry labels and order them (roughly) according to their energies using first the single electron excitation energies (multiples of $\Delta_O$) and then try to follow Hund's rules if any are applicable. Connect the weak-field side of the diagram to the strong field side of the diagram so that each state is represented as a continuous function of the crystal field strength.

![Correlation_Diagram](/assets/Correlation_Diagram_3k7d482d8.png)

## 3. Using the Tanabe-Sugano Diagram to Analyze Absorption Spectra

Shown below is the Electronic Absorption Spectrum of an octahedral $Co^{2+}$ complex. The spectrum shows three bands, each marked with a "*" in the figure. The spectrum is in units of unnormalized absorbance vs. cm$^{-1}$. Each peak arises from the ground state to a SPIN-ALLOWED excited state.

![Co2Abs](/assets/Co2Abs.png)

#### Qualitative Electronic Structure of $Co^{2+}$

a. Show the crystal field splitting orbital picture for weak and strong field cases of $O_h$ symmetry. What are S and L for each case? The free ion case is shown below (S = 3/2, L = 3).

![Co2_d7](/assets/Co2_d7.png)

b. Do weak and strong-field cases lead to different ground states? Use the Tanabe-Sugano diagram below to justify your answer and identify the ground state(s). (Sorry the x-axis axis is partially cut off, it should read $D_q/B$.)

![Co2_TS](/assets/Co2_TS.png)

c. Refer back to the spectrum at the beginning of this question. What are possible assignments for the three bands? (Remember that they are all spin-allowed transitions.)

d. Use the energy spacing of the bands to decide what the likely ground state is and assign the bands to the appropriate transitions.

e. The T-S diagram is in units of $\frac{E}{B}$ vs. $\frac{D_q}{B}$, meaning we cannot directly compare the T-S diagram to the spectrum. However, we can use the T-S diagram to find the ratio of the energy spacings of the bands. Find the ratios of the energies of the bands in the spectrum and use this to locate the value of $\frac{D_q}{B}$ on the T-S diagram. What is the (approximate) value of $\frac{D_q}{B}$?

f. Use the value of $\frac{D_q}{B}$ you found in part e to find the values of $\frac{E}{B}$ for each transition of the complex. Use these to solve for the value of $B$ in cm$^{-1}$.

g. The value of $B$ you found in part f is the Racah parameter for the complex. Every metal in every oxidation state will have a different value of $B$. The value of $B$ for $Co^{2+}$ is 880 cm$^{-1}$. Differences between the value you found and the general value are in some part attributable to the affect of ligand stabilization of the metal orbitals. This is called the nephelauxetic effect and is quantified by the nephelauxetic ratio, $\eta = \frac{B_{free}}{B_{complex}}$. What is the nephelauxetic ratio for the complex you are analyzing?

h. Use the value of $B$ you found in part f to find the value of $D_q$ in cm$^{-1}$.

i. What is a plausible explanation for why the second band is so much weaker that the first and third bands? (Hint: Remember what we said about the slope of a state in the T-S diagram in class and/or think about where the state ends up in the strong field limit.)