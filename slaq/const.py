# View Block with https://app.slack.com/block-kit-builder

# General Section

DIVIDER_BLOCK = {
    "type": "divider"
}

MARKDOWN_BLOCK = {
    "type": "mrkdwn",
    "text": ""
}

TEXT_ADD_FAQ_MODAL = ":scroll: Log : New FAQ Entry has been added by you."
TEXT_EDIT_FAQ_MODAL = ":scroll: Log : FAQ Entry has been edited by you."
TEXT_DELETE_FAQ_MODAL = ":scroll: Log : FAQ Entry has been deleted by you."

CONTROL_RESPONSE_ADDITIONAL = "\n\nDoes this answer your question? :grin:"
CONTROL_RESPONSE_UNSURE = ":thinking_face: Hmm... I seem to be having trouble understanding your question, is it similar to any of these:\n\n"
CONTROL_RESPONSE_UNSURE_ADDITIONAL = "\n\nIf there are, could you rephrase the question?"
CONTROL_RESPONSE_NOT_FOUND = "Hmm.. I don't think I can answer this question, you can also check my FAQ List using the */list-faq* command. Can anyone help follow up this? :raised_hand:"

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

# App Home Screen

VIEW_APP_HOME_BLOCK = {
    "type": "home",
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Welcome to Slaq :speech_balloon:*"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": "Author: Abhishta Gatya",
                    "emoji": True
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Slaq is a tool to answer frequently-asked questions on your Workspace. All you need to do is mention *@Slaq* when asking questions <https://github.com/abhishtagatya/slaq|*Learn More*>."
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Adding FAQs*"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": "Adding new entry of Frequently-Asked Questions",
                    "emoji": True
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Use the */add-faq* command to open the _Add FAQ_ modal. Fill in the question and answer set for every entry you want to be easily answered."
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Managing FAQs*"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": "Managing existing entries of Frequently-Asked Questions",
                    "emoji": True
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Use the */list-faq* command to open the _List FAQ_ modal. This will enlist all existing FAQs in this Workspace. You can also manage to edit or delete past entries."
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "That is all; If any issues occur please direct yourself over to the <https://github.com/abhishtagatya/slaq/issues|*Issue Page*> for further information. Thank you!"
            }
        }
    ]
}
