from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login/")
def login():
    name = request.args.get('name', type=str)
    password = request.args.get('password', type=str)
    print(name, password)
    return render_template("login.html", name=name, password=password)


if __name__ == "__main__":
    app.run(debug=True)
