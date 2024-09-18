from dataclasses import dataclass

@dataclass
class Answer:
   question_id: int
   answer_txt: str
   is_correct: bool
   id: int = None