from flask import Flask, jsonify
from flask_cors import CORS
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.api.routes import register, login, pwchange, post
from src.database.db import init_app, db


app = Flask(__name__)
CORS(app)

app = init_app(app)

app.register_blueprint(register.bp, url_prefix="/api")
app.register_blueprint(login.bp, url_prefix="/api")
app.register_blueprint(pwchange.bp, url_prefix="/api")
app.register_blueprint(post.bp, url_prefix="/api")

@app.route("/")
def app_root():
    return jsonify({"message": "info info"})

if __name__ == "__main__":
    app.run(debug=True)



# =================== KE BAWAH DEBUG GAPENTING ================================

# import os
# import psycopg2

# def test_connection():
#     database_url = os.getenv("DATABASE_URL")
#     print(f"Testing connection url: {database_url}")
    
#     try:
#         conn = psycopg2.connect(database_url)
#         print("Koneksi DB Berhasil!")
#         conn.close()
#     except Exception as e:
#         print(f"DB Connection gagal: {e}")

# test_connection()



# def test_connectivity():
#     host = "ep-aged-shadow-a1okb9nq.ap-southeast-1.aws.neon.tech"
#     port = 5432
    
#     try:
#         start = time.time()
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(10)
#         result = sock.connect_ex((host, port))
#         sock.close()
        
#         if result == 0:
#             print("✅ Port 5432 is reachable")
#         else:
#             print(f"❌ Port 5432 blocked (error code: {result})")
            
#     except Exception as e:
#         print(f"❌ Socket error: {e}")

# test_connectivity()


