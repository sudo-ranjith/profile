"""
Created by sudo-ranjith at 11/04/20

Feature: #Enter feature name here
# Enter feature description here

Scenario: # Enter scenario name here 
"""

from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/corona')
def corona_dashboard():
    return render_template("/templates/home.html")
