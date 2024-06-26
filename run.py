from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#Inicializar app Flask
app = Flask(__name__)

init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)

#Registrar ruta asociada a una vista (ruta > función)
app.route('/api/mascotas/',methods=['GET'])(get_all_mascotas)
app.route('/api/mascotas/<int:mascota_id>',methods=['GET'])(get_mascota)
app.route('/api/mascotas/',methods=['POST'])(create_mascota)
app.route('/api/mascotas/<int:mascota_id>',methods=['PUT'])(update_mascota)
app.route('/api/mascotas/<int:mascota_id>',methods=['DELETE'])(delete_mascota)

#Se asegura de que todo se ejecute dentro del if
if __name__ == '__main__':
    #levanta el servidor de desarrollo de Flask
    app.run(debug=True)