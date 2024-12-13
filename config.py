import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:edson@localhost:3306/noticia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
