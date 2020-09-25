from app import app
from flask import render_template

@app.route('/rock/scissors')
def index():
    return "Players 1 wins by playing rock"