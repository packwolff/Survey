from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ------------------------
# DB Helper Function
# ------------------------
def get_db_connection():
    conn = sqlite3.connect('survey.db')
    conn.row_factory = sqlite3.Row
    return conn

# ------------------------
# Routes
# ------------------------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/survey')
def survey_page():
    return render_template('survey.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    name = request.form['name']
    department = request.form['department']
    facility = request.form['facility']
    rating = request.form['rating']
    comment = request.form['comment']

    conn = get_db_connection()
    conn.execute("INSERT INTO responses (name, department, facility, rating, comment) VALUES (?, ?, ?, ?, ?)",
                (name, department, facility, rating, comment))
    conn.commit()
    conn.close()

    return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    rows = conn.execute("SELECT department, facility, rating FROM responses").fetchall()
    conn.close()

    data = [dict(row) for row in rows]   # <-- FIX
    print("DATA SENT TO TEMPLATE:", data)
    return render_template('dashboard.html', data=data)


# Run app
if __name__ == '__main__':
    app.run(debug=True)
