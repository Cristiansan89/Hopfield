from sqlalchemy import Column, Integer, String, ForeignKey, Date,DateTime,Boolean,PickleType
from sqlalchemy.ext.mutable import MutableList
from server import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
class Imagen(db.Model):
    __tablename__ = 'imagen'
    id = Column(Integer, primary_key=True)
    patron = Column(String)
    aprendizaje = Column(String)