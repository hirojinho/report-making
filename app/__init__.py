from flask import Flask

app = Flask(__name__)

# Import and register routes
from app.routes.main import main_bp

app.register_blueprint(main_bp)
