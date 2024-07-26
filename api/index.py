from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/api/secrets', methods=['GET'])
def get_secrets():
    response = requests.get("https://confidential.vercel.app/api/secrets")
    secrets = response.json()
    return jsonify(secrets)

@app.route('/api/run', methods=['POST'])
def run_tool():
    data = request.json
    api_id = data.get('api_id')
    api_hash = data.get('api_hash')
    secret_key = data.get('secret_key')
    # Your logic here
    return jsonify({"message": "Tool executed successfully!"})

if __name__ == '__main__':
    app.run()
