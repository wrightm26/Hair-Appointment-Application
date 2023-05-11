from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/locservices')
def locservices():
    return render_template('locservices.html')

@app.route('/braidservices')
def braidservices():
    return render_template('braidservices.html')

@app.route('/gallery')
def braidservices():
    return render_template('gallery.html')
