from flask import Flask, render_template, request, abort, redirect  
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Contact', methods=['GET', 'POST'])
def Contact():
    with open('datos.json', 'r', encoding='utf-8') as fich:
        datos = json.load(fich)

    search_term = request.form.get('search_term', '')
    selected_brand = request.form.get('selected_brand', '')
    resultados = []
    if search_term and selected_brand:
        for producto in datos:
            if search_term.lower() in producto['titulo'].lower() and selected_brand.lower() in producto['marca'].lower():
                resultados.append(producto)
    elif search_term:
        for producto in datos:
            if search_term.lower() in producto['titulo'].lower():
                resultados.append(producto)
    elif selected_brand:
        for producto in datos:
            if selected_brand.lower() in producto['marca'].lower():
                resultados.append(producto)
    else:
        resultados = datos
    marcas_unicas = set(producto['marca'] for producto in datos)

    return render_template('contact.html', resultados=resultados, search_term=search_term, selected_brand=selected_brand, marcas_unicas=marcas_unicas)

@app.route('/producto/<int:id>')
def mostrar_producto(id):
    with open('datos.json', 'r', encoding='utf-8') as fich:
        datos = json.load(fich)

    producto_encontrado = None
    for producto in datos:
        if producto['id'] == id:
            producto_encontrado = producto
            break
    if producto_encontrado:
        return render_template('producto.html', producto=producto_encontrado)
    else:
        return render_template('error.html', message='Producto no encontrado'), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port, debug=True)
