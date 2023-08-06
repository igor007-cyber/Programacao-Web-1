from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
app.config['SESSION_TYPE'] = 'arquivos'
Session(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, password))
        conn.commit()
        conn.close()
        flash('Usuário criado com sucesso!')
        return redirect(url_for('sair   '))
    return render_template('register.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password =?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = user[1]
            flash('Login realizado com sucesso!')
        else:
            flash('Usuário ou senha incorretos.')
        return redirect(url_for('sair'))
    return render_template('login.html')

 
@app.route('/sair')
def logout():
    session.pop('username', None)
    return redirect(url_for('sair'))

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
    init_db()