import sqlite3

from flask import Flask, render_template

app= Flask(__name__)
app.config["SECRET_KEY"]= 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    print("Test")
    return conn

app  = Flask(__name__) 

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

app.run(host="localhost", debug=True)