from flask import Flask, jsonify, request

app = Flask(__name__)

# localhost:5000
@app.route('/')
def home():
    return jsonify(message='Hello World!'), 200

# localhost:5000/check?name=Kabbya&age=22
@app.route('/check')
def check():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    
    if (age < 18):
        return jsonify(message=f'Sorry {name}, you are not old enough.'), 401
    else:
        return jsonify(message=f'Welcome {name}, you can proceed...')
    
# localhost:5000/check_param/Kabbya/11
@app.route('/check_param/<string:name>/<int:age>')
def check_param(name: str, age: int):
    if (age < 18):
        return jsonify(message=f'Sorry {name}, you are not old enough.'), 401
    else:
        return jsonify(message=f'Welcome {name}, you can proceed...')

if __name__ == '__main__':
    app.run(debug=True)