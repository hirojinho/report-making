from typing import Tuple
from flask import Blueprint, Response, jsonify, request

from app.routes.completion.services.completion import CompletionService

completion: Blueprint = Blueprint('completion', __name__)
completion_service = CompletionService("phi3")

@completion.route('/api/completion', methods = ['POST'])
def generate_completion() -> Tuple[Response, int]:
    input: str = request.form['user_input']

    # Validate input format
    if not isinstance(input, str):
        return jsonify({'error': 'Invalid data format'}), 400

    completion = completion_service.generate_completion(input)
    return jsonify(completion), 200