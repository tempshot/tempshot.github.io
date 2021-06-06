from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'data_base'

mysql = MySQL(app)

@app.route('/', methods = ['Get', 'POST'])
def registration():
    if request.method == 'POST':

        detail = request.form
        f_name = detail['f_name']
        l_name = detail['l_name']
        mail = detail['mail']
        dob = detail['dob']
        phone = detail['phone']
        address_ = detail['address_']
        course = detail['course']
        startingFrom = detail['startingFrom']
        timeSlot = detail['timeSlot']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO form(f_name, l_name, mail, dob, phone, address_, course, startingFrom, timeSlot) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(f_name, l_name, mail, dob, phone, address_, course, startingFrom, timeSlot))
        mysql.connection.commit()
        cur.close()
        return redirect('/registered')
    return render_template('index.html')

@app.route('/registered')
def registeres():
    cur = mysql.connection.cursor()
    res = cur.execute("SELECT * FROM form WHERE id=(SELECT max(id) FROM form);")
    if res>0:
        id_no = cur.fetchall()
        return render_template('registered.html',id_no=id_no)

app.run(debug=True)
    


