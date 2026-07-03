import pickle

with open("saved_pkl/diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load scaler
with open("saved_pkl/scaler_diabetes.pkl", "rb") as file:
    scaler = pickle.load(file)

def diabetes_prediction(data):

    scaler_data=scaler.transform(data)

    prediction_data = model.predict(scaler_data)

    return prediction_data[0]