import joblib
import pandas as pd

def load_model():
    model = joblib.load("model/salary_model.pkl")
    return model

def predict_salary(input_dict):
    model = load_model()

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(input_df)[0]
    return ">50K" if prediction == 1 else "<=50K"