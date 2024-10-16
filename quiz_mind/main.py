import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)
print("Welcome to Geography quiz!")
print("You have 10 questions to guess which is true or false.")

def get_questions_for_difficulty():
    chosen_difficulty = input("Choose a difficulty to start (easy, medium): \n").lower()
    question_bank = []
    for question in question_data:
        if question["difficulty"] == chosen_difficulty:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            question_difficulty = question["difficulty"]  # Extract the difficulty
            new_question = Question(question_text, question_answer, question_difficulty)
            question_bank.append(new_question)

    if not question_bank:
        print(f"No questions available for the difficulty '{chosen_difficulty}'. Exiting the game.")
        return None
    else:
        random.shuffle(question_bank)  # Randomize the order of the questions
        return question_bank



# Initialize the Quiz
question_bank = get_questions_for_difficulty()

if question_bank:
    quiz = QuizBrain(question_bank)
    quiz.play_quiz()
