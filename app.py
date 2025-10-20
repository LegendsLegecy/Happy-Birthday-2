from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def birthday_surprise():
    return render_template('index.html')

@app.route('/birthday')
def birthday_surprise_page():
    return render_template('birthday_surprise.html')
