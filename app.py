from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Computer')
def Computer():
    return render_template("Computer.html")

@app.route('/Rams')
def Rams():
    return render_template("Rams.html")

@app.route('/Laptop')
def Laptop():
    return render_template("laptop.html")

@app.route('/Products')
def Products():
    return render_template("products.html")

@app.route('/About')
def About():
    return render_template("about.html")

@app.route('/Contact')
def Contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)

