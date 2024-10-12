from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Creates question bank
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#Quiz initialize
quiz = QuizBrain(question_bank)

# Play the quiz
quiz.play_quiz()