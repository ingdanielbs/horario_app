from flask import Flask, render_template, request
import pandas as pd
import json

from horario import competenciasInstructor, horario, horario_fichas, instructores, fichas

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    listado_instructores = instructores()
    if request.method == "POST":
        documento = request.form["documento"]
        horarioInstructor = horario(documento)
        competencias = competenciasInstructor(documento)        
        return render_template("index.html", horarioInstructor=horarioInstructor, listado_instructores=listado_instructores, competencias=competencias)
    return render_template("index.html", listado_instructores=listado_instructores)

@app.route("/hficha", methods=["GET", "POST"])
def horario_ficha():
    listado_fichas = fichas()
    if request.method == "POST":
        ficha = request.form["ficha"]
        horario_f = horario_fichas(ficha)
        return render_template("horario_ficha.html", horario_f=horario_f, listado_fichas=listado_fichas)    
    return render_template("horario_ficha.html", listado_fichas=listado_fichas)

@app.route("/api/h_instructor", methods=["GET", "POST"])
def api_h_instructores():
    horarioInstructor = horario('DANIEL DAVID BENAVIDES SÁNCHEZ ')
    horario_dict = horarioInstructor.copy()
    horario_dict['horario'] = [(k, v) for k, v in horario_dict['horario'].items()]
    horario_json = json.dumps(horario_dict, default=lambda x: x.tolist() if isinstance(x, pd.Series) else x)
    """ horario_dict = json.loads(horario_json) """
    return horario_json

if __name__ == "__main__":
    app.run(debug=True)
    