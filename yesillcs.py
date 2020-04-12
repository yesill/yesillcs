from flask import Flask, render_template

app = Flask(__name__)

@app.route("https://glacial-brook-22958.herokuapp.com/")
def page_index():
    return render_template('index.html')

@app.route("https://glacial-brook-22958.herokuapp.com/notifications")
def page_notifications():
    return render_template('notifications.html')

@app.route("https://glacial-brook-22958.herokuapp.com/login")
def page_login():
    return render_template('login.html')

@app.route("https://glacial-brook-22958.herokuapp.com/logs")
def page_logs():
    return render_template('logs.html')

app.run()