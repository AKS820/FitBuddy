import sqlite3
from flask import Flask, render_template,  request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def hello():
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts').fetchone()
    post2 = conn.execute('SELECT * FROM posts').fetchone()
    conn.close()
    return render_template("index.html" ,posts = [post,post2])
