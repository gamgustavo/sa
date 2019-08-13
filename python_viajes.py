from flask import Flask, redirect, url_for, request, jsonify
import json




class viaje(object):
    def __init__(self,  number, nombre_cliente, nombre_piloto, longitud_cliente, latitud_cliente, longitud_piloto, latitud_piloto, precio, estado):
        self.number = number
        self.nombre_cliente = nombre_cliente
        self.nombre_piloto = nombre_piloto
        self.longitud_cliente = longitud_cliente
        self.latitud_cliente = latitud_cliente
        self.longitud_piloto = longitud_piloto
        self.latitud_piloto = latitud_piloto
        self.precio = precio
        self.estado = estado



my_objects = []        
app = Flask(__name__)



@app.route('/crear_viaje', methods = ['POST'])
def crear_viaje():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        nombre_piloto = request.form['nombre_piloto']
        longitud_cliente = request.form['longitud_cliente']
        latitud_cliente = request.form['latitud_cliente']
        longitud_piloto = request.form['longitud_piloto']
        latitud_piloto = request.form['latitud_piloto']  
        precio = 50
        estado = 'atendido'
        my_objects.append( viaje( my_objects.count(),nombre_cliente, nombre_piloto, longitud_cliente,latitud_cliente,longitud_piloto,latitud_piloto,precio,estado))
        result = dict(nombre_cliente=nombre_cliente, nombre_piloto = nombre_piloto, longitud_cliente = longitud_cliente,latitud_cliente =latitud_cliente,longitud_piloto = longitud_piloto,latitud_piloto = latitud_piloto,precio = precio,estado =estado)
        return json.dumps(result)







if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5006)
