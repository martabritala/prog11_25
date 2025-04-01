from flask import Flask, render_template, redirect, request
from data import uztaisit_vienu_spamu, pievienot_datus, iegut_datus, iegut_vardu

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

@app.route("/spams")
def spams():
    dati = iegut_datus()
    # print(dati)
    return render_template("spams.html", dati = dati)

@app.route("/veidot_spamu", methods=["POST"])
def veidot():
    name = request.form["vards"]
    sex = request.form["dzimums"]
    age = request.form["vecums"]
    # uztaisit_vienu_spamu(name, age, sex)
    pievienot_datus(name, age, sex)
    return redirect("/spams")

@app.route("/karatavas")
def karatavas():
    vards = iegut_vardu()
    return render_template("karatavas.html", vards=vards)




if __name__ == '__main__':
    app.run(port=5000)
