from flask import Flask, render_template, request, redirect, url_for
from database import get_db

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE username = ?", (user,))
        datos = cursor.fetchone()

        conn.close()

        if datos and datos["password"] == passwd:

            if datos["rol"] == "admin":
                # Cambiar esta ruta cuando tengas tu página real
                return redirect(url_for('admin_bienvenida'))
            else:
                # Cambiar esta ruta cuando tengas tu página real
                return redirect(url_for('usuario_bienvenida'))

        return "Usuario o contraseña incorrectos"

    return render_template('login.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        rol = request.form['rol']   # admin o usuario

        conn = get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)",
                (user, passwd, rol)
            )
            conn.commit()
            mensaje = "Registro exitoso "
            
            
        except:
            mensaje = "El usuario ya existe"

        conn.close()
        return mensaje

    return render_template('registro.html')


@app.route('/admin')
def admin_bienvenida():
    return render_template('admin.html')


@app.route('/usuario')
def usuario_bienvenida():
    return render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True)
