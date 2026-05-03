from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/hamburguesas')
def hamburguesas():
    menu = [
        {
            "nombre": "Hamburguesa Clásica",
            "precio": 2500,
            "descripcion": "Carne, lechuga, tomate y queso",
            "imagen": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
        },
        {
            "nombre": "Hamburguesa Doble",
            "precio": 3500,
            "descripcion": "Doble carne, queso, papas y salsa especial",
            "imagen": "https://images.unsplash.com/photo-1550547660-d9450f859349"
        },
        {
            "nombre": "Hamburguesa Especial",
            "precio": 4000,
            "descripcion": "Carne, bacon, queso, huevo y salsas",
            "imagen": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"
        }
    ]
    return render_template('hamburguesas.html', menu=menu)

@app.route('/platanos')
def platanos():
    menu = [
        {
            "nombre": "Plátanos con queso",
            "precio": 2000,
            "descripcion": "Plátanos maduros con queso",
            "imagen": "https://i.blogs.es/4221eb/platano-relleno-hondureno-1/840_560.jpg"
        },
        {
            "nombre": "Plátanos con natilla",
            "precio": 2200,
            "descripcion": "Con natilla casera",
            "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgtwfCqd3jGipVG4gx_ZEMGirTqiqsaXkOTg&s"
        }
    ]
    return render_template('platanos.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))