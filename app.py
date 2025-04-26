from flask import Flask, Response, jsonify, render_template
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello"

@app.route("/get_dog_breeds", methods=['GET'])
def get_dog_breeds():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    json_res = json.loads(response.text)
    breeds = json_res["message"]
    return render_template("/dashboard.html", breeds=breeds)

if __name__ == '__main__':
    app.run()

