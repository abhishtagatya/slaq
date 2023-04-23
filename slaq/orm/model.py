import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class BaseModel(DeclarativeBase):
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }


class Question(BaseModel):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_str: Mapped[str] = mapped_column(String(4000))
    team_id: Mapped[str] = mapped_column(String(12))
    submitter_id: Mapped[str] = mapped_column(String(12))
    answer_id: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f'(Question: {self.id}, {self.submitter_id}, {self.team_id})'


class Answer(BaseModel):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    answer_str: Mapped[str] = mapped_column(String(4000))
    team_id: Mapped[str] = mapped_column(String(12))
    submitter_id: Mapped[str] = mapped_column(String(12))

    def __repr__(self):
        return f'(Answer: {self.id}, {self.submitter_id}, {self.team_id})'
