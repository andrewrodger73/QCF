# 🌌 Quantum Constraint Framework (QCF) Simulation v4

**Resolving Black Hole Singularities via Informational Thermodynamics**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20681174.svg)](https://doi.org/10.5281/zenodo.20681174)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-green.svg)]()
[![Status](https://img.shields.io/badge/Simulation_Status-Complete-brightgreen.svg)]()

This repository contains the complete numerical simulation framework for the **Quantum Constraint Framework (QCF)**, an extension to General Relativity designed to dynamically resolve spacetime singularities within black holes. Inspired by the postulates of Isomorphic Cosmic Equilibrium (ICE), QCF posits that a finite curvature ceiling ($K_{max} = 1/16$ in Planck units) is imposed on the interior geometry due to the saturation of the Bekenstein-Holographic entropy bound at the event horizon.

The accompanying script, `v4_sim.py`, calculates and visualizes critical physical signatures predicted by this framework across a vast mass spectrum ($10^9 \text{ kg}$ to $10^{31} \text{ kg}$).

---

## 💡 Core Theoretical Insights (What This Paper Says)

The QCF resolves the classical GR breakdown ($K \to \infty$ as $r \to 0$) by introducing a mandatory spatial cutoff radius, $\mathbf{r_{cut}}$, derived from:
$$\mathbf{r_{cut} = (192)^{1/6} r_s^{1/3} \ell_p^{2/3}}$$

This single constraint yields massive physical consequences:

*   **Singularity Elimination:** Curvature ($K$) is capped at $K_{max}$ for all $r < r_{cut}$, replacing the point singularity with a finite, quantum core.
*   **Modified Energy Scale ($\mathbf{E_{max}}$):** The maximum energy of emitted Hawking radiation shifts from the standard thermal scale ($k_B T_H$) to the much higher **Quantum Cutoff Energy**, $E_{max} = \hbar c / r_{cut}$.
*   **Altered Lifetimes:** Due to suppression of high-energy particle emission, black hole evaporation times ($\tau$) are *extended* compared to standard GR predictions.

---

## 💻 Simulation Capabilities (`v4_sim.py`)

The simulation script performs comprehensive numerical checks and generates seven figures visualizing the QCF predictions:

### **Key Outputs Demonstrated:**
1.  **Energy Scale Comparison (Fig 1):** Visualizing $E_{max}(M)$ against $k_B T_H(M)$ overlaid with Fermi-LAT and IceCube observational constraints.
2.  **Lifetime Scaling (Fig 2):** Direct comparison of $\tau_{Standard}$ vs. $\tau_{QCF}$, showing how QCF extends the lifetime, especially for lighter PBHs.
3.  **Spectral Truncation (Fig 3):** Shows the standard Planck spectrum being abruptly cut off by $E_{max}$ for a representative BH ($M=5 \times 10^{11} \text{ kg}$).
4.  **Curvature Ceiling (Fig 4 & Fig 7):** Detailed visualization of how $K/K_{max}$ saturates at the cutoff radius, both in normalized and physical units ($\text{for } M_{\odot}$).
5.  **Phenomenological Shifts (Fig 6):** Plots the fractional corrections to temperature ($\Delta T_H/T_H$) and QNM frequencies ($\delta\omega/\omega$).

---

## 🚀 How To Run The Simulation

This project requires Python 3.9 or newer.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/andrewrodger73/QCF.git
    cd QCF_Paper_Repo
    ```
2.  **Install Dependencies:**
    ```bash
    pip install numpy matplotlib
    ```
3.  **Execute the Simulation:**
    ```bash
    python v4_sim.py
    ```

### 📁 Output Structure:
The simulation will create a `/results/` directory containing all generated figures (PNG format):
*   `Fig1_Emax_observational.png`
*   `Fig2_lifetime_comparison.png`
*   `Fig3_spectrum_M5e11kg.png`
*   ... and so on, up to `Fig7_summary_all_predictions.png`.

---

## 🧐 Quick Sanity Check (Unit Tests)

The script includes embedded unit tests that confirm key relations:
*   ✅ Primordial cutoff radius ($M=10^{12} \text{ kg}$) is within $5\%$ tolerance of theoretical expectation.
*   ✅ The thermal energy scale for a test mass falls correctly within the GeV-TeV range expected from current observations.

---
***"The World isn't broken. We’re just running the wrong diagnostics."*** - Andrew Rodger (Author) 😉
