from dataclasses import dataclass

@dataclass
class Question:
   question_text: str
   id: int = None