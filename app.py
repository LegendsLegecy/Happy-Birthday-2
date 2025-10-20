from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def birthday_surprise():
    return render_template('index.html')

@app.route('/birthday')
def birthday_surprise_page():
    return render_template('birthday_surprise.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')
