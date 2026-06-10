# QCF Simulation Engine (v2.0.0)

This repository contains the core computational engine for the Quantum Constraint Framework (QCF). The script evaluates macroscopic thermodynamic properties, phenomenological boundaries, and interior geometric limits to simulate black hole behavior under a universal curvature ceiling.

---

## Script Architecture (`QCF_v2_sim.py`)

The simulation engine is structured around two distinct operational components executed in a single sequential sweep:

1. **Global Validation Engine**: Tracks mass sweeps ($10^9 \text{ kg}$ to $10^{31} \text{ kg}$) to calculate informational energy bounds, standard vs. QCF lifetimes, graybody spectral distributions, and formal boundary corrections ($\Delta T_H/T_H$ and $\delta\omega/\omega$).
2. **Interior Collapse Simulator**: Models a normalized geometric profile ($r_s = 2.0$) of matter falling inward toward $r \rightarrow 0$ to demonstrate the abrupt geometric "circuit breaker" mechanism that truncates the classical singularity.

---

## Core Invariants & Physics Logic

The script applies the framework's mathematical boundaries natively using SI units:

* **Curvature Ceiling ($K_{\text{max}}$)**: Enforces an absolute upper bound on the Kretschmann scalar based on the Planck length:
  $$K_{\text{max}} = \frac{1}{16 l_p^4}$$
* **Spatial Cutoff ($r_{\text{cut}}$)**: Computes the sub-linear coordinate boundary where the curvature ceiling takes effect:
  $$r_{\text{cut}} = 192^{1/6} r_s^{1/3} l_p^{2/3}$$
* **Section 6 Boundary Deviations**: Evaluates the ultra-small fractional corrections derived for the Hawking temperature and Quasi-Normal Mode (QNM) ringdown frequencies:
  $$\frac{\Delta T_H}{T_H} \simeq \frac{l_p^2}{A_H}, \quad \frac{\delta\omega}{\omega} \sim \left(\frac{l_p}{r_s}\right)^{4/3}$$

---

## Generated Visual Assets

Running the script automatically compiles and renders 6 publication-grade figures into the `results/` directory:

* **`Fig1_Emax.png`**: Plots the maximum informational energy threshold ($E_{\text{max}} \propto M^{-1/3}$) against a background overlay of the Fermi-LAT observational energy band ($10^8$ to $10^{11} \text{ eV}$).
* **`Fig2_lifetime.png`**: Validates the semiclassical correspondence principle, showing that QCF lifetime paths perfectly track standard GR lines for macroscopic masses.
* **`Fig3_spectrum.png`**: Evaluates the continuous graybody emission profile for a $5 \times 10^{11} \text{ kg}$ primordial black hole under a hard high-frequency truncation cliff.
* **`Fig4_KKmax.png`**: Maps the dimensionless $K/K_{\text{max}}$ ratio across a solar-mass horizon, showing where the continuum limit flattens into an invariant plateau.
* **`Fig5_Kretschmann_Truncation.png`**: Visualizes internal spatial collapse. It highlights the sharp, abrupt geometric truncation at $r_{\text{cut}}$ and excludes any ad-hoc smooth internal fluid core model.
* **`Fig6_QCF_predictions.png`**: Evaluates the explicit fractional corrections from Section 6 over a broad mass domain, inserting markers for $1 \text{ M}_{\odot}$ and $10^{12} \text{ kg}$ boundaries.

---

## Execution Guide

### 1. Setup Dependencies
Ensure your scientific Python environment has the baseline plotting and numerical packages installed:

```bash
pip install numpy matplotlib
```

### 2. Run the Engine
To fire the consolidated simulation suite and calculate all thermodynamic properties, spectral profiles, perturbation curves, and interior metrics:

```bash
python QCF_v2_sim.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

*Developed independently at maximum operational speed. Run the metrics, review the scripts, and audit the workings for yourself.*
