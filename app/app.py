from flask import Flask, render_template, jsonify
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "index.html",
        title="Welcome to my Webpage",
        version="1.0.0"
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "app_name": "CICD Project",
        "version": "1.0.0",
        "description": "This is a sample CICD project for development and containerization web applications."
    })

if __name__ == '__main__':
    ##host ='0.0.0.0' is important for docker container to be accessible from outside the container
    port= int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)