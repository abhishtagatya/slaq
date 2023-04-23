# View Block with https://app.slack.com/block-kit-builder

# Add FAQ Section
VIEW_QUESTION_FIELD_BID = "question-field"
VIEW_ANSWER_FIELD_BID = "answer-field"

ADD_FAQ_CID = "add-faq-cb"

VIEW_ADD_FAQ_RESP = [
    {
        "type": "section",
        "block_id": "add-faq-block",
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: Opened 'Add FAQ' Modal!",
        },
    }
]

VIEW_ADD_FAQ_BLOCK = {
    "type": "modal",
    "callback_id": ADD_FAQ_CID,
    "submit": {
        "type": "plain_text",
        "text": "Save",
        "emoji": True
    },
    "close": {
        "type": "plain_text",
        "text": "Discard",
        "emoji": True
    },
    "title": {
        "type": "plain_text",
        "text": "Add Workspace FAQ",
        "emoji": True
    },
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "input",
            "block_id": VIEW_QUESTION_FIELD_BID,
            "element": {
                "type": "plain_text_input",
                "action_id": "plain_text_input-action"
            },
            "label": {
                "type": "plain_text",
                "text": "What was the question?",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": VIEW_ANSWER_FIELD_BID,
            "element": {
                "type": "plain_text_input",
                "multiline": True,
                "action_id": "plain_text_input-action"
            },
            "label": {
                "type": "plain_text",
                "text": "What was the answer?",
                "emoji": True
            }
        }
    ]
}
