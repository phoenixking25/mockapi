from flask import Flask, render_template, request
import json

app = Flask(__name__)

fields = []
data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    api_running = False
    if request.method == 'POST':
        print len(request.form)
        print request.form["field" + str(0+1)]
        for i in xrange(len(request.form) - 2):
            fields.append(str(request.form["field" + str(i+1)]))
        number = request.form['number']
        make_data(int(number))
        return render_template('form.html', api_running=True)
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

@app.route('/get/<id>', methods=['GET'])
def get_item(id):
    global data
    print len(data)
    return json.dumps(data[int(id) - 1]), 200

@app.route('/delete/<id>', methods=['DELETE'])
def del_request(id):
    if request.method == 'DELETE':
        global data
        del data[int(id) - 1]
        return 'success', 200


def make_data(number):
    global data
    global fields
    data = []
    obj = {}
    for i in xrange(number):
        obj['id'] = i + 1
        print obj['id']
        for j in fields:
            obj[j] = j + " " + str(i + 1)
        data.append(obj)
        obj = {}

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)