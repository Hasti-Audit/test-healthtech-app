import pickle
import sqlite3

# NC-B5: Hardcoded credentials
DB_PASSWORD = "SuperSecretPassword123!"
API_TOKEN = "sk_live_51H8..."

def load_ml_model(filepath):
    # NC-B1: pickle.load without safeguard
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

def get_patient_record(patient_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    # NC-B4: SQL Injection
    query = f"SELECT * FROM patients WHERE id = '{patient_id}'"
    cursor.execute(query)
    return cursor.fetchall()

def preprocess_data(X_train, X_test):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    # NC-B3: Data Leakage
    X_all = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_all, X_test_scaled
