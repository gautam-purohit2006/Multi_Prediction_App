import pickle

with open("saved_pkl/emp_salary.pkl","rb") as file:
    emp_model = pickle.load(file)

def emp_prediction(data):

    emp_predict = emp_model.predict(data)

    return emp_predict[0]