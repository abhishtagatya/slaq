from typing import List

from slaq.const import *


class Control:

    @staticmethod
    def answer_query(data: List, t_high: int = 0.7, t_low: int = 0.5):
        if any(datum['similarity'] >= t_high for datum in data):
            return data[0]['faq'].answer_str + CONTROL_RESPONSE_ADDITIONAL

        if all(datum['similarity'] < t_low for datum in data):
            return CONTROL_RESPONSE_NOT_FOUND

        temp_response = CONTROL_RESPONSE_UNSURE
        for idx, datum in enumerate(data):
            temp_response += f"{idx + 1}. {datum['faq'].question_str}\n"
        temp_response += CONTROL_RESPONSE_UNSURE_ADDITIONAL
        return temp_response


