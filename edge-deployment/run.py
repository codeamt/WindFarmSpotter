from engine import app
from engine.windfarmspotter_model import *

if __name__ == "__main__":
  app.run(host="127.0.0.1", debug=app.config['DEBUG'], port=app.config["PORT"], threaded=True)