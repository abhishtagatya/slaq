from slaq.orm.model import FAQ

import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy.orm import Session


class FAQORM:

    def __init__(self, db: sqlalchemy.engine.Engine):
        self.db = db

    def create_new_faq(self,
                       question_str: str,
                       answer_str: str,
                       team_id: str):
        with Session(self.db) as session:
            statement = insert(FAQ).values(
                question_str=question_str,
                answer_str=answer_str,
                team_id=team_id
            ).returning(FAQ)
            [temp] = session.execute(statement).fetchone()
            result = temp.id

            session.commit()

        return result

    def edit_existing_faq(self,
                          uid: int,
                          question_str: str,
                          answer_str: str):
        with Session(self.db) as session:
            statement = update(FAQ).where(
                FAQ.id == uid
            ).values(
                question_str=question_str,
                answer_str=answer_str
            ).returning(FAQ)
            [temp] = session.execute(statement).fetchone()
            result = temp.id

            session.commit()

        return result

    def get_faq_by_team(self, team_id: str):
        with Session(self.db) as session:
            result = session.query(FAQ).filter(
                FAQ.team_id == team_id
            ).all()

        return result

    def get_faq_by_id(self, uid: int):
        with Session(self.db) as session:
            result = session.query(FAQ).filter(
                FAQ.id == uid
            ).first()

        return result

    def delete_faq_by_id(self, uid: int):
        with Session(self.db) as session:
            statement = delete(FAQ).where(FAQ.id == uid)
            session.execute(statement)
            session.commit()
