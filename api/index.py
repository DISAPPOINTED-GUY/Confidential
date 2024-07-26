from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/secrets', methods=['GET'])
def get_secrets():
    secrets = {
        "CONFIDENTIAL": os.getenv("CONFIDENTIAL"),
        "UTTV": os.getenv("UTTV"),
        "SECRET_KEY": os.getenv("SECRET_KEY")
    }
    return jsonify(secrets)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
