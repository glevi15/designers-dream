from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import numpy as np
import json
import base64
from binascii import a2b_base64
import urllib
from pprint import pprint

from flask import Flask, jsonify, request, render_template

from flask_cors import CORS

PROJECT_ID_COUNTER = 0
database = {}
database["projects"] = {}
# if os.path.exists('db.json'):
#     with open('db.json') as json_file:
#         database = json.load(json_file)

app = Flask(__name__)
            # static_folder = "./dist/static",
            # template_folder = "./dist")
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/convert', methods=['POST'])
def convert():
    print('Incoming..')  # parse as JSON
    imageDataURI = request.get_json()['imageData']
    imageData = urllib.request.urlopen(imageDataURI).read()

    print('running model...')
    out_data = run_model(imageData)

    out_data = str(base64.b64encode(out_data))
    return_data = {'imageData': u'data:image/png;base64,%s' % out_data[2:-1]}
    
    print("done: ")
    return jsonify(return_data), 200

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_project() :
    text_data = request.get_data(as_text=True)
    json_data = json.loads(text_data)
    print("text: %s" % text_data)

    global PROJECT_ID_COUNTER

    id = PROJECT_ID_COUNTER
    database["projects"][id] = json_data
    database["projects"][id]["id"] = id
    # TODO return id of project from DB
    PROJECT_ID_COUNTER += 1
    print("Created new project with id %d" % id)

    with open('db.json', 'w') as outfile:
        json.dump(database, outfile)

    return jsonify({'id' : id})

@app.route('/save', methods=['POST'])
def save_project() :
    text_data = request.get_data(as_text=True)
    json_data = json.loads(text_data)

    id = json_data["id"]
    sketch_image = json_data["sketchImage"]
    result_image = json_data["resultImage"]

    database["projects"][id]["sketchImage"] = sketch_image
    database["projects"][id]["resultImage"] = result_image

    with open('db.json', 'w') as outfile:
        json.dump(database, outfile)

    return jsonify({'id' : id})

@app.route('/projects', methods=['GET'])
def get_projects() :
    return jsonify(database)

@app.route('/status', methods=['POST'])
def change_status() :
    text_data = request.get_data(as_text=True)
    json_data = json.loads(text_data)
    print("text: %s" % text_data)

    id = json_data["id"]
    status = json_data["status"]

    database["projects"][id]["status"] = status

    with open('db.json', 'w') as outfile:
        json.dump(database, outfile)

    return jsonify({'id' : id})

@app.route('/delete', methods=['POST'])
def delete_project() :
    text_data = request.get_data(as_text=True)
    json_data = json.loads(text_data)

    id = json_data["id"]

    if id in database["projects"]:
        del database["projects"][id]

        with open('db.json', 'w') as outfile:
            json.dump(database, outfile)

        return jsonify({'id' : id})

    return jsonify({id:-1})

def run_model(imageData):
    model_dir = "model"

    input_instance = dict(input=base64.urlsafe_b64encode(imageData).decode("ascii"), key="0")
    input_instance = json.loads(json.dumps(input_instance))

    b64data = None
    # force CPU
    config = tf.ConfigProto( device_count = {'GPU': 0})

    with tf.Session(config=config) as sess:
        saver = tf.train.import_meta_graph(model_dir + "/export.meta")
        saver.restore(sess, model_dir + "/export")

        input_vars = json.loads(tf.get_collection("inputs")[0].decode())
        output_vars = json.loads(tf.get_collection("outputs")[0].decode())
        input = tf.get_default_graph().get_tensor_by_name(input_vars["input"])
        output = tf.get_default_graph().get_tensor_by_name(output_vars["output"])

        input_value = np.array(input_instance["input"])
        output_value = sess.run(output, feed_dict={input: np.expand_dims(input_value, axis=0)})[0]

        output_instance = dict(output=output_value.decode("ascii"), key="0")

        b64data = output_instance["output"]
        b64data += "=" * (-len(b64data) % 4)
        output_data = base64.urlsafe_b64decode(b64data.encode("ascii"))

    return output_data

if __name__ == '__main__':
    app.run(debug=1)