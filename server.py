from distutils.log import debug
from flask import Flask, render_template, request
# nuevos
from flask_sqlalchemy import SQLAlchemy
import json as js
import os

# pandas para la transpuesta
import pandas as pd
# para la matriz identidad
import numpy as np

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
# nuevos
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
db = SQLAlchemy(app)

from models import *


@app.route("/")
def index():
    return render_template("code.html")


@app.route("/imagenes", methods=['POST', 'GET'])
def imagenes():
    if request.method == "GET":
        return render_template("code.html")
    if request.method == "POST":
        # paso los datos de la petición a json
        patron = request.json
        print(patron['imagen'], type(patron['imagen']))
        # para el vector
        vector = {'E1': patron['imagen']}
        val_vector = pd.DataFrame(data=vector)
        print(val_vector)
        # para la transpuesta
        valor_transpuesta = val_vector.T
        print(valor_transpuesta)
        # resultado del patron
        result_patron = valor_transpuesta.values * val_vector.values
        print(result_patron)
        # matriz identidad
        matriz_identidad = np.identity(25, dtype=int)
        print(matriz_identidad)
        # resultado del aprendizaje del patrón
        valor_aprendizaje = result_patron - matriz_identidad
        print(valor_aprendizaje)
        # Guardando en la base de dato
        imagen_patron = js.dumps(patron['imagen'])
        aprendizaje_patron = js.dumps(valor_aprendizaje.tolist())
        print(imagen_patron, type(imagen_patron))
        print(aprendizaje_patron, type(aprendizaje_patron))
        nueva_imagen = Imagen(patron=imagen_patron, aprendizaje=aprendizaje_patron)
        db.session.add(nueva_imagen)
        db.session.commit()
        return js.dumps({"ok": 1})


@app.route("/mostrar")
def mostrar():
    primera_imagen = Imagen.query.first()
    # filtrado primera_imagen=Imagen.query.filter_by(letra="a").first()
    deserialized = js.loads(primera_imagen.imagen)
    print(deserialized, type(deserialized))
    return render_template("code.html")

if __name__ == "__main__":
    db.create_all()
    # Ejecutor
    app.run(debug=True, port=8080)
