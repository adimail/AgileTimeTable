import subject
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/sem1_computer_theory', methods=['GET'])
def get_sem1_computer_theory():
    return jsonify(subject.sem1_computer_theory.to_dict(orient='records'))

@app.route('/api/sem1_non_computer_theory', methods=['GET'])
def get_sem1_non_computer_theory():
    return jsonify(subject.sem1_non_computer_theory.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
