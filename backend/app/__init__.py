from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///taskdb.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    jwt = JWTManager(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Import and register blueprints
    from routes.auth import auth_bp
    from routes.tasks import tasks_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(tasks_bp, url_prefix='/api')
    
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({'status': 'healthy', 'message': 'Task Manager API is running'}), 200
    
    return app
