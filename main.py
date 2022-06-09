from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login/", methods=["POST"])
def login():
    name = request.form['name']
    # name = request.args.get('name', type=str)
    password = request.form['password']
    # password = request.args.get('password', type=str)
    print(name, password)
    return render_template("login.html", name=name, password=password)


if __name__ == "__main__":
    app.run(debug=True)
