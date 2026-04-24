from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Mi negocio</h1><p>Ya está online</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
