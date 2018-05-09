from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/new', methods=['POST'])
def dojo_new():
    name = request.form['name']
    email = request.form['email']
    return render_template('dojo.html')
app.run(debug=True)