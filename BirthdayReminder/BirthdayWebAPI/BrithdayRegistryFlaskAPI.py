from flask import Flask, request, jsonify
from BirthdayRegistry import BirthdayRegistry
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

data = BirthdayRegistry()

@app.route("/birthdays", methods=["GET"])
def get_items():
    return data.to_json()

@app.route("/birthdays", methods=["POST"])
def add_item():
    data.add_birthday(request.json["name"], request.json["month"], request.json["day"])
    return "OK"

@app.route("/birthdays/today", methods=["GET"])
def get_items_today():
    return jsonify(data.get_birthdays_today())

@app.route("/birthdays", methods=["DELETE"])
def delete_item():
    data.delete_birthday(request.json["name"])
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)