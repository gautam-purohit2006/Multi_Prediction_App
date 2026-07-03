from flask import Flask, render_template, request
from models.spam_mail import predict_spam
from models.car_price import car_predict
from models.diabetes_check import diabetes_prediction
from models.gold_price_prediction import gold_prediction
from models.heart_disease import heart_prediction
from models.house_price import house_prediction
from models.employee_salary import emp_prediction
import numpy as np

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",active_page="index")


@app.route("/diabetes",methods=["GET","POST"])
def diabetes():

    result = " "

    if request.method == "POST":

        arr = np.array([list(map(float, request.form.values()))])

        # data = [[1,89,66,23,94,28.1,0.167,21]] # 0
        # data = [[6,148,72,35,0,33.6,0.627,50]] # 1

        prediction=diabetes_prediction(arr)

        result = prediction

    print(result)

    return render_template("diabetes.html",active_page="diabetes", prediction = result)

@app.route("/car",methods=["GET","POST"])
def car():
    result  = " "

    if request.method == "POST":

        arr = np.array([list(map(float, request.form.values()))])
        # data = [[2014 , 5.59  , 27000, 0 ,0 ,0, 1]]
        prediction=car_predict(arr)

        result = round(prediction, 2)

    print(result)

    
    return render_template("car.html",active_page="car", prediction = result)


@app.route("/spam", methods=["GET","POST"])
def spam_predict():
    result = " "

    if request.method == "POST":

        message = request.form["message"]
        result = predict_spam(message)

    print(result)

    return render_template(
        "spam.html",
        prediction=result
    )
    # return render_template("spam.html",active_page="spam")


@app.route("/gold", methods=["GET","POST"])
def gold():

    result = " "

    if request.method == "POST":

        arr = np.array([list(map(float, request.form.values()))])

        # data=[[1447.160034,78.370003 ,15.285, 1.474491]]

        prediction = gold_prediction(arr)

        result =  round(prediction, 2)

    print(result)

    return render_template("gold.html",active_page="gold" , prediction = result)


@app.route("/heart_prediction", methods=["GET","POST"])
def heart_pred():

    result = " "
    print("Method:", request.method)
    print("Form =", request.form)

    if request.method == "POST":

        # arr = np.array([list(map(float, request.form.values()))])

        # data=[[55,1,0,160,289,0,0,145,1,0.8,1,1,3]] # 0
        data=[[50,0,0,110,254,0,0,159,0,0,2,0,2]] # 1

        prediction_data = heart_prediction(data)

        result = prediction_data

    else:
        print("Error....gh......")    
        
    print(result)    
    return render_template("heart_prediction.html",active_page="heart" , prediction=result)


@app.route("/House_prediction", methods=["GET","POST"])
def House_prediction():

    result = " "

    if request.method == 'POST':

        arr = np.array([list(map(float, request.form.values()))])

        # data = [[3460,3,2,1,1,0,1,0,1,1,0,2]]
        # data = [[8520,3,1,1,1,0,0,0,1,2,0,2]]

        predict_data = house_prediction(arr)
        result = round(predict_data)

    print(result)
    return render_template("house.html",active_page="house" , prediction=result)

@app.route("/emp", methods=["GET","POST"])
def Emp_salary():

    result = " "

    if request.method == 'POST':

        arr = np.array([list(map(float, request.form.values()))])

        # data = [[24,0,4,1,3,1]]

        predict_data = emp_prediction(arr)
        result = round(predict_data)


    print(result)
    return render_template("emp.html",active_page="emp" , prediction=result)

app.run(debug=True)