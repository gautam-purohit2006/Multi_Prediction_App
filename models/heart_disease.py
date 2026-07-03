import pickle

with open("saved_pkl/Heart_Disease.pkl", "rb") as f:
    heart_model = pickle.load(f)

def heart_prediction(data):

    prediction = heart_model.predict(data)

    # print("CODE :", prediction)
    return prediction[0]
    # return "POST OK"
