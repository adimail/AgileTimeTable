from flask import Flask, jsonify
import timetable

app = Flask(__name__)

@app.route('/api/dataframe')
def get_dataframe():
    your_dataframe = timetable.complete_timetable

    json_data = your_dataframe.to_json(orient='records')

    return jsonify(data=json_data)

if __name__ == '__main__':
    app.run(debug=True)
