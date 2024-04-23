from flask import Flask, render_template, request, abort, redirect  
import json

app = Flask(__name__)

# Carga los datos del archivo JSON
with open('/media/usuario/KIKO/PaginaPC/datos.json', 'r', encoding='utf-8') as json_file:
    datos = json.load(json_file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Contact', methods=['GET', 'POST'])
def Contact():
    # Obtener la marca seleccionada del formulario
    selected_brand = request.form.get('selected_brand', '')

    # Filtrar los productos según la marca seleccionada
    resultados = []
    if selected_brand:
        for producto in datos:
            if selected_brand.lower() in producto['marca'].lower():
                resultados.append(producto)
    else:
        resultados = datos

    # Obtener las marcas únicas para el select
    marcas_unicas = set(producto['marca'] for producto in datos)

    return render_template('contact.html', resultados=resultados, selected_brand=selected_brand, marcas_unicas=marcas_unicas)


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
