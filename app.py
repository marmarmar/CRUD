from flask import Flask, render_template, redirect, url_for, request
from database import Database
from socks import Product

app = Flask(__name__)


@app.route('/')
def index():
    socks_list = Product.list_products()
    return render_template("index.html", socks=socks_list)

@app.route('/add', methods=['GET', 'POST'])
def add_socks():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template("form.html")



if __name__ == "__main__":
    Database.make_db()
    app.run(debug=True)