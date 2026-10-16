from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', titulo='Inicio', mensaje='Bienvenido a mi website de UDL-ICO!')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Bienvenido a la página de servicios de UDL-ICO!')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto', mensaje='Bienvenido a la página de contacto de UDL-ICO!')

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo='Productos', mensaje='Bienvenido a la página de productos de UDL-ICO!')

if __name__ == '__main__':
    app.run(debug=True,port=5051)