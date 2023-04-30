import os
import logging
import re

from dotenv import load_dotenv

from slaq.const import *
from slaq.db import Database
from slaq.orm.faq import FAQORM
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
faq_orm = FAQORM(db=db.db)


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
def handle_add_faq_command(body, ack, client, logger):
    ack(
        text="Adding new FAQ",
        blocks=VIEW_ADD_FAQ_RESP
    )

    faq_modal = BlockKit.construct_faq_add_modal()
    res = client.views_open(
        trigger_id=body["trigger_id"],
        view=faq_modal
    )
    logger.info(res)


@bot.command("/list-faq")
def handle_list_faq_command(body, ack, client, logger):
    ack(
        text="Listing FAQs",
        blocks=VIEW_LIST_FAQ_RESP
    )

    logger.info(body)
    team_id = body["team_id"]
    faq_list = faq_orm.get_faq_by_team(team_id=team_id)
    faq_modal = BlockKit.construct_faq_list_modal(data=faq_list)

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view=faq_modal
    )
    logger.info(res)


@bot.view(ADD_FAQ_CID)
def add_faq_submission(ack, body, client, logger):
    ack()

    user_id = body["user"]["id"]
    team_id = body["team"]["id"]
    data = body["view"]["state"]["values"]

    sub_question_field = BlockKit.get_value_from_text_input(data, VIEW_QUESTION_FIELD_BID)
    sub_answer_field = BlockKit.get_value_from_text_input(data, VIEW_ANSWER_FIELD_BID)

    faq_orm.create_new_faq(
        question_str=sub_question_field,
        answer_str=sub_answer_field,
        team_id=team_id
    )

    logger.info(body)

    client.chat_postMessage(channel=user_id, text=TEXT_ADD_FAQ_MODAL)


@bot.action(EDIT_FAQ_AID)
def handle_delete_faq_action(ack, body, client, logger):
    ack()
    logger.info(body)

    action_value = body["actions"][0]["value"]
    _, faq_id = action_value.split("-")

    select_faq = faq_orm.get_faq_by_id(uid=faq_id)
    faq_modal = BlockKit.construct_faq_edit_modal(
        uid=select_faq.id,
        question=select_faq.question_str,
        answer=select_faq.answer_str
    )

    res = client.views_update(
        view_id=body["view"]["id"],
        hash=body["view"]["hash"],
        view=faq_modal
    )

    logger.info(res)


@bot.action(DELETE_FAQ_AID)
def handle_delete_faq_action(ack, body, client, logger):
    ack()
    logger.info(body)

    user_id = body["user"]["id"]
    team_id = body["team"]["id"]
    action_value = body["actions"][0]["value"]
    _, faq_id = action_value.split("-")

    faq_orm.delete_faq_by_id(uid=faq_id)

    faq_list = faq_orm.get_faq_by_team(team_id=team_id)
    faq_modal = BlockKit.construct_faq_list_modal(data=faq_list)

    client.chat_postMessage(channel=user_id, text=TEXT_DELETE_FAQ_MODAL)

    res = client.views_update(
        view_id=body["view"]["id"],
        hash=body["view"]["hash"],
        view=faq_modal
    )
    logger.info(res)


@bot.view(re.compile(EDIT_FAQ_CID_REGEX))
def edit_faq_submission(ack, body, client, logger):
    ack()

    user_id = body["user"]["id"]
    team_id = body["team"]["id"]
    callback_id = body["view"]["callback_id"]
    data = body["view"]["state"]["values"]

    sub_question_field = BlockKit.get_value_from_text_input(data, VIEW_QUESTION_FIELD_BID)
    sub_answer_field = BlockKit.get_value_from_text_input(data, VIEW_ANSWER_FIELD_BID)
    _, faq_id = callback_id.split('_')

    faq_orm.edit_existing_faq(
        uid=int(faq_id),
        question_str=sub_question_field,
        answer_str=sub_answer_field
    )

    logger.info(body)

    client.chat_postMessage(channel=user_id, text=TEXT_EDIT_FAQ_MODAL)


@bot.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # Call views.publish with the built-in client
        client.views_publish(
            # Use the user ID associated with the event
            user_id=event["user"],
            view=VIEW_APP_HOME_BLOCK
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
