from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/services')
def services():
    return render_template('services.html')
