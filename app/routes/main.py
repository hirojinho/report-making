from flask import Blueprint, Response, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/ping', methods=['GET'])
def ping() -> Response:
    return jsonify('pong')

from app.routes.completion.completion import completion

main_bp.register_blueprint(completion)