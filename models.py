from sqlalchemy import Column, Integer, String, ForeignKey, Date,DateTime,Boolean,PickleType
from sqlalchemy.ext.mutable import MutableList
from server import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import json as js

class Imagen(db.Model):
    __tablename__ = 'imagen'
    id = Column(Integer, primary_key=True)
    patron = Column(String)
    letra = Column(String)
    def convertijson(self): 
        return js.loads(self.patron) 

class Aprendizaje(db.Model):    
    __tablename__ = 'aprendizaje'
    id = Column(Integer, primary_key=True)
    aprendizaje = Column(String)