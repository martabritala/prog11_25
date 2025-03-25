from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/sveiki")
def sveiki():
    vardi = ["Marta", "Anna", "Katrina"]
    return render_template("sveiki.html", name=vardi, last="")

@app.route("/sveiki/<vards1>/<uzvards1>")
def sveiki_cits(vards1, uzvards1):
    vards = [vards1]
    uzvards = uzvards1
    return render_template("sveiki.html", name=vards, last=uzvards)


if __name__ == '__main__':
    app.run(port=5000)
