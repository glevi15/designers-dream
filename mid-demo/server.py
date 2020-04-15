from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import json
import base64
from binascii import a2b_base64
import urllib

from flask import Flask, jsonify, request, render_template

# class Model(object):
#     def __init__(self):
#         self.session = tf.Session()
#         self.session.__enter__()

#         model_dir = "model"
#         self.saver = tf.train.import_meta_graph(model_dir + "/export.meta")
#         self.saver.restore(self.session, model_dir + "/export")

#     def predict(self, imageData):
#         input_instance = dict(input=base64.urlsafe_b64encode(imageData).decode("ascii"), key="0")
#         input_instance = json.loads(json.dumps(input_instance))

#         input_vars = json.loads(tf.get_collection("inputs")[0].decode())
#         output_vars = json.loads(tf.get_collection("outputs")[0].decode())
#         input = tf.get_default_graph().get_tensor_by_name(input_vars["input"])
#         output = tf.get_default_graph().get_tensor_by_name(output_vars["output"])

#         input_value = np.array(input_instance["input"])
#         output_value = self.session.run(output, feed_dict={input: np.expand_dims(input_value, axis=0)})[0]

#         output_instance = dict(output=output_value.decode("ascii"), key="0")
#         b64data = output_instance["output"]
#         b64data += "=" * (-len(b64data) % 4)
#         output_data = base64.urlsafe_b64decode(b64data.encode("ascii"))
        
#         return output_data

# model = Model()

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    print('Incoming..')  # parse as JSON
    imageDataURI = request.get_json()['imageData']
    imageData = urllib.request.urlopen(imageDataURI).read()
    
    print('running model...')
    out_data = run_model(imageData)
    # out_data = model.predict(imageData)

    out_data = str(base64.b64encode(out_data))
    return_data = {'imageData': u'data:image/png;base64,%s' % out_data[2:-1]}

    print("done")
    return jsonify(return_data), 200


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

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

