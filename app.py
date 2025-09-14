from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# شمارنده درخواست‌ها برای مانیتورینگ
REQUEST_COUNT = Counter("request_count", "Total request count")

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route("/")
def hello():
    return "Hello DevOps!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)