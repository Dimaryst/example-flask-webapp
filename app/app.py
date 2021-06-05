from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hi_page')
def hi():
    return "<h1>HI! My dear friend!</h1>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
