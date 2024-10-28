from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.training_plan_model import TrainingPlan
from app import db

training_plan_bp = Blueprint('training_plan_routes', __name__)

@training_plan_bp.route('/training-plans', methods=['POST'])
@jwt_required()
def create_training_plan():
    data = request.get_json()
    new_plan = TrainingPlan(
        name=data['name'],
        description=data.get('description', ''),
        objective=data['objective'],
        duration=data['duration'],
        weekly_frequency=data['weekly_frequency'],
        difficulty_level=data['difficulty_level']
    )
    db.session.add(new_plan)
    db.session.commit()
    return jsonify({'message': 'Training plan created successfully!'}), 201

@training_plan_bp.route('/training-plans', methods=['GET'])
@jwt_required()
def get_all_training_plans():
    plans = TrainingPlan.query.all()
    result = [{'id': p.id, 'name': p.name, 'objective': p.objective} for p in plans]
    return jsonify(result), 200

@training_plan_bp.route('/training-plans/<int:plan_id>', methods=['GET'])
@jwt_required()
def get_training_plan(plan_id):
    plan = TrainingPlan.query.get_or_404(plan_id)
    return jsonify({
        'id': plan.id,
        'name': plan.name,
        'objective': plan.objective,
        'description': plan.description,
        'duration': plan.duration,
        'weekly_frequency': plan.weekly_frequency,
        'difficulty_level': plan.difficulty_level
    }), 200

@training_plan_bp.route('/training-plans/<int:plan_id>', methods=['PUT'])
@jwt_required()
def update_training_plan(plan_id):
    data = request.get_json()
    plan = TrainingPlan.query.get_or_404(plan_id)
    plan.name = data.get('name', plan.name)
    plan.description = data.get('description', plan.description)
    plan.objective = data.get('objective', plan.objective)
    plan.duration = data.get('duration', plan.duration)
    db.session.commit()
    return jsonify({'message': 'Training plan updated successfully!'}), 200

@training_plan_bp.route('/training-plans/<int:plan_id>', methods=['DELETE'])
@jwt_required()
def delete_training_plan(plan_id):
    plan = TrainingPlan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': 'Training plan deleted successfully!'}), 200
