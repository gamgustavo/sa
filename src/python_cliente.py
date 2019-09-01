from flask import Flask, redirect, url_for, request, jsonify
import json




class cliente(object):
    def __init__(self,  number, nombre, apellido):
        self.number = number
        self.nombre = nombre
        self.apellido = apellido


my_objects = []        
app = Flask(__name__)




@app.route('/crear_cliente', methods = ['POST'])
#"""Metodo Post para la creacion de Cliente
#
#    Parámetros:
#    number -- number
#    nombre -- nombre
#    apellido -- apellido
#    logitud -- logitud
#    latitud -- latitud
#
#    Return:
#    Devuelve el objeto creado
#    
#"""
def crear_cliente():
    if request.method == 'POST':
        number = request.form['number']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        my_objects.append( cliente( number, nombre, apellido))
        result = dict(number=number, nombre=nombre,apellido = apellido)
        return json.dumps(result)


@app.route('/get_cliente', methods = ['POST'])
def get_cliente():
    nombre = request.form['nombre']
    for obj in my_objects:
        if obj.nombre == nombre:
            person = dict(number=obj.number, nombre=obj.nombre, apellido = obj.apellido )
            return json.dumps(person)
    person  = dict(number=0, nombre=0, apellido = 0 )
    return json.dumps(person)






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
