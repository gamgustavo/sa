from flask import Flask, redirect, url_for, request, jsonify
import requests
import json


class posiciones(object):
    def __init__(self,  number, tipo, longitud, latitud):
        self.number = number
        self.tipo = tipo
        self.longitud = longitud
        self.latitud = latitud



my_objects = []        
app = Flask(__name__)


def get_posicion_detalle(number,tipo):
    for obj in my_objects:
        if obj.number == number and obj.tipo == tipo:
            person = dict(logitud=obj.longitud, latitud=obj.latitud)
            return json.dumps(person)
    person = person = dict(logitud=0, latitud=0)
    return json.dumps(person)


@app.route('/get_posicion', methods = ['POST'])
#"""Metodo Post para la obtencion de posiciones
#
#    Parámetros:
#    number -- number
#    tipo -- tipo
#    apellido -- apellido
#
#    Return:
#    Devuelve la posicion de persona o conductor
#    
#   """
def get_posicion():
    if request.method == 'POST':
        number = request.form['number']
        tipo = request.form['tipo']
        resultado = get_posicion_detalle(number,tipo)
        return resultado


@app.route('/create_posicion', methods = ['POST'])
#"""Metodo Post para la creacion de Posiciones
#
#    Parámetros:
#    number -- number
#    tipo -- tipo
#    apellido -- apellido
#
#    Return:
#    Devuelve la posicion de persona o conductor
#    
#   """
def create_posicion():
    if request.method == 'POST':
        number = request.form['number']
        tipo = request.form['tipo']
        longitud = request.form['longitud']
        latitud = request.form['latitud']
        my_objects.append(posiciones( number, tipo, longitud, latitud))
        result = dict(number=number, tipo=tipo,longitud = longitud,latitud = latitud)
        return json.dumps(result)


@app.route('/update_posicion', methods = ['POST'])
#"""Metodo Post para la actualizacion de posicione
#
#    Parámetros:
#    number -- number
#    tipo -- tipo
#
#    Return:
#    Devuelve la posicion de persona o conductor
#    
#   """
def update_posicion():
    if request.method == 'POST':
        number = request.form['number']
        tipo = request.form['tipo']
        longitud = request.form['longitud']
        latitud = request.form['latitud']

        for obj in my_objects:
            if obj.number == number and obj.tipo == tipo:
                obj.longitud = longitud
                obj.latitud = latitud
                person = dict(logitud=obj.logitud, latitud=obj.latitud)
                return json.dumps(person)
        person = person = dict(logitud=0, latitud=0)
        return json.dumps(person)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004)
