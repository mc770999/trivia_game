from dataclasses import asdict

from flask import Blueprint, jsonify, request

from model.answer_model import Answer
from repository.answer_repository import get_all_answers
from repository.question_repository import get_all_questions, create_question
from service.question_service import create_full_question_on_db

question_blueprint = Blueprint("question",__name__)

@question_blueprint.route("/question", methods=['GET'])
def get_all():
    fighters = list(map(asdict, get_all_questions()))
    return jsonify(fighters), 200



def create():
    try:
        data = request.json
        # Create the question using the data from the request
        new_question = create_full_question_on_db(data)
        return jsonify(asdict(new_question)), 201
    except Exception as e:
        return jsonify({"error": str(e)}),
