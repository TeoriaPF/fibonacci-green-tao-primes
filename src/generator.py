python
import numpy as np
import pandas as pd

def generate_primes(n_max):
    """Gjeneron numrat primë duke përdorur Sieve of Eratosthenes."""
    sieve = [True] * n_max
    sieve[0] = sieve[1] = False
    for i in range(2, int(n_max**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n_max, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def find_green_tao_ap(primes, k_length=4, max_gap=200):
    """Kërkon progresione aritmetike Green-Tao (AP-k)."""
    prime_set = set(primes)
    progressions = []
    
    # Kërkojmë në një nënbashkësi për performancë
    for p in primes[:50000]:
        for g in range(6, max_gap, 6): # Diferencat e gjata duhet të plotpjesëtohen me 6
            is_ap = True
            for step in range(1, k_length):
                if (p + step * g) not in prime_set:
                    is_ap = False
                    break
            if is_ap:
                progressions.append({
                    'start_prime': p,
                    'gap': g,
                    'gap_mod8': g % 8,
                    'gap_mod34': g % 34,
                    'macro_ratio': g / np.log(p),
                    'survived_to_higher': 1 if k_length >= 5 else 0
                })
