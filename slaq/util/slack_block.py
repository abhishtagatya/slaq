import copy
from typing import Dict, List

from slaq.const import *


class BlockKit:
    INPUT_ACTION_TEXT = 'plain_text_input-action'

    FIELD_TEXT = 'text'
    FIELD_VALUE = 'value'
    FIELD_ACCESSORY = 'accessory'
    FIELD_ELEMENT = 'element'
    FIELD_ELEMENTS = 'elements'
    FIELD_BLOCKS = 'blocks'
    FIELD_PLACEHOLDER = 'placeholder'
    FIELD_IVALUE = 'initial_value'
    FIELD_CALLBACK = 'callback_id'

    @staticmethod
    def construct_faq_add_modal():
        return copy.deepcopy(VIEW_ADD_FAQ_BLOCK)

    @staticmethod
    def construct_faq_edit_modal(uid: int, question: str, answer: str):
        base_modal = copy.deepcopy(VIEW_EDIT_FAQ_BLOCK)
        base_modal[BlockKit.FIELD_CALLBACK] += "_" + str(uid)
        base_modal[BlockKit.FIELD_BLOCKS][1][BlockKit.FIELD_ELEMENT][BlockKit.FIELD_IVALUE] = question
        base_modal[BlockKit.FIELD_BLOCKS][2][BlockKit.FIELD_ELEMENT][BlockKit.FIELD_IVALUE] = answer
        return base_modal

    @staticmethod
    def get_value_from_text_input(data: Dict, block_id: str):
        return data[block_id][BlockKit.INPUT_ACTION_TEXT][BlockKit.FIELD_VALUE]

    @staticmethod
    def construct_questions_list_modal(data: List):
        base_modal = copy.deepcopy(VIEW_LIST_QUESTION_BLOCK)

        data_len = len(data) - 1
        for idx, datum in enumerate(data):
            new_section = copy.deepcopy(VIEW_LIST_QUESTION_SECTION_BLOCK)
            new_section[BlockKit.FIELD_TEXT][BlockKit.FIELD_TEXT] = datum.question_str
            new_section[BlockKit.FIELD_ACCESSORY][BlockKit.FIELD_VALUE] = 'delete-' + str(datum.id)

            new_context = copy.deepcopy(VIEW_LIST_QUESTION_CONTEXT_BLOCK)
            new_markdown_block = copy.deepcopy(MARKDOWN_BLOCK)
            new_markdown_block[BlockKit.FIELD_TEXT] = "Attached to Answer ID : " + str(datum.answer_id)

            new_context[BlockKit.FIELD_ELEMENTS].append(new_markdown_block)

            base_modal[BlockKit.FIELD_BLOCKS].append(new_section)
            base_modal[BlockKit.FIELD_BLOCKS].append(new_context)

            if idx != data_len:
                base_modal[BlockKit.FIELD_BLOCKS].append(DIVIDER_BLOCK)

        return base_modal

    @staticmethod
    def construct_answers_list_modal(data: List):
        base_modal = copy.deepcopy(VIEW_LIST_ANSWER_BLOCK)

        data_len = len(data) - 1
        for idx, datum in enumerate(data):
            new_section = copy.deepcopy(VIEW_LIST_ANSWER_SECTION_BLOCK)
            new_section[BlockKit.FIELD_TEXT][BlockKit.FIELD_TEXT] = f"Answer ID : {datum.id}\n\n_{datum.answer_str}_"
            new_section[BlockKit.FIELD_ACCESSORY][BlockKit.FIELD_VALUE] = 'delete-' + str(datum.id)

            base_modal[BlockKit.FIELD_BLOCKS].append(new_section)

            if idx != data_len:
                base_modal[BlockKit.FIELD_BLOCKS].append(DIVIDER_BLOCK)

        return base_modal

    @staticmethod
    def construct_faq_list_modal(data: List):
        base_modal = copy.deepcopy(VIEW_LIST_FAQ_BLOCK)

        data_len = len(data) - 1
        for idx, datum in enumerate(data):
            new_question_block = copy.deepcopy(VIEW_LIST_FAQ_QUESTION_BLOCK)
            new_question_block[BlockKit.FIELD_TEXT][BlockKit.FIELD_TEXT] = datum.question_str

            new_answer_block = copy.deepcopy(VIEW_LIST_FAQ_ANSWER_BLOCK)
            new_answer_md_block = copy.deepcopy(MARKDOWN_BLOCK)
            new_answer_md_block[BlockKit.FIELD_TEXT] = datum.answer_str
            new_answer_block[BlockKit.FIELD_ELEMENTS].append(new_answer_md_block)

            new_button_block = copy.deepcopy(VIEW_LIST_FAQ_BUTTON_BLOCK)
            new_button_block[BlockKit.FIELD_ELEMENTS][0][BlockKit.FIELD_VALUE] = "edit-" + str(datum.id)
            new_button_block[BlockKit.FIELD_ELEMENTS][1][BlockKit.FIELD_VALUE] = "delete-" + str(datum.id)

            base_modal[BlockKit.FIELD_BLOCKS].append(new_question_block)
            base_modal[BlockKit.FIELD_BLOCKS].append(new_answer_block)
            base_modal[BlockKit.FIELD_BLOCKS].append(new_button_block)

            if idx != data_len:
                base_modal[BlockKit.FIELD_BLOCKS].append(DIVIDER_BLOCK)

        return base_modal
