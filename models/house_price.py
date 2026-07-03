import pickle

with open("saved_pkl/house.pkl","rb") as file:
    house_model=pickle.load(file)

def house_prediction(data):

    prediction = house_model.predict(data)

    return prediction[0]