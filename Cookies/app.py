from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        name = request.form['name']
        response = make_response(render_template('getcookie.html'))
        response.set_cookie('name', name)
        return response

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('name')
    return '<h1>Welcome, ' + name + '!</h1>'

if __name__ == "__main__":
    app.run()