from dataclasses import asdict

from flask import Blueprint, jsonify, request

from model.answer_model import Answer
from repository.answer_repository import get_all_answers

answers_blueprint = Blueprint("answers", __name__)

@answers_blueprint.route("/", methods=['GET'])
def get_all():
    fighters = list(map(asdict, get_all_answers()))
    return jsonify(fighters), 200




