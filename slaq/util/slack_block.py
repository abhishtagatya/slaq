from typing import Dict


class BlockKit:

    INPUT_ACTION_TEXT = 'plain_text_input-action'

    FIELD_VALUE = 'value'

    @staticmethod
    def get_value_from_text_input(data: Dict, block_id: str):
        return data[block_id][BlockKit.INPUT_ACTION_TEXT][BlockKit.FIELD_VALUE]