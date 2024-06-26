from app.database import get_db

class Mascota:

    #constructor
    def __init__(self,id_mascota=None,nombre=None,tipo=None,sexo=None,tamanio=None,edad=None,descripcion=None,url_foto=None):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.tipo = tipo
        self.sexo = sexo
        self.tamanio = tamanio
        self.edad = edad
        self.descripcion = descripcion
        self.url_foto = url_foto

    def serialize(self):
        return {
            'id_mascota':self.id_mascota,
            'nombre':self.nombre, 
            'tipo':self.tipo, 
            'sexo':self.sexo,
            'tamanio':self.tamanio,
            'edad':self.edad,
            'descripcion':self.descripcion,
            'url_foto':self.url_foto,
        }
    
    @staticmethod
    def get_all():
        #lógica para buscar en la bd todas las mascotas
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM mascotas"
        cursor.execute(query)
        #obtengo resultados
        rows = cursor.fetchall()
        mascotas = [Mascota(id_mascota=row[0], nombre=row[1], tipo=row[2], sexo=row[3], tamanio=row[4], edad=row[5], descripcion=row[6], url_foto=row[7]) for row in rows]
        #cerramos el cursor
        cursor.close()
        return mascotas
    
    @staticmethod
    def get_mascota(mascota_id):
        #lógica para buscar en la bd una mascota en particular
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM mascotas WHERE id_mascota = %s", (mascota_id,))
        #obtengo resultado
        row = cursor.fetchone()
        #cerramos el cursor
        cursor.close()
        #si encuentro registro lo devuelvo sino retorno None
        if row:
            return Mascota(id_mascota=row[0], nombre=row[1], tipo=row[2], sexo=row[3], tamanio=row[4], edad=row[5], descripcion=row[6], url_foto=row[7])
        return None
    
    def save_mascota(self):
        #lógica para ctualizar o crear en la bd una mascota
        db = get_db()
        cursor = db.cursor()
        if self.id_mascota:
            cursor.execute("""
                UPDATE mascotas SET nombre = %s, tipo = %s, sexo = %s, tamanio = %s, edad = %s, descripcion = %s, url_foto = %s
                WHERE id_mascota = %s
            """, (self.nombre, self.tipo, self.sexo, self.tamanio, self.edad, self.descripcion, self.url_foto, self.id_mascota))
        else: 
            cursor.execute("""
                INSERT INTO mascotas (nombre, tipo, sexo, tamanio, edad, descripcion, url_foto) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (self.nombre, self.tipo, self.sexo, self.tamanio, self.edad, self.descripcion, self.url_foto))
            #obtengo el último id generado
            self.id_mascota = cursor.lastrowid
        #salvamos los cambios en la bd
        db.commit()
        #cerramos el cursor
        cursor.close()
        return
    
    def delete_mascota(self):
        #lógica para eliminar de la bd una mascota
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""DELETE FROM mascotas WHERE id_mascota = %s""", (self.id_mascota,))
        #salvamos los cambios en la bd
        db.commit()
        #cerramos el cursor
        cursor.close()
        return
    



