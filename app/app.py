from flask import Flask, render_template
from settings import HOST_IP
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings_page():
    return render_template('settings.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host=HOST_IP)
