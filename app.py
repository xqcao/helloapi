from flask import Flask, render_template
app = Flask(__name__, static_folder='apistatic')


@app.route('/')
def hello():
    return render_template('index.html', data='hello from svc index fun()')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)
