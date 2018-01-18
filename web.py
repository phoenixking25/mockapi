from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

fields = []
data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    api_running = False # assuming first api is not running
    if request.method == 'POST':
        for i in xrange((len(request.form) - 2)/2): #getting no of fields and running for loop on that
            fields.append(dict(field_name = str(request.form["field" + str(i+1)]), datatype = int(request.form["datatype" + str(i+1)])))
            print fields #getting fields and respective datatype in a array
        number = request.form['number'] # getting no of records to be wanted
        make_data(int(number)) #calling function
        return render_template('form.html', api_running=True) #rendering data in html page
    return render_template('form.html')

@app.route('/get', methods=['GET'])
def get_request():
    return json.dumps(data), 200 # returning json data

# @app.route('/post', methods=['POST'])
# def post_request():
#     if request.method == 'POST':
#         global data
#         # obj = dict(id = len(data) + 1, request.form)
#         data.append(obj)
#         #return 'success', 200

@app.route('/get/<id>', methods=['GET'])
def get_item(id):
    global data
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
        for j in fields:
            if j["datatype"] == 1:
                obj[j["field_name"]] = j["field_name"] + " " + str(i + 1)
            elif j["datatype"] == 2:
                obj[j["field_name"]] = random.randrange(1316211567000, 1916211567000)
            elif j["datatype"] == 3:
                obj[j["field_name"]] = {}
            elif j["datatype"] == 4:
                obj[j["field_name"]] = False
            elif j["datatype"] == 5:
                obj[j["field_name"]] = random.randrange(0, 101)
            elif j["datatype"] == 6:
                obj[j["field_name"]] = []
        data.append(obj)
        obj = {}

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)