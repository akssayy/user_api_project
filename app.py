from flask import Flask, request, jsonify
from models import db, User

from routes import bp as routes_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(routes_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)