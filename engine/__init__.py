from flask import Flask
app = Flask(__name__)
app.config.from_object('engine.settings')

import engine.routes

