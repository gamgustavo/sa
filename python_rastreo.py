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
            person = dict(logitud=obj.logitud, latitud=obj.latitud)
            return person
        else:
            person = person = dict(logitud=0, latitud=0)
            return person


@app.route('/get_posicion', methods = ['POST'])
def get_posicion():
    if request.method == 'POST':
        number = request.form['number']
        tipo = request.form['tipo']
        resultado = get_posicion_detalle(number,tipo)
        result = dict(number=number, logitud=resultado['logitud'],latitud = resultado['latitud'])
        return json.dumps(result)


@app.route('/create_posicion', methods = ['POST'])
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
                return person
        person = person = dict(logitud=0, latitud=0)
        return person



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004)
