from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/sveiki")
def sveiki():
    return render_template("sveiki.html")

if __name__ == '__main__':
    app.run(port=5000)
