from service.answer_service import convert_to_answers
from model.answer_model import Answer
from model.question_model import Question
from repository.question_repository import create_question
from  repository.answer_repository import create_answer
from typing import List


def create_full_question_on_db(json) -> None:
    question = _convert_question_model(json)
    q_id = create_question(question)
    answers : List[Answer] = convert_to_answers(json ,q_id)
    for answer in answers:
        create_answer(answer)
    return q_id




def _convert_question_model(json):
    return Question(json["question"])

