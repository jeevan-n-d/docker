from flask import Flask, render_template_string, request, redirect
import mysql.connector

app = Flask(__name__)

# HTML Template (UI)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f4f4;
            text-align: center;
        }
        .container {
            background: white;
            padding: 20px;
            margin: 50px auto;
            width: 400px;
            border-radius: 10px;
            box-shadow: 0 0 10px gray;
        }
        input {
            padding: 10px;
            width: 80%;
            margin: 10px;
        }
        button {
            padding: 10px 20px;
            background: blue;
            color: white;
            border: none;
            cursor: pointer;
        }
        table {
            margin: 20px auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🚀 Flask + MySQL App</h2>

        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <br>
            <button type="submit">Add</button>
        </form>

        <h3>Stored Names:</h3>
        <table border="1">
            {% for row in data %}
            <tr><td>{{ row[1] }}</td></tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

# DB Connection
def get_db():
    return mysql.connector.connect(
        host="db",
        user="user1",
        password="user123",
        database="mydb"
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    db = get_db()
    cursor = db.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100)
        )
    """)

    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
        return redirect('/')

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    return render_template_string(HTML_PAGE, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
