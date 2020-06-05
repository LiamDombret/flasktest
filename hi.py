from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("test.html", content="Hello World!")

@app.route("/name<name>")
def name(name):
    return f"Hello, {name}"

@app.route("/count<count>")
def count(count):
    return render_template("count.html", value=int(count))

if __name__ == "__main__":
    app.run()
