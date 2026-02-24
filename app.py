from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API = "https://infosoud.gov.cz/api/v1"

@app.route("/organizace/lov")
def lov():
    r = requests.get(f"{API}/organizace/lov")
    return jsonify(r.json())

@app.route("/organizace/podrizene/lov")
def podrizene():
    r = requests.get(f"{API}/organizace/podrizene/lov")
    return jsonify(r.json())

@app.route("/organizace/lovkod/jednaci-sin")
def sins():
    id_org = request.args.get("idOrganizace", "")
    r = requests.get(f"{API}/organizace/lovkod/jednaci-sin?idOrganizace={id_org}")
    return jsonify(r.json())

@app.route("/jednani/vyhledej", methods=["POST"])
def vyhledej():
    r = requests.post(f"{API}/jednani/vyhledej", json=request.get_json())
    return jsonify(r.json())

if __name__ == "__main__":
    app.run()
