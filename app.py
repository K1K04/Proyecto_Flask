from flask import Flask, render_template, request, abort, redirect  
import json

app = Flask(__name__)

# Carga los datos del archivo JSON
with open('/media/usuario/KIKO/PaginaPC/datos.json', 'r', encoding='utf-8') as json_file:
    datos = json.load(json_file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Computer')
def Computer():
    return render_template("Computer.html")

@app.route('/Rams')
def Rams():
    return render_template("Rams.html")

@app.route('/Products')
def Products():
    return render_template("products.html")

@app.route('/About')
def About():
    return render_template("about.html")

@app.route('/Contact')
def Contact():
    return render_template("contact.html")

@app.route('/listaorype', methods=['POST'])
def lista_orype():
    # Obtener la cadena de búsqueda del formulario
    search_term = request.form.get('search_term', '')

    # Filtrar los productos según la cadena de búsqueda
    resultados = []
    if search_term:
        for producto in datos:
            if producto['titulo'].startswith(search_term):
                resultados.append(producto)
    else:
        resultados = datos

    return render_template('listaorype.html', resultados=resultados, search_term=search_term)

@app.route('/producto/<int:id>')
def mostrar_producto(id):
    # Buscar el producto con el id dado en tus datos
    producto_encontrado = None
    for producto in datos:
        if producto['id'] == id:
            producto_encontrado = producto
            break

    # Verificar si se encontró el producto
    if producto_encontrado:
        return render_template('producto.html', producto=producto_encontrado)
    else:
        # Si el producto no se encuentra, puedes renderizar una plantilla de error o redirigir a otra página.
        return render_template('error.html', message='Producto no encontrado'), 404



if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)

