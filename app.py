#!flask/bin/python
from flask import Flask
from flask import request
from sklearn.externals import joblib
import signals, suggestions
import os

clf = joblib.load('model2.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    # LOAD FILE
    sample_test = signals.Sample.load_from_file("./test_z.txt")

    # RESHAPE
    lin = sample_test.get_linearized(reshape=True)

    # PREDICT
    number = clf.predict(lin)

    # CONVERT WITH ASCII
    char = chr(ord('a') + number[0])
    print char
    return char

# /get-file?filename=abc.txt
@app.route('/get-file')
def query_example():
    filename = request.args.get('filename') #if key doesn't exist, returns None
    # LOAD FILE
    sample_test = signals.Sample.load_from_file("/Users/apple/nodejs/meo-hub-docker/node-red/data/training/"+filename)

    # RESHAPE
    lin = sample_test.get_linearized(reshape=True)

    # PREDICT
    number = clf.predict(lin)

    # CONVERT WITH ASCII
    char = chr(ord('a') + number[0])
    print char

    os.remove("/Users/apple/nodejs/meo-hub-docker/node-red/data/training/"+filename)

    return char

if __name__ == '__main__':
    app.run(debug=True)