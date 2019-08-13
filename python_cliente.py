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
def crear_cliente():
    if request.method == 'POST':
        number = request.form['number']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        my_objects.append( cliente( number, nombre, apellido))
        result = dict(number=number, nombre=nombre,apellido = apellido)
        return json.dumps(result)







if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
