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
from sqlalchemy import null

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
        aprendizaje = request.json
        # para el vector
        vector = {'E1': patron['imagen']}
        val_vector = pd.DataFrame(data=vector)
        # para la transpuesta
        valor_transpuesta = val_vector.T
        # resultado del patron
        result_patron = valor_transpuesta.values * val_vector.values
        # matriz identidad
        matriz_identidad = np.identity(25, dtype=int)
        # resultado del aprendizaje del patrón
        matriz_aprendizaje = result_patron - matriz_identidad
        
        if == null

        else

        
        # Guardando en la base de dato
        imagen_patron = js.dumps(patron['imagen'])
        nueva_letra = patron['letra']
        nueva_imagen = Imagen(patron=imagen_patron, letra=nueva_letra)
        
        aprendizaje_patron = js.dumps(matriz_aprendizaje.tolist())
        nuevo_aprendizaje = Aprendizaje(aprendizaje=aprendizaje_patron)

        db.session.add(nueva_imagen, nuevo_aprendizaje)
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
