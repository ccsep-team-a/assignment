from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    @app.route('/')
    def index():
        return 'Index Page'
        
    @app.route("/1")
    def test1():
        return render_template('test.html')

    @app.route("/2")
    def test2():
        return render_template('test2.html')

    @app.route("/3")
    def test3():
        return render_template('test3.html')
    return app
    

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
