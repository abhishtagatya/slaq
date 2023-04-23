from typing import List

from slaq.orm.model import Answer

import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session


class AnswerORM:

    def __init__(self, db: sqlalchemy.engine.Engine):
        self.db = db

    def create_new_answer(self, answer_str: str, submitter_id: str, team_id: str):
        with Session(self.db) as session:
            statement = insert(Answer).values(
                answer_str=answer_str,
                submitter_id=submitter_id,
                team_id=team_id
            ).returning(Answer)
            [temp] = session.execute(statement).fetchone()
            result = temp.id

            session.commit()

        return result

    def get_answer_by_ids(self, ids: List[int]):

        with Session(self.db) as session:
            result = session.query(Answer).filter(
                Answer.id in ids
            ).all()

        return result
