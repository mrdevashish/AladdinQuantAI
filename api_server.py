from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/signal")
def signal():
    return jsonify({
        "symbol": "NIFTY",
        "signal": random.choice(["BUY","SELL","HOLD"])
    })

app.run(host="0.0.0.0", port=5000)
