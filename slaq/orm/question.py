from slaq.orm.model import Question

import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session


class QuestionORM:

    def __init__(self, db: sqlalchemy.engine.Engine):
        self.db = db

    def create_new_question(self,
                            question_str: str,
                            submitter_id: str,
                            team_id: str,
                            answer_id: int):
        with Session(self.db) as session:
            statement = insert(Question).values(
                question_str=question_str,
                submitter_id=submitter_id,
                team_id=team_id,
                answer_id=answer_id
            ).returning(Question)
            [temp] = session.execute(statement).fetchone()
            result = temp.id

            session.commit()

        return result

    def get_questions_by_filter(self, team_id: str):

        with Session(self.db) as session:
            result = session.query(Question).filter(
                Question.team_id == team_id
            ).all()

        return result
