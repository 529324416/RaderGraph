from flask import Flask
from flask.signals import request_tearing_down
from flask.templating import render_template
from flask import request
from graph import render_graph
from gevent.pywsgi import WSGIServer
import json

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("test.html")

@app.route("/testInterface")
def testInterface():

    return render_graph([0,10,20,30,40,50,60]).dump_options_with_quotes()

@app.route("/render_graph",methods=["POST"])
def render_your_graph():

    if request.method == 'POST':
        data = [int(v) for k,v in request.json.items()]
        print(data)
        return render_graph(data).dump_options_with_quotes()
        

if __name__ == "__main__":

    http_server = WSGIServer(('0.0.0.0', int(5000)), app)
    http_server.serve_forever()