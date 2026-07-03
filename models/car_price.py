import pickle

with open("saved_pkl/car_model.pkl", "rb") as f:
    model = pickle.load(f)

def car_predict(data):

    prediction=model.predict(data)

    return prediction[0]