from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
password = os.getenv("password")

db_params = {
    'dbname': 'ttdb',
    'user': 'adimail',
    'password': password,
    'host': 'localhost'
}

def execute_query(query, params=(), fetch=False):
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute(query, params)
    
    if fetch:
        result = cursor.fetchall()
    else:
        result = None
    
    connection.commit()
    connection.close()
    
    return result

@app.route('/', methods=['GET', 'POST'])
def manage_subjects():
    if request.method == 'POST':
        name = request.form['name']
        abbreviation = request.form['abbreviation']
        theory_hours = request.form['theory_hours']
        semester = request.form['semester']
        practical_hours = request.form['practical_hours']
        
        execute_query("INSERT INTO subjects (name, abbreviation, theory_hours, semester, practical_hours) VALUES (%s, %s, %s, %s, %s)",
                      (name, abbreviation, theory_hours, semester, practical_hours))
        
        return redirect(url_for('manage_subjects'))

    subjects = execute_query("SELECT * FROM subjects", fetch=True)
    
    if not subjects:
        subjects = []
    
    return render_template('manage_subjects.html', subjects=subjects)

@app.route('/edit_subject/<int:id>', methods=['GET', 'POST'])
def edit_subject(id):
    if request.method == 'POST':
        name = request.form['name']
        abbreviation = request.form['abbreviation']
        theory_hours = request.form['theory_hours']
        execute_query("UPDATE subjects SET name=%s, abbreviation=%s, theory_hours=%s WHERE id=%s", (name, abbreviation, theory_hours, id))
        return redirect(url_for('manage_subjects'))
    
    subject_result = execute_query("SELECT * FROM subjects WHERE id=%s", (id,), fetch=True)
    
    if subject_result and len(subject_result) > 0:
        subject = subject_result[0]
    else:
        return "Subject not found."
    
    return render_template('edit_subject.html', subject=subject)

@app.route('/delete_subject/<int:id>', methods=['POST'])
def delete_subject(id):
    execute_query("DELETE FROM subjects WHERE id=%s", (id,))
    return redirect(url_for('manage_subjects'))

if __name__ == '__main__':
    app.run(debug=True)
