"""
Created by sudo-ranjith at 11/04/20

Scenario: # this is a sample flask application, that uses blueprint feature.
"""
from flask import Flask, request, jsonify, render_template, Blueprint


app = Flask(__name__)
auth_api = Blueprint('auth', __name__)


@auth_api.route('/home')
def home():
    return jsonify({"message": "welcome flask dev, now it is automated"})
