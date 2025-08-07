from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
return "Hello from EC2 update version32 with Docker and GitHub Actions! this is for production"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

