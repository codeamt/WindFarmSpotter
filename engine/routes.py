from flask import Flask, request, jsonify, render_template
import logging
import time
import requests
import os
import base64
import glob
from engine import app
from engine.windfarmspotter_model import *
from werkzeug.utils import secure_filename


@app.route("/", methods=["GET"])
def index():
  samples = glob.glob("%s/*" % app.config['SAMPLE_FOLDER'])
  instructions = "Welcome to WindSpotter!\n\nThis API exposes a model for inferring wind farm capacity of \
  satellite imagery input.\n\nSample test images are located in the root > static > test_imgs.\n\nThe API is comprised of the following endpoints:\n\n/predict\n\n\n\nTo run inference on a sample image, make a POST request to the prediction endpoint.\n\n\n\nExample request:\n\n\n\ncurl -X POST http://127.0.0.1:5000/predict -H 'Content-Type: application/json'  -d '{'file':'~/wfs_inference_py/engine/static/test_imgs/test_low_capacity_7.jpg'}'"
  return jsonify({"instructions": instructions, "sample_file_names": samples})
  if request.args['type'] == 'json':
    return jsonify({"instructions": instructions, "sample_file_names": samples})
  else:
  return render_template('index.html', samples=samples)


@app.route("/predict", methods=["POST"])
def predict():
  windfarmspotter_model = WindFarmSpotter(app.config["PATH"])
  label_map = {
     "turbines_low_capacity": "Low Capacity Wind Farm",
     "turbines_medium_capacity": "Medium Capacity Wind Farm",
     "turbines_high_capacity": "High Capacity Wind Farm",
     "no_turbines_no_potential": "Not a Turbine Farm",
     "no_turbines_low_potential": "Potential Low Capacity Wind Farm",
     "no_turbines_med_potential": "Potential Medium Capacity Wind Farm",
     "no_turbines_high_potential": "Potential High Capacity Wind Farm"
  }


  if request.is_json:
    user_input = request.get_json()["file"]
    print(user_input)
    file_data = Path(user_input).read_bytes()
    #bytes_array = data.read_bytes()
    app.logger.info("Classifying satellite image %s" % (Path(user_input).name),)
    img = open_image(BytesIO(file_data))
    t = time.time()
    pred_class, pred_idx, outputs = windfarmspotter_model.model.predict(img)
    dt = time.time() - t
    app.logger.info("Execution time: %0.02f seconds" % (dt))
    app.logger.info("Image %s classified as %s" % (Path(user_input).name, pred_class))
    return jsonify({"prediction": label_map[str(pred_class)]})
  else:
    user_input = request.form["file"]#request.files.get('file')
    #basename = Path(user_input).name
    print(user_input)
    full_url = app.config["PATH"] + "/engine" + user_input
    file_data = Path(full_url).read_bytes()
    app.logger.info("Classifying satellite image %s" % (Path(user_input).name),)
    img = open_image(BytesIO(file_data))
    t = time.time()
    pred_class, pred_idx, outputs = windfarmspotter_model.model.predict(img)
    dt = time.time() - t
    app.logger.info("Execution time: %0.02f seconds" % (dt))
    app.logger.info("Image %s classified as %s" % (Path(user_input).name, pred_class))
    return jsonify({"prediction": label_map[str(pred_class)]})
