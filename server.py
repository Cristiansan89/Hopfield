from distutils.log import debug
from flask import Flask, render_template,request
#nuevos
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import json as js
import os

#importamos pandas para la transpuestas
import pandas as pd
# para la matriz identidad
import numpy as np

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
#nuevos
app.config["SQLALCHEMY_DATABASE_URI"] =dbdir
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
        # paso los datos de la peticion a json
        patron = request.json
        print(patron['imagen'],type(patron['imagen']))
        
        # para el vector 
        vector = {'E1': patron['imagen']}
        valorVector = pd.DataFrame(data = vector)
        print(valorVector)

        #para la transpuesta
        valorTranspuesta = valorVector.T
        print(valorTranspuesta)
        
        #resultado del patron
        resultPatron = valorTranspuesta.values * valorVector.values
        print(resultPatron)
    
        #matriz identidad
        matrizIdentidad = np.identity(25, dtype=int)
        print(matrizIdentidad)
    
        # resultado del aprendizaje del patrón
        valorAprendizaje = resultPatron - matrizIdentidad
        print(valorAprendizaje)
 
        
        # Guardando en la bases de datos
        imagenPatron = js.dumps(patron['imagen'])
        aprendizajePatron = js.dumps(valorAprendizaje.tolist())
        print(imagenPatron, type(imagenPatron))
        print(aprendizajePatron, type(aprendizajePatron))
        nuevaImagen = Imagen(patron=imagenPatron, aprendizaje=aprendizajePatron)
        db.session.add(nuevaImagen)
        db.session.commit()
        return js.dumps({"ok":1})

@app.route("/mostrar")
def mostrar():
    primera_imagen=Imagen.query.first()
    #filtrado primera_imagen=Imagen.query.filter_by(letra="a").first()
    deserialized = js.loads(primera_imagen.imagen)
    print(deserialized, type(deserialized))
    return render_template("code.html")
    
if __name__ == "__main__":
    db.create_all()

    # Ejecutor
    app.run(debug=True, port= 8080)


