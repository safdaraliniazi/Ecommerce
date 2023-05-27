from flask import Flask, render_template
from database import load_products_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  products = load_products_from_db()
  return render_template('home.html', products=products)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
