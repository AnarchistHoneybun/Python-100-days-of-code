

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        ans = input(f"Q.{self.question_number+1} {self.question_list[self.question_number].text} (True/False)?: ").lower()
        if ans == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print(f"You got it right!\nYour current score is {self.score}/{self.question_number+1}")
        else:
            print(f"That's wrong.\nThe correct answer was: {self.question_list[self.question_number].answer}")
            print(f"Your current score is {self.score}/{self.question_number+1}")
        self.question_number += 1
