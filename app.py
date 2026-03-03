from flask import Flask
from routes import portfolio_bp

app = Flask(__name__)
app.register_blueprint(portfolio_bp)

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)