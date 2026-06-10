import os
import numpy as np
import matplotlib.pyplot as plt

# Create output results directory
os.makedirs('results', exist_ok=True)

# =============================================================================
# --- PHYSICAL CONSTANTS (SI UNITS) ---
# =============================================================================
G = 6.67430e-11
c = 299792458.0
hbar = 1.054571817e-34
h = 6.62607015e-34
kB = 1.380649e-23
l_p = np.sqrt(hbar * G / c**3)
K_max = 1 / (16 * l_p**4)
M_sun = 1.98847e30 # for paper scaling formulas

# =============================================================================
# --- CORE MATHEMATICAL EQUATIONS FROM PAPER ---
# =============================================================================
def r_s(M):
    return 2 * G * M / c**2

def r_cut(M):
    # Equation (10): r_cut = 192^(1/6) * r_s^(1/3) * l_p^(2/3)
    return 192**(1/6) * r_s(M)**(1/3) * l_p**(2/3)

def E_max(M):
    return h * c / (2 * np.pi * r_cut(M))

def T_H(M):
    return hbar * c**3 / (8 * np.pi * G * M * kB)

def lifetime_std(M):
    return 5120 * np.pi * G**2 * M**3 / (hbar * c**4)

def K_schw(r, M):
    return 48 * G**2 * M**2 / (c**4 * r**6)

def delta_T_fraction(M):
    # Paper Eq 11: ΔT_H/T_H ≃ l_p^2 / A_H ≈ 2.38e-78 (M_sun/M)^2
    A_H = 4 * np.pi * r_s(M)**2
    return l_p**2 / A_H

def delta_omega_fraction(M):
    # Paper Eq 12: δω/ω ∼ (l_p / r_s)^{4/3} ≈ 9.6e-52 (M_sun/M)^{4/3}
    return (l_p / r_s(M))**(4/3)

# =============================================================================
# --- THERMODYNAMIC INTEGRATION ENGINE ---
# =============================================================================
def planck_safe(x):
    x = np.asarray(x)
    out = np.empty_like(x, dtype=float)
    small = x < 100
    out[small] = x[small]**3 / np.expm1(x[small])
    large = ~small
    out[large] = x[large]**3 * np.exp(-x[large])
    out[x == 0] = 0
    return out

def power_fraction(M):
    x_max = E_max(M) / (kB * T_H(M))
    if x_max > 700:
        return 1.0
    xs = np.linspace(0, x_max, 20000)
    return np.trapz(planck_safe(xs), xs) / (np.pi**4 / 15)

