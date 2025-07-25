import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_model():
    # Load data
    df = pd.read_csv("data/adult_3.csv")  
    
    # Clean column names: strip, lower, replace spaces
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Clean income strings: strip whitespace, convert to str just in case
    df["income"] = df["income"].astype(str).str.strip()
    
    # Map income to numeric labels (adjust mapping if your labels differ!)
    label_map = {"<=50K": 0, ">50K": 1}
    df["income"] = df["income"].map(label_map)
    
    # Check how many rows got mapped (dropped those that don't match)
    df = df[df["income"].isin([0, 1])]
    
    if df.empty:
        raise ValueError("No rows left after filtering with valid income labels. Check your CSV and mapping.")
    
    # Drop rows with missing values just in case
    df = df.dropna()
    
    # Define features and target
    X = df.drop(columns=["income"])
    y = df["income"]
    
    # Handle categorical variables if any (e.g., do one-hot encoding)
    # Minimal example: let's just convert categorical columns to dummy variables
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    if categorical_cols:
        X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
        
    # Model training
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    
    # Predict & evaluate
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/salary_model.pkl")
    print("Model saved at model/salary_model.pkl")

if __name__ == "__main__":
    train_model()