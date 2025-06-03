from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    users = cursor.fetchall()
    conn.close()
    return [{"id": user[0], "name": user[1]} for user in users]

@app.route("/users", methods=["GET"])
def users():
    return jsonify(get_users())

if __name__ == "__main__":
    app.run(debug=True)