# =============================================================================
# --- GRAPHICS GENERATION RUN ---
# =============================================================================
def run_original_simulation():
    print("Executing master simulation script...")

    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('default')

    masses = np.logspace(9, 17, 200)
    Ecut = np.array([E_max(m) for m in masses]) / 1.60218e-19
    tau_std = np.array([lifetime_std(m) for m in masses]) / (3600 * 24 * 365.25)
    frac = np.array([power_fraction(m) for m in masses])
    tau_qcf = tau_std / np.maximum(frac, 1e-30)

    print("[Generating]: Figure 1 -> results/Fig1_Emax.png")
    plt.figure(figsize=(9, 4))
    plt.loglog(masses, Ecut, color='C0')
    plt.axhspan(1e8, 1e11, alpha=0.2, color='orange')
    plt.xlabel('M [kg]'); plt.ylabel('E_max [eV]'); plt.title('QCF E_max')
    plt.grid(True, which='both', alpha=0.3); plt.tight_layout()
    plt.savefig('results/Fig1_Emax.png', dpi=300); plt.close()

    print("[Generating]: Figure 2 -> results/Fig2_lifetime.png")
    plt.figure(figsize=(9, 4))
    plt.loglog(masses, tau_std, label='Standard', color='C0')
    plt.loglog(masses, tau_qcf, label='QCF', color='C1', lw=2)
    plt.axhline(13.8e9, c='k', ls='--')
    plt.xlabel('M [kg]'); plt.ylabel('Lifetime [yr]'); plt.legend(); plt.title('QCF lifetimes')
    plt.grid(True, which='both', alpha=0.3); plt.tight_layout()
    plt.savefig('results/Fig2_lifetime.png', dpi=300); plt.close()

    print("[Generating]: Figure 3 -> results/Fig3_spectrum.png")
    M0 = 5e11
    x = np.logspace(-1, 3, 800)
    E = x * kB * T_H(M0)
    spec = planck_safe(x)
    x_max = E_max(M0) / (kB * T_H(M0))
    spec_qcf = np.where(x <= x_max, spec, 0)
    plt.figure(figsize=(8, 4))
    plt.loglog(E / 1.60218e-19, spec, label='Standard', color='C0')
    plt.loglog(E / 1.60218e-19, spec_qcf, label='QCF', color='C1', lw=2)
    plt.axvline(E_max(M0) / 1.60218e-19, c='r', ls=':')
    plt.axvspan(1e8, 1e11, alpha=0.15, color='orange')
    plt.xlabel('E [eV]'); plt.ylabel('flux'); plt.title('Spectrum M=5e11 kg')
    plt.legend(); plt.grid(True, which='both', alpha=0.3); plt.tight_layout()
    plt.savefig('results/Fig3_spectrum.png', dpi=300); plt.close()

    print("[Generating]: Figure 4 -> results/Fig4_KKmax.png")
    M_sun_local = 1.98847e30
    rs = r_s(M_sun_local); rc = r_cut(M_sun_local)
    r = np.logspace(np.log10(rc * 0.9), np.log10(20 * rs), 500)
    ratio = K_schw(r, M_sun_local) / K_max; ratio_c = np.minimum(ratio, 1)
    plt.figure(figsize=(8, 5))
    plt.loglog(r / rs, ratio, '--', label='GR', color='C0')
    plt.loglog(r / rs, ratio_c, lw=2, label='QCF', color='C1')
    plt.axvline(rc / rs, c='r', ls=':'); plt.axhline(1, c='k', lw=1)
    plt.xlabel('r/r_s'); plt.ylabel('K/K_max'); plt.title('Solar-mass curvature ceiling')
    plt.legend(); plt.grid(True, which='both', alpha=0.3); plt.tight_layout()
    plt.savefig('results/Fig4_KKmax.png', dpi=300); plt.close()

    print("[Generating]: Figure 5 -> results/Fig5_Kretschmann_Truncation.png")
    plt.figure(figsize=(11, 7.5))
    r_s_norm = 2.0
    r_cut_norm = 192**(1/6) * r_s_norm**(1/3)
    K_max_norm = 0.0625
    r_vals = np.linspace(0.001, 4.0, 1500)
    k_classic = (12 * r_s_norm**2) / (r_vals**6)
    k_abrupt = np.where(r_vals > r_cut_norm, k_classic, K_max_norm)
    # smooth core removed per paper Sec 5
    plt.plot(r_vals, k_classic, label=r'Classical Schwarzschild ($K \propto r^{-6}$)', color='C0', linewidth=1.5, linestyle=':')
    plt.plot(r_vals, k_abrupt, label=r'QCF Abrupt Cutoff ($K_{max} = 1/16$)', color='C2', linewidth=2.5)
    plt.axvline(x=r_cut_norm, color='gray', linestyle='--', alpha=0.6, label=f'$r_{{cut}}$ ({r_cut_norm:.2f})')
    plt.axvline(x=r_s_norm, color='green', linestyle='-', alpha=0.6, label=f'Event Horizon $r_s$ ({r_s_norm:.1f})')
    plt.axhline(y=K_max_norm, color='orange', linestyle='-.', alpha=0.7, label=r'$K_{max} = 0.0625$')
    plt.title('Quantum Constraint Framework: Singularity Elimination', fontsize=15, pad=12)
    plt.xlabel('Radial Coordinate $r$', fontsize=13); plt.ylabel('Kretschmann Scalar $K$', fontsize=13)
    plt.xlim(-0.1, 4.2); plt.ylim(0, 0.125); plt.grid(True, linestyle='-', alpha=0.2)
    plt.legend(loc='upper right', framealpha=0.9); plt.tight_layout()
    plt.savefig('results/Fig5_Kretschmann_Truncation.png', dpi=300); plt.close()

    print("[Generating]: Figure 6 -> results/Fig6_QCF_predictions.png")
    masses_pred = np.logspace(9, 31, 300)
    dT = np.array([delta_T_fraction(m) for m in masses_pred])
    domega = np.array([delta_omega_fraction(m) for m in masses_pred])
    plt.figure(figsize=(9, 5))
    plt.loglog(masses_pred, dT, label=r'$\Delta T_H/T_H \simeq l_p^2/A_H$', color='C0')
    plt.loglog(masses_pred, domega, label=r'$\delta\omega/\omega \sim (l_p/r_s)^{4/3}$', color='C1')
    plt.axvline(M_sun, color='k', ls='--', alpha=0.5, label=r'1 M$_\odot$')
    plt.axvline(1e12, color='gray', ls=':', alpha=0.5, label=r'PBH $10^{12}$ kg')
    plt.xlabel('M [kg]'); plt.ylabel('Fractional correction')
    plt.title('QCF Phenomenological Predictions (Paper Eq 11-12)')
    plt.legend(); plt.grid(True, which='both', alpha=0.3); plt.tight_layout()
    plt.savefig('results/Fig6_QCF_predictions.png', dpi=300); plt.close()

    print("\n==========================================================")
    print(" SUCCESS: Patched figures synced to results folder.")
    print("==========================================================")

if __name__ == "__main__":
    run_original_simulation()