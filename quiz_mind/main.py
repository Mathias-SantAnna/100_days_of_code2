from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

#Creates question bank
question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#Quiz initialize
quiz = QuizBrain(question_bank)

# Play the quiz
quiz.play_quiz()