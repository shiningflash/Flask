from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    student_list = requests.get('http://127.0.0.1:8000/students').json()
    return jsonify(student_list)


@app.route('/students', methods=['GET', 'POST'])
def students():

    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        address = request.form['address']
        # print(student_id, name, address)
        url = 'http://127.0.0.1:8000/students/create'
        myobj = {
            'student_id': student_id,
            'name': name,
            'address': address
        }
        try:
            req = requests.post(url, data=myobj)
            print(req.text)
        except Exception as e:
            print(e)
        return redirect(url_for('home'))


@app.route('/employees', methods=['GET'])
def employees_list():
    employees_list = requests.get("http://127.0.0.1:8000/api/employees").json()
    return jsonify(employees_list)


@app.route('/employees/create', methods=['GET', 'POST'])
def create_employee():

    if request.method == 'GET':
        global departments_list
        departments_list = requests.get("http://127.0.0.1:8000/api/departments").json()
        departments_name = [departments_list[i]['name'] for i in range(len(departments_list))]
        return render_template('employee_form.html', departments_name=departments_name)

    elif request.method == 'POST':
        department_str = request.form['department']
        departments = [department['id'] for department in departments_list if department['name'] == department_str]

        employee_id = request.form['employee_id']
        name = request.form['name']
        address = request.form['address']
        url = 'http://127.0.0.1:8000/api/employees'
        myobj = {
            'employee_id': employee_id,
            'name': name,
            'address': address,
            'department': int(departments[0])
        }
        try:
            req = requests.post(url, data=myobj)
            print(req.text)
        except Exception as e:
            print(e)
        return redirect(url_for('employees_list'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
