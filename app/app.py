from flask import Flask, render_template
from settings import HOST_IP
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings_page():
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(debug=True, host=HOST_IP)
