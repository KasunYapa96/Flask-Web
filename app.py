from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    # return render_template('index.html')
    return "Hello World"


@app.route('/<name>')
def user(name):
    return f"Hello {name}!"


@app.route('/admin')
def index():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
