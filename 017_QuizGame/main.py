from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    dyn = Question(question["question"], question["correct_answer"])
    question_bank.append(dyn)

random.shuffle(question_bank)

quiz_brain = QuizBrain(question_bank)
for i in range (len(quiz_brain.question_list)-2):
    quiz_brain.next_question()

print(f"\n\nYou've completed the quiz\nYour final score was {quiz_brain.score}/{len(quiz_brain.question_list)-2}")