from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Ask the user to choose a difficulty level
chosen_difficulty = input("Choose a difficulty (easy, medium): ").lower()

#Creates question bank
question_bank = []
for question in question_data:
    if question["difficulty"] == chosen_difficulty:
        question_text = question['question']
        question_answer = question['correct_answer']

        new_question = Question(question_text, question_answer, question["difficulty"])
        question_bank.append(new_question)

# Check if there are questions for the selected difficulty
if not question_bank:
    print(f"No questions available for the difficulty '{chosen_difficulty}'. Exiting the game.")
else:
    # Initialize the Quiz
    quiz = QuizBrain(question_bank)

    # Play the quiz
    quiz.play_quiz()
