from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World 123'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
