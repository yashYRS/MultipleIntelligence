class Question_Object:
    def __init__(self, question_text='test', answers=('q1', 'q2', 'q3'),
                                                       correct_answer=0):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

