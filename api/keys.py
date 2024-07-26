from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/keys')
def get_keys():
    keys = {
        "confidential": os.getenv("CONFIDENTIAL"),
        "tvscientist": os.getenv("UTTV"),
        "secret_key": os.getenv("SECRET_KEY"),
    }
    return jsonify(keys)

if __name__ == '__main__':
    app.run()
  
