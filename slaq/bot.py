import os
import logging
from dotenv import load_dotenv

from slaq.const import (
    ADD_FAQ_CID,
    VIEW_QUESTION_FIELD_BID,
    VIEW_ANSWER_FIELD_BID,
    VIEW_ADD_FAQ_RESP,
    VIEW_ADD_FAQ_BLOCK
)
from slaq.db import Database
from slaq.orm.question import QuestionORM
from slaq.orm.answer import AnswerORM
from slaq.util.slack_block import BlockKit

from slack_bolt import App

load_dotenv()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

bot = App(
    token=os.getenv('SLACK_BOT_TOKEN'),
    signing_secret=os.getenv('SLACK_SIGNING_SECRET')
)

db = Database(database_url=os.getenv('DATABASE_URL'))
question_orm = QuestionORM(db=db.db)
answer_orm = AnswerORM(db=db.db)


# Middleware
@bot.middleware
def log_request(logger, body, next):
    logger.info(body)
    return next()


@bot.event("app_mention")
def handle_mention(body, say, logger):
    event = body["event"]
    logger.debug(event)

    thread_ts = event.get("thread_ts", None) or event["ts"]

    say(f"What can I do for you?", thread_ts=thread_ts)


@bot.command("/add-faq")
def handle_command(body, ack, client, logger):
    logger.info(body)
    ack(
        text="Adding new FAQ",
        blocks=VIEW_ADD_FAQ_RESP
    )

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view=VIEW_ADD_FAQ_BLOCK
    )
    logger.info(res)


@bot.options("es_a")
def show_options(ack):
    ack({"options": [{"text": {"type": "plain_text", "text": "Maru"}, "value": "maru"}]})


@bot.options("mes_a")
def show_multi_options(ack):
    ack(
        {
            "option_groups": [
                {
                    "label": {"type": "plain_text", "text": "Group 1"},
                    "options": [
                        {
                            "text": {"type": "plain_text", "text": "Option 1"},
                            "value": "1-1",
                        },
                        {
                            "text": {"type": "plain_text", "text": "Option 2"},
                            "value": "1-2",
                        },
                    ],
                },
                {
                    "label": {"type": "plain_text", "text": "Group 2"},
                    "options": [
                        {
                            "text": {"type": "plain_text", "text": "Option 1"},
                            "value": "2-1",
                        },
                    ],
                },
            ]
        }
    )


@bot.view(ADD_FAQ_CID)
def add_faq_submission(ack, body, logger):
    ack()

    user_id = body["user"]["id"]
    team_id = body["team"]["id"]
    data = body["view"]["state"]["values"]

    sub_question_field = BlockKit.get_value_from_text_input(data, VIEW_QUESTION_FIELD_BID)
    sub_answer_field = BlockKit.get_value_from_text_input(data, VIEW_ANSWER_FIELD_BID)

    new_answer = answer_orm.create_new_answer(
        answer_str=sub_answer_field,
        submitter_id=user_id,
        team_id=team_id
    )
    new_question = question_orm.create_new_question(
        question_str=sub_question_field,
        submitter_id=user_id,
        team_id=team_id,
        answer_id=new_answer
    )

    logger.info(f"Questions: {new_question}, Answer: {new_answer}")
    logger.info(body)
