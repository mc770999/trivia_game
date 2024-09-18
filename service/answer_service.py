from toolz import pipe,reduce, partial
from toolz.curried import partial

from model.answer_model import Answer
from model.user_model import User

def convert_to_answers(question,q_id):
    answer_list = [question["correct_answer"]] + question["incorrect_answers"]
    def _create_answer(tup):
        return Answer(question_id=q_id, answer_txt=tup[1], is_correct=tup[0] == 0)
    return pipe(
        answer_list,
        partial(enumerate),
        partial(map,_create_answer),
        list
    )



#[{true},{false},{false}]
#[(0,{true}),(1,{false}),{false}]
