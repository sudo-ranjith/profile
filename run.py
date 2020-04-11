"""
Created by sudo-ranjith at 11/04/20


Scenario: # this is the run.py which will trigger the flask application
"""

from flask import Flask
from auth.views.app import auth_api
from dashboard.views.routes import dashboard_bp

application = Flask(__name__)
application.register_blueprint(auth_api, url_prefix='/api')
application.register_blueprint(dashboard_bp, url_prefix='/dashboard')

if __name__ == "__main__":
    application.run(debug=True)
