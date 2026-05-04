from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

db_path = 'messenger.db'
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')
    c.execute('''CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        text TEXT,
        room TEXT,
        time TEXT
    )''')
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    conn = get_db()
    try:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                     (data['username'], data['password']))
        conn.commit()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (data['username'],)).fetchone()
        return jsonify({'id': user['id'], 'username': user['username']})
    except:
        return jsonify({'error': 'User exists'})
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                       (data['username'], data['password'])).fetchone()
    conn.close()
    if user:
        return jsonify({'id': user['id'], 'username': user['username']})
    return jsonify({'error': 'Wrong credentials'})

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)

@socketio.on('message')
def on_message(data):
    room = data['room']
    time = datetime.now().strftime('%H:%M')
    conn = get_db()
    conn.execute('INSERT INTO messages (user_id, text, room, time) VALUES (?, ?, ?, ?)',
                 (data['user_id'], data['text'], room, time))
    conn.commit()
    conn.close()
    emit('message', {'user': data['username'], 'text': data['text'], 'time': time}, room=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
