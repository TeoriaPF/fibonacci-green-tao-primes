python
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from generator import generate_primes, find_green_tao_ap

def train_predictive_model():
    print("[ML] Duke gjeneruar të dhënat e trajnimit...")
    primes = generate_primes(5_000_000)
    
    # Bashkojmë të dhënat e sekuencave normale dhe atyre që mbijetojnë
    df_ap4 = find_green_tao_ap(primes, k_length=4)
    df_ap5 = find_green_tao_ap(primes, k_length=5)
    df_ap5['survived_to_higher'] = 1
    
    df = pd.concat([df_ap4, df_ap5], ignore_index=True).drop_duplicates(subset=['start_prime', 'gap'])
    
    X = df[['start_prime', 'gap_mod8', 'gap_mod34', 'macro_ratio']]
    y = df['survived_to_higher']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_split=0.2, random_state=42)
    
    print("[ML] Duke trajnuar modelin e avancuar Gradient Boosting...")
    model = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"\n🚀 SAKTËSIA E MODELIT: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("\nRaporti i Klasifikimit:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_predictive_model()
