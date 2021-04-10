"""
Created by sudo-ranjith at 11/04/20


Scenario: # this is the run.py which will trigger the flask application
"""

from flask import Flask, render_template
from auth.views.app import auth_api
# from dashboard.views.routes import dashboard_bp

app = Flask(__name__)
app.register_blueprint(auth_api, url_prefix='/api')
# app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
@app.route('/profile')
def home():
    return render_template("index.html")


@app.route('/test_bot')
def with_bot():
    return render_template("index_bot.html")


@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
