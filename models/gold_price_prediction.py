import pickle

with open("saved_pkl/gold_prediction.pkl", "rb") as f:
    gold_model = pickle.load(f)

def gold_prediction(data):

    prediction = gold_model.predict(data)

    return prediction[0]
    # return "POST OK"