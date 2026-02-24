from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests
import os
import json

app = Flask(__name__)
CORS(app)

API = "https://infosoud.gov.cz/api/v1"

def proxy_response(data):
    return Response(
        json.dumps(data, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

@app.route("/organizace/lov")
def lov():
    r = requests.get(f"{API}/organizace/lov")
    return proxy_response(r.json())

@app.route("/organizace/podrizene/lov")
def podrizene():
    r = requests.get(f"{API}/organizace/podrizene/lov")
    return proxy_response(r.json())

@app.route("/organizace/lovkod/jednaci-sin")
def sins():
    id_org = request.args.get("idOrganizace", "")
    r = requests.get(f"{API}/organizace/lovkod/jednaci-sin?idOrganizace={id_org}")
    return proxy_response(r.json())

@app.route("/jednani/vyhledej", methods=["POST"])
def vyhledej():
    r = requests.post(f"{API}/jednani/vyhledej", json=request.get_json())
    return proxy_response(r.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
