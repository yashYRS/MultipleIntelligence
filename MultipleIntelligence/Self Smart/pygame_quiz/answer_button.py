from button import Button
from colors import Color


class AnswerButton(Button):

    def __init__(self, x, y, w, h, text, on_click_func=None, score_weight = 0 ):
        super().__init__(x, y, w, h, text, on_click_func)
        self.score_weight = score_weight
        self.PRESSED_BACK_COLOR = Color.WHITE
