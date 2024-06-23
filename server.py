import datetime
import smtplib
from flask import Flask, render_template, request, redirect, url_for
from models import user_model, car_model, manufacturer_model

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')

@app.route('/')
def root():
    return render_template('login.html')


@app.route('/index.html')
def home():
    cars = car_model.get_all_cars()
    return render_template('index.html', cars= cars)


@app.route('/login.html', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        res = user_model.login(username, password)
        if res['status'] == 200:
            global user
            user = res['user']
            return redirect(url_for('home')) 
        elif res['status'] == 400:
            error = "Invalid credentials, please try again."
        else:
            return redirect(url_for('register'))

    return render_template('login.html', error=error)



@app.route('/register.html', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        adderss = request.form['adderss']
        age = request.form['age']
        creditcard = request.form['creditcard']
        res = user_model.create_user({'user_name':username, 'password':password, 'user_email':email, 'user_address':adderss, 'user_age':age, 'credit_card':creditcard})
        if res['status'] == 200:
            global user
            user = res['new user']
            return redirect(url_for('home')) 
        else:
            error = "A problem occurred, please try again."

    return render_template('register.html', error=error)


@app.route('/carDetails', methods=['GET'])
def carDetails():
    car_id = request.args.get('car_id')
    if car_id:
        car = car_model.get_car_by_id(car_id)
        if car:
            manu = manufacturer_model.get_manufacturer_by_id(car[3])
            car_data = {
                'model': car[1],
                'color': car[2],
                'manufacturer': manu[1],
                'manufacturer_date': car[4],
                'licence_num': car[5],
                'price': car[6],
                'num_seats': car[7],
                'car_pic': car[8]
            }
            return render_template('carDetails.html', car=car_data)
        else:
            return "Car not found", 404
    else:
        return "Car ID not provided", 400


if __name__ == '__main__':
    app.run(port=3000)