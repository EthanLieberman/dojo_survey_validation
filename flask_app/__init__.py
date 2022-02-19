# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"          #<-- literally anything

MyCustomDB = 'dojo_survey_schema'         #<-- reference source for the name of the current database all model files can use