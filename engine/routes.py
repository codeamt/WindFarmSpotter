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
  instructions = "Welcome to WindSpotter!\n\nThis API exposes a model for inferring wind farm capacity of \
  satellite imagery input.\n\nSample test images are located in the root > data > test.\n\nThe API is comprised of the following endpoints:"


  samples = glob.glob("%s/*" % app.config['SAMPLE_FOLDER'])

  if request.is_json:
    return jsonify(instructions)
  else:
    return render_template('index.html', samples=samples)


@app.route("/predict", methods=["POST"])
def predict():

  label_map = {
     "turbines_low_capacity": "Low Capacity Wind Farm",
     "turbines_medium_capacity": "Medium Capacity Wind Farm",
     "turbines_high_capacity": "High Capacity Wind Farm",
     "no_turbines_no_potential": "Not a Turbine Farm",
     "no_turbines_low_potential": "Potential Low Capacity Wind Farm",
     "no_turbines_med_potential": "Potential Medium Capacity Wind Farm",
     "no_turbines_high_potential": "Potential High Capacity Wind Farm"
  }

  windfarmspotter_model = WindFarmSpotter(app.config["PATH"])
  windfarmspotter_model.model.model.eval()


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




