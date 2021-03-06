from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os
from sqlalchemy.sql import text
from sqlalchemy.exc import OperationalError

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)


    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or \
                "sqlite:///" + os.path.join(basedir, "app.db")

    db = SQLAlchemy(app)

    class Product(db.Model):
	    id = db.Column(db.Integer, primary_key=True)
	    name = db.Column(db.String(50))
	    price = db.Column(db.String(50))
	    
	    def all_products():
		    return Product.query.all()
		    
		    
    class Store(db.Model):
	    id = db.Column(db.Integer, primary_key=True)
	    name = db.Column(db.String(50))
	    
    class Stock(db.Model):
        
        pid = db.Column(db.Integer, primary_key=True)
        sid = db.Column(db.Integer, primary_key=True)
        stock_count = db.Column(db.Integer)
        
        
    @app.route("/")
    def index():
	    products = Product.all_products()
	    return render_template('index.html', products=products)


    @app.route("/search")
    def search():
	    query = request.values.get("q")
        
	    if query == "":
		    return render_template('search.html')
		    
	    if query is not None:
		    try:
			    result = db.session.query(Product).filter(text("name LIKE '%%%s%%'" % query)).all()
			    #result = db.session.query(Product).filter(Product.name.like('%%%s%%' % query)).all()
		    except OperationalError as e:
			    flash(str(e))
			    return redirect(url_for("search"))
	    
		    return render_template('search.html',result=result)
	    return render_template('search.html')
    
    @app.route("/product")
    def product():
        id = request.values.get('product')
        product = Product.query.filter_by(id=id).first()
        return render_template('product.html', product=product)
        
    @app.route('/_check_stock')
    def check_stock():
        pid = request.args.get('productID', 0, type=int)
        store = request.args.get('store')     
        
        store = Store.query.filter_by(name=store).first()        
        stock = Stock.query.filter_by(pid=pid,sid=store.id).first()
        
        return jsonify(result=stock.stock_count)
 

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("404.html"), 404

    return app
    

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
