from flask import Flask, redirect, url_for, request, jsonify
import json



class Conductor(object):
    def __init__(self,  number, nombre, apellido, automotor):
        self.number = number
        self.nombre = nombre
        self.apellido = apellido
        self.automotor = automotor


my_objects = []        
app = Flask(__name__)




@app.route('/crear_conductor', methods = ['POST'])
#"""Metodo Post para la creacion de conductores
#
#    Parámetros:
#    number -- number
#    nombre -- nombre
#    apellido -- apellido
#    automotor -- automotor   
#    logitud -- logitud
#    latitud -- latitud
#
#    Return:
#    Devuelve el objeto creado
#    
#   """
def crear_conductor():
    if request.method == 'POST':
        number = request.form['number']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        automotor = request.form['automotor']
        my_objects.append(Conductor( number, nombre, apellido, automotor))
        result = dict(number=number, nombre=nombre,apellido = apellido,automotor = automotor)
        return json.dumps(result)


@app.route('/get_conductor', methods = ['POST'])
def get_conductor():
    for obj in my_objects:
        person = dict(number=obj.number, nombre=obj.nombre, apellido = obj.apellido, automotor = obj.automotor)
        return json.dumps(person)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)



