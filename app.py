import time
from flask import Flask, jsonify

app = Flask(__name__)

# Mock system startup time
START_TIME = time.time()

@app.get("/status")
def get_status():
    uptime_seconds = int(time.time() - START_TIME)
    return jsonify({
        "status": "Healthy",
        "service_name": "Atos-Candidate-Gateway",
        "uptime": f"{uptime_seconds} seconds",
        "region": "Istanbul-Goztepe",
        "version": "1.0.0"
    })

@app.get("/")
def home():
    return "System Status API is running. Access /status for details."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
