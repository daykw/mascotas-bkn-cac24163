from flask import jsonify, request
from app.models import Mascota

def index():
    response = {'message':'Bienvenido a Tu Mejor Amigo'}
    return jsonify(response)

def get_all_mascotas():
    resultado_mascotas = Mascota.get_all()
    return jsonify([mascota.serialize() for mascota in resultado_mascotas])

def get_mascota(mascota_id):
    mascota = Mascota.get_mascota(mascota_id)
    if not mascota:
        return jsonify({'message':'La mascota no fue encontrada'}), 404
    return jsonify([mascota.serialize()])

def create_mascota():
    #obtengo los datos enviados en formato json desde el form del front end y los convierto en un diccionario
    data = request.json
    #valido los datos que lo requieran
    if (data['nombre']==''):
        return jsonify({'message':'El campo nombre es obligatorio'}), 400
    if (data['tipo']==''):
        return jsonify({'message':'El campo tipo es obligatorio'}), 400
    mascota = Mascota(None,data['nombre'],data['tipo'],data['sexo'],data['tamanio'],data['edad'],data['descripcion'],data['url_foto'])
    #creo la mascota
    mascota.save_mascota()
    response = {'message':'La mascota fue creada con éxito','data':data, 'id':new_mascota.id_mascota}
    return jsonify(response) , 201

def update_mascota(mascota_id):
    mascota = Mascota.get_mascota(mascota_id)
    if not mascota:
        response = {'message':'La mascota no fue encontrada', 'id':mascota_id}
        return jsonify(response) , 404
    #obtengo los datos enviados en formato json desde el form del front end y los convierto en un diccionario
    data = request.json
    #actualizo la mascota
    mascota.nombre = data['nombre']
    mascota.tipo = data['tipo']
    mascota.sexo = data['sexo']
    mascota.tamanio = data['tamanio']
    mascota.edad = data['edad']
    mascota.descripcion = data['descripcion']
    mascota.url_foto = data['url_foto']
    mascota.save_mascota()
    response = {'message':'La mascota fue actualizada con éxito', 'data':data, 'id':mascota_id}
    return jsonify(response) , 201

def delete_mascota(mascota_id):
    mascota = Mascota.get_mascota(mascota_id)
    if not mascota:
        response = {'message':'La mascota no fue encontrada', 'id':mascota_id}
        return jsonify(response) , 404
    mascota.delete_mascota()
    response = {'message':'La mascota fue eliminada con éxito', 'id':mascota_id}
    return jsonify(response) , 200


    
