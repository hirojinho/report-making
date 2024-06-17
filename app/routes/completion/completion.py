from typing import Any, Dict, Tuple
from flask import Blueprint, Response, jsonify, request

from app.routes.completion.services.completion import CompletionService

completion: Blueprint = Blueprint('completion', __name__)
completion_service = CompletionService("phi3")

@completion.route('/api/completion', methods = ['POST'])
def generate_completion() -> Tuple[Response, int]:
    input_data: Dict[str, str] = request.json if request.json else {}

    # Validate input format
    if not isinstance(input_data, dict) or 'input' not in input_data or not isinstance(input_data['input'], str):
        return jsonify({'error': 'Invalid data format'}), 400
    
    # Process input data
    input_value = input_data['input']
    completion = f'Processed input: {input_value}'
    return jsonify(completion), 200