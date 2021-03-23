from flask import Flask, render_template, request
from process import Person

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def result():
    r = request.form
    if int(r["poids"]) > 200:
        error = "poids"
        return render_template("home.html", error=error)
    elif int(r["taille"]) > 300:
        error = "taille"
        return render_template("home.html", error=error)
    elif int(r["age"]) > 150:
        error = "age"
        return render_template("home.html", error=error)

    p = Person(r["sex"], r["poids"], r["taille"], r["age"], r["ta"], r["objectif"], r["morpho"], r["actif"])

    tmb = p.calculTMB()
    ta = "%.0f" % p.calculTA(tmb)
    maccro = p.macro(ta, r["objectif"])
    
    return render_template("result.html", calorie=ta, maccro=maccro, objectif=r["objectif"])