from flask import Flask, render_template, request
import json

app = Flask(__name__)

name = field1 = ''
data = []
endpoint = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    api_running = False
    if request.method == 'POST':
        global name
        global field1
        global endpoint
        name = request.form['name']
        field1= request.form['field1']
        number = request.form['number']
        make_data(int(number))
        endpoint = name
        return render_template('form.html', api_running=True, api_name=name)
    return render_template('form.html')


@app.route('/get', methods=['GET'])
def get_request():
    return json.dumps(data), 200

@app.route('/post', methods=['POST'])
def post_request():
    if request.method == 'POST':
        global data
        obj = dict(id = len(data) + 1, field1 = request.form[''])
        data.append(obj)
        return 'success', 200

@app.route('/delete/<id>', methods=['DELETE'])
def del_request(id):
    if request.method == 'DELETE':
        global data
        del data[int(id) - 1]
        return 'success', 200

# @app.route('/put/<id>', methods=['PUT'])
# def put_request(id):
#     if request.method == 'PUT':
#         global data
#         print request.form
#         return request.form['js']


def make_data(number):
    global data
    data = []
    for i in xrange(number):
        obj = dict(id = i + 1, field1=str(field1) + " " + str(i+1))
        data.append(obj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)