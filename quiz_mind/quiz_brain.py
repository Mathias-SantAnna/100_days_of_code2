class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Congrats! Correct Answer!")
        else:
            print(f"Your answer is wrong. The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}.\n")

    def restart_game(self):
        while True:
            if not self.still_has_questions():
                print(f"\nYour final score is {self.score} out of {len(self.question_list)}.")
                play_again = input("Do you want to play again? (Y/N): ").lower()

                if play_again == "y":
                    self.question_number = 0  # Reset question number
                    self.score = 0  # Reset score
                    print("Restarting the game...\n")
                    self.play_quiz()
                else:
                    print("Thank you for playing!")
                    break

    def play_quiz(self):
        while self.still_has_questions():
            self.next_question()
        self.restart_game()