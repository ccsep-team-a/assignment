from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
    
@app.route("/1")
def test1():
    return render_template('test.html')

@app.route("/2")
def test2():
    return render_template('test2.html')


@app.route("/3")
def test3():
    return render_template('test3.html')
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
