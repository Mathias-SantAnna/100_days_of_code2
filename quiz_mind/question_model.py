class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_1 = Question("What is your favorite color?", "blue")
print(question_1.text)
