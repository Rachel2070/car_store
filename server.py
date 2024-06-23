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
            car_data = {
                'model': car[1],
                'color': car[2],
                'manufacturer': car[3],
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

# @app.route('/error_login.html')
# def error_login():
#     return render_template('error_login.html')
#
#
# @app.route('/schedule.html')
# def schedule():
#     student_name = username
#     student_class = schooluder_model.get_class_by_student(student_name)
#     data = schooluder_model.get_week_schedule_by_class(student_class)
#     day = datetime.datetime.today().weekday()
#     hour = datetime.datetime.now().hour
#     date = datetime.datetime.today().strftime('%A - %B %d:')
#     return render_template('schedule.html', week_schedule=data, day=day + 1, hour=hour, date=date,
#                            student_class=student_class)
#
#
# @app.route('/fun_task.html')
# def about_fun_tasks():
#     student_name = username
#     student_class = schooluder_model.get_class_by_student(student_name)
#     fun_tasks = fun_tasks_model.get_fun_tasks_by_grade(student_class)
#     print(fun_tasks)
#     fun_tasks_1 = fun_tasks[0:int(len(fun_tasks) / 2)]
#     fun_tasks_2 = fun_tasks[int(len(fun_tasks) / 2):len(fun_tasks)]
#     return render_template('fun_task.html', student_class=student_class, fun_tasks=fun_tasks, fun_tasks_1=fun_tasks_1,
#                            fun_tasks_2=fun_tasks_2)
#
#
# def send_email(user, pwd, recipient, subject, body):
#     FROM = user
#     TO = recipient if isinstance(recipient, list) else [recipient]
#     SUBJECT = subject
#     TEXT = body
#     # Prepare actual message
#     message = """From: %s\nTo: %s\nSubject: %s\n\n%s
#     """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.login(user, pwd)
#         server.sendmail(FROM, TO, message)
#         server.close()
#         print('successfully sent the mail')
#     except Exception as e:
#         print(e)
#         print("failed to send mail")
#
#
# @app.route('/contacts.html', methods=['GET', 'POST'])
# def contacts():
#     if request.method == 'POST':
#         teacher_name = request.form['teacher_name']
#         subject = request.form['subject']
#         msg = request.form['msg']
#         student_mail = request.form['student_mail']
#         password = request.form['password']
#         teacher_email = people_model.get_teacher_email_by_name(teacher_name)
#         send_email(student_mail, password, teacher_email, subject, msg)
#         return redirect(url_for('schedule'))
#     return render_template('contacts.html')
#
#
# @app.route('/tasks.html')
# def tasks():
#     global username
#     print(username)
#     tasks = task_model.get_student_tasks_by_name(username)
#     print(tasks)
#     return render_template('tasks.html', tasks=tasks)
#
#
# @app.route('/check')
# def check():
#     global username
#     is_done = request.args.get("done")
#     task_id = request.args.get("task_id")
#     if is_done == 'on':  # mean false
#         task_model.update_student_task_is_done(task_id, 0, username)
#     else:  # mean true
#         task_model.update_student_task_is_done(task_id, 1, username)
#     return tasks()
#
#
# @app.route('/teacher_task.html', methods=['GET', 'POST'])
# def teacher_post_task():
#     error = None
#     if request.method == 'POST':
#         grade = request.form['grade']
#         date = request.form['date']
#         date = datetime.datetime.strptime(date, '%Y-%m-%d')
#         day = date.weekday()
#         hour = request.form['hour']
#         subject = request.form['subject']
#         descr = request.form['descr']
#         upload_task_model.insert_task(grade, day, hour, date, descr)
#         return redirect(url_for('teacher_post_task'))
#     return render_template('teacher_task.html', error=error)
#
#
# @app.route('/teacher_fun_task.html', methods=['GET', 'POST'])
# def teacher_post_fun_task():
#     error = None
#     if request.method == 'POST':
#         grade = request.form['grade']
#         descr = request.form['descr']
#         link = request.form['link']
#         upload_fun_task_model.insert_fun_task(grade, descr, link)
#         return redirect(url_for('teacher_post_fun_task'))
#     return render_template('teacher_fun_task.html', error=error)
#
#
# @app.route('/teacher_schedule.html', methods=['GET', 'POST'])
# def teacher_post_lesson():
#     error = None
#     if request.method == 'POST':
#         grade = request.form['grade']
#         day = request.form['day']
#         hour = request.form['hour']
#         subject = request.form['subject']
#         zoom_link = request.form['zoom_link']
#         schooluder_model.insert_lesson_to_schedule(grade, day, hour, subject, zoom_link)
#         return redirect(url_for('teacher_post_lesson'))
#     return render_template('teacher_schedule.html', error=error)


if __name__ == '__main__':
    app.run(port=3000)
