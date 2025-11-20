from flask import Flask, jsonify
from flask_cors import CORS
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.api.routes import register, login
from src.database.db import init_app, db


app = Flask(__name__)
CORS(app)

app = init_app(app)

app.register_blueprint(register.bp, url_prefix="/api")
app.register_blueprint(login.bp, url_prefix="/api")

@app.route("/")
def app_root():
    return jsonify({"message": "info info"})

if __name__ == "__main__":
    app.run(debug=True)