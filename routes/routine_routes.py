from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.routine_model import Routine
from app import db

routine_bp = Blueprint('routine_routes', __name__)

# Helper function to ensure only admins can access certain endpoints
def admin_required(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt_identity()
        if claims['role'] != 'admin':
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    wrapper.__name__ = fn.__name__
    return wrapper

@routine_bp.route('/routines', methods=['POST'])
@admin_required
def create_routine():
    data = request.get_json()
    new_routine = Routine(
        name=data['name'],
        description=data.get('description', ''),
        objective=data['objective'],
        routine_type='predefined'  # Ensure this is a general routine
    )
    db.session.add(new_routine)
    db.session.commit()
    return jsonify({'message': 'Routine created successfully!'}), 201

@routine_bp.route('/routines', methods=['GET'])
@jwt_required()
def get_all_routines():
    routines = Routine.query.all()
    result = [{'id': r.id, 'name': r.name, 'objective': r.objective} for r in routines]
    return jsonify(result), 200

@routine_bp.route('/routines/<int:routine_id>', methods=['GET'])
@jwt_required()
def get_routine(routine_id):
    routine = Routine.query.get_or_404(routine_id)
    return jsonify({
        'id': routine.id,
        'name': routine.name,
        'objective': routine.objective,
        'description': routine.description
    }), 200

@routine_bp.route('/routines/<int:routine_id>', methods=['PUT'])
@admin_required
def update_routine(routine_id):
    data = request.get_json()
    routine = Routine.query.get_or_404(routine_id)
    routine.name = data.get('name', routine.name)
    routine.description = data.get('description', routine.description)
    routine.objective = data.get('objective', routine.objective)
    db.session.commit()
    return jsonify({'message': 'Routine updated successfully!'}), 200

@routine_bp.route('/routines/<int:routine_id>', methods=['DELETE'])
@admin_required
def delete_routine(routine_id):
    routine = Routine.query.get_or_404(routine_id)
    db.session.delete(routine)
    db.session.commit()
    return jsonify({'message': 'Routine deleted successfully!'}), 200
