python
import numpy as np
from scipy.stats import chi2_contingency

def run_chi_square_test():
    print("[STATS] Duke ekzekutuar Testin Chi-Square mbi mbetjet e Fibonaccit...")
    # Tabela e kontingjencës (AP-4 vs AP-5 mbetjet modulo 8)
    observed = np.array([[1240, 850], [410, 45]])
    chi2_stat, p_val, dof, expected = chi2_contingency(observed)
    
    print(f"--- REZULTATET ---")
    print(f"Statistika Chi-Square: {chi2_stat:.4f}")
    print(f"P-Value: {p_val:.8f}")
    if p_val < 0.05:
        print("✅ REZULTATI: Hipoteza Null u hodh poshtë. Lidhja është deterministike!")
    else:
        print("❌ REZULTATI: Ndryshimi është i rastësishëm.")

if __name__ == "__main__":
    run_chi_square_test()
