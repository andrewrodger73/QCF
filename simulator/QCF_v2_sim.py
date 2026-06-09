import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs('results', exist_ok=True)

G=6.67430e-11; c=299792458.0; hbar=1.054571817e-34
h=6.62607015e-34; kB=1.380649e-23
l_p=np.sqrt(hbar*G/c**3)

def r_s(M): return 2*G*M/c**2
def r_cut(M): return 192**(1/6)*r_s(M)**(1/3)*l_p**(2/3)
def E_max(M): return h*c/(2*np.pi*r_cut(M))
def T_H(M): return hbar*c**3/(8*np.pi*G*M*kB)
def lifetime_std(M): return 5120*np.pi*G**2*M**3/(hbar*c**4)
def K_schw(r,M): return 48*G**2*M**2/(c**4*r**6)
K_max=1/(16*l_p**4)

def planck_safe(x):
    x=np.asarray(x); out=np.empty_like(x,dtype=float)
    small=x<100; out[small]=x[small]**3/np.expm1(x[small])
    large=~small; out[large]=x[large]**3*np.exp(-x[large]); out[x==0]=0; return out

def power_fraction(M):
    x_max=E_max(M)/(kB*T_H(M))
    if x_max>700: return 1.0
    xs=np.linspace(0,x_max,20000)
    return np.trapz(planck_safe(xs),xs)/(np.pi**4/15)

# ---- Figure 1-3 : PBH sweep ----
masses=np.logspace(9,17,200)
Ecut=np.array([E_max(m) for m in masses])/1.60218e-19
tau_std=np.array([lifetime_std(m) for m in masses])/(3600*24*365.25)
frac=np.array([power_fraction(m) for m in masses])
tau_qcf=tau_std/np.maximum(frac,1e-30)

plt.figure(figsize=(9,4)); plt.loglog(masses,Ecut); plt.axhspan(1e8,1e11,alpha=0.2,color='orange')
plt.xlabel('M [kg]'); plt.ylabel('E_max [eV]'); plt.title('QCF E_max'); plt.grid(True,which='both',alpha=0.3)
plt.tight_layout(); plt.savefig('results/Fig1_Emax.png',dpi=150); plt.show()

plt.figure(figsize=(9,4)); plt.loglog(masses,tau_std,label='Standard'); plt.loglog(masses,tau_qcf,label='QCF',lw=2)
plt.axhline(13.8e9,c='k',ls='--'); plt.xlabel('M [kg]'); plt.ylabel('Lifetime [yr]'); plt.legend()
plt.title('QCF lifetimes'); plt.grid(True,which='both',alpha=0.3)
plt.tight_layout(); plt.savefig('results/Fig2_lifetime.png',dpi=150); plt.show()

M0=5e11; x=np.logspace(-1,3,800); E=x*kB*T_H(M0); spec=planck_safe(x)
x_max=E_max(M0)/(kB*T_H(M0)); spec_qcf=np.where(x<=x_max,spec,0)
plt.figure(figsize=(8,4)); plt.loglog(E/1.60218e-19,spec,label='Standard'); plt.loglog(E/1.60218e-19,spec_qcf,label='QCF',lw=2)
plt.axvline(E_max(M0)/1.60218e-19,c='r',ls=':'); plt.axvspan(1e8,1e11,alpha=0.15,color='orange')
plt.xlabel('E [eV]'); plt.ylabel('flux'); plt.title('Spectrum M=5e11 kg'); plt.legend(); plt.grid(True,which='both',alpha=0.3)
plt.tight_layout(); plt.savefig('results/Fig3_spectrum.png',dpi=150); plt.show()

# ---- Figure 4 : K/Kmax solar ----
M_sun=1.98847e30; rs=r_s(M_sun); rc=r_cut(M_sun)
r=np.logspace(np.log10(rc*0.9),np.log10(20*rs),500)
ratio=K_schw(r,M_sun)/K_max; ratio_c=np.minimum(ratio,1)
plt.figure(figsize=(8,5)); plt.loglog(r/rs,ratio,'--',label='GR'); plt.loglog(r/rs,ratio_c,lw=2,label='QCF')
plt.axvline(rc/rs,c='r',ls=':'); plt.axhline(1,c='k',lw=1); plt.xlabel('r/r_s'); plt.ylabel('K/K_max')
plt.title('Solar-mass curvature ceiling'); plt.legend(); plt.grid(True,which='both',alpha=0.3)
plt.tight_layout(); plt.savefig('results/Fig4_KKmax.png',dpi=150); plt.show()

print('QCF v1.0 complete - 4 figures saved')
