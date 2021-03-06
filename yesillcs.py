from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template('index.html')

@app.route("/notifications")
def page_notifications():
    return render_template('notifications.html')

@app.route("/login")
def page_login():
    return render_template('login.html')

@app.route("/logs")
def page_logs():
    return render_template('logs.html')

if __name__ == "__main__":
    app.run()