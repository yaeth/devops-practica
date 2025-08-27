from flask import Flask

app = Flask(__name__)

@app.router("/")
def home():
    return "Hola, Mundo desde docker con Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
        
