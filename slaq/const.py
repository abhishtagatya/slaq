# View Block with https://app.slack.com/block-kit-builder

# General Section

DIVIDER_BLOCK = {
    "type": "divider"
}

MARKDOWN_BLOCK = {
    "type": "mrkdwn",
    "text": ""
}

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
                "action_id": "plain_text_input-action",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Ex. Where is the Data Request Sheet?"
                }
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
                "action_id": "plain_text_input-action",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Ex. It is attached on the #data channel."
                }
            },
            "label": {
                "type": "plain_text",
                "text": "What was the answer?",
                "emoji": True
            }
        }
    ]
}

# Edit FAQ Section

EDIT_FAQ_CID = "edit-faq-cb"
EDIT_FAQ_CID_REGEX = "edit-faq-cb_\d+"

VIEW_EDIT_FAQ_BLOCK = {
    "type": "modal",
    "callback_id": EDIT_FAQ_CID,
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
        "text": "Edit Workspace FAQ",
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
                "action_id": "plain_text_input-action",
                "initial_value": ""
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
                "action_id": "plain_text_input-action",
                "initial_value": ""
            },
            "label": {
                "type": "plain_text",
                "text": "What was the answer?",
                "emoji": True
            }
        }
    ]
}

# List FAQ Section

LIST_FAQ_CID = "list-faq-cb"
LIST_FAQ_BID = "list-faq-block"

EDIT_FAQ_AID = "edit-faq-action"
DELETE_FAQ_AID = "delete-faq-action"

VIEW_LIST_FAQ_RESP = [
    {
        "type": "section",
        "block_id": LIST_FAQ_BID,
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: Opened 'List of FAQ' Modal!",
        },
    }
]

# VIEW_LIST_SUCCESS_RESP = [
#     {
#         "type": "section",
#         "block_id": "list-question-block",
#         "text": {
#             "type": "mrkdwn",
#             "text": ":white_check_mark: Your entry has been saved!",
#         },
#     }
# ]

VIEW_LIST_FAQ_QUESTION_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": ""
    }
}

VIEW_LIST_FAQ_ANSWER_BLOCK = {
    "type": "context",
    "elements": []
}

VIEW_LIST_FAQ_BUTTON_BLOCK = {
    "type": "actions",
    "elements": [
        {
            "type": "button",
            "action_id": EDIT_FAQ_AID,
            "text": {
                "type": "plain_text",
                "text": "Edit",
                "emoji": True
            },
            "value": ""
        },
        {
            "type": "button",
            "action_id": DELETE_FAQ_AID,
            "text": {
                "type": "plain_text",
                "text": "Delete",
                "emoji": True
            },
            "style": "danger",
            "value": ""
        }
    ]
}

VIEW_LIST_FAQ_BLOCK = {
    "type": "modal",
    "callback_id": LIST_FAQ_CID,
    "title": {
        "type": "plain_text",
        "text": "List of Questions",
        "emoji": True
    },
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Saved Frequently Asked Questions (FAQ) for Slaq in this Workspace.",
                "emoji": True
            }
        },
        {
            "type": "divider"
        }
    ]
}

# List Question Section

LIST_QUESTION_CID = "list-question-cb"
LIST_QUESTION_BID = "list-question-block"

DELETE_QUESTION_AID = "delete-question-action"

VIEW_LIST_QUESTION_RESP = [
    {
        "type": "section",
        "block_id": LIST_QUESTION_BID,
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: Opened 'List of Questions' Modal!",
        },
    }
]

# VIEW_LIST_SUCCESS_RESP = [
#     {
#         "type": "section",
#         "block_id": "list-question-block",
#         "text": {
#             "type": "mrkdwn",
#             "text": ":white_check_mark: Your entry has been saved!",
#         },
#     }
# ]

VIEW_LIST_QUESTION_SECTION_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": ""
    },
    "accessory": {
        "type": "button",
        "action_id": DELETE_QUESTION_AID,
        "text": {
            "type": "plain_text",
            "text": "Delete",
            "emoji": True
        },
        "style": "danger",
        "value": ""
    }
}

VIEW_LIST_QUESTION_CONTEXT_BLOCK = {
    "type": "context",
    "elements": []
}

VIEW_LIST_QUESTION_BLOCK = {
    "type": "modal",
    "callback_id": LIST_QUESTION_CID,
    "title": {
        "type": "plain_text",
        "text": "List of Questions",
        "emoji": True
    },
    "blocks": []
}

# List Answer Section

LIST_ANSWER_CID = "list-answer-cb"
LIST_ANSWER_BID = "list-answer-block"

DELETE_ANSWER_AID = "delete-answer-action"

VIEW_LIST_ANSWER_RESP = [
    {
        "type": "section",
        "block_id": LIST_ANSWER_BID,
        "text": {
            "type": "mrkdwn",
            "text": ":white_check_mark: Opened 'List of Answers' Modal!",
        },
    }
]

# VIEW_LIST_SUCCESS_RESP = [
#     {
#         "type": "section",
#         "block_id": "list-question-block",
#         "text": {
#             "type": "mrkdwn",
#             "text": ":white_check_mark: Your entry has been saved!",
#         },
#     }
# ]

VIEW_LIST_ANSWER_SECTION_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": ""
    },
    "accessory": {
        "type": "button",
        "action_id": DELETE_ANSWER_AID,
        "text": {
            "type": "plain_text",
            "text": "Delete",
            "emoji": True
        },
        "style": "danger",
        "value": ""
    }
}

VIEW_LIST_ANSWER_CONTEXT_BLOCK = {
    "type": "context",
    "elements": []
}

VIEW_LIST_ANSWER_BLOCK = {
    "type": "modal",
    "callback_id": LIST_ANSWER_CID,
    "title": {
        "type": "plain_text",
        "text": "List of Answers",
        "emoji": True
    },
    "blocks": []
}
