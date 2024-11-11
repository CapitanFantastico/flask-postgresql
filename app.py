from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

# Modelos
class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add_factura():
    nueva_factura = Factura(total=100.0)
    db.session.add(nueva_factura)
    db.session.commit()
    return "Factura añadida"

if __name__ == '__main__':
    app.run(debug=True)
