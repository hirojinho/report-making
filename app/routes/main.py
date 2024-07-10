from flask import Blueprint, Response, jsonify, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/ping', methods=['GET'])
def ping() -> Response:
    return jsonify('pong')

@main_bp.route('/', methods=['GET', 'POST'])
def index() -> Response | str:
    if request.method == 'POST':
        user_input: str = request.form['user_input']
        # Process user_input as needed
        return jsonify({'message': f'User input received: {user_input}'})

    # If GET request or initial load, render the form
    return render_template('index.html')

from app.routes.completion.completion import completion

main_bp.register_blueprint(completion)