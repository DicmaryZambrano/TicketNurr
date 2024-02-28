from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conneccion a a base de datos
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "crud_flask"
mysql = MySQL(app)

# Sesion
app.secret_key = "mysecretkey"


@app.route("/")
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contactos")
    datos = cursor.fetchall()
    return render_template("index.html", contactos=datos)


@app.route("/add_contact", methods=["POST"])
def add_contact():
    if request.method == "POST":
        nombre_completo = request.form["nombre_completo"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO contactos (nombre_completo, telefono, email) VALUES (%s, %s, %s)",
            (
                nombre_completo,
                telefono,
                email,
            ),
        )
        mysql.connection.commit()
        flash("Contacto agregado satisfactoriamente")
        return redirect(url_for("Index"))


@app.route("/edit/<id>")
def get_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contactos WHERE id = %s", (id))
    data = cursor.fetchall()
    contacto = data[0]
    return render_template("edit-contact.html", contacto=contacto)


@app.route("/update/<id>", methods=["POST"])
def update_contact(id):
    if request.method == "POST":
        nombre_completo = request.form["nombre_completo"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE contactos
            SET nombre_completo = %s,
                telefono = %s,
                email = %s
            WHERE id = %s
            """,
            (nombre_completo, telefono, email, id),
        )
        mysql.connection.commit()
        flash("Contacto actualizado satisfactoriamente")
        return redirect(url_for("Index"))


@app.route("/delete/<string:id>")
def delete_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM contactos WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash("Contacto eliminado satisfactoriamente")
    return redirect(url_for("Index"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
