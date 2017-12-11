from flask_api import FlaskAPI
from run import endpoint

app = FlaskAPI(__name__)


@app.route('/' + endpoint, methods =  method)
def getrequest():
    return {"status": "ok"}, 200

def runapi(port):
    if __name__ == '__main__':
        app.run(port=port, debug=True, threaded=False, processes=1)