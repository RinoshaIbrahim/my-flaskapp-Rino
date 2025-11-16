from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'yourdb'
mysql = MySQL(app)

@app.route('/add', methods=['POST'])
def add():
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO tablename (field1, field2) VALUES (%s, %s)', (value1, value2))
    mysql.connection.commit()
    cursor.close()
    return 'Inserted!'