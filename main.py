from data import questions
from Question import Question
from Quiz import Quiz

questions_bank = []

for question in questions:
  new_question = Question(question["question"], question["correct_answer"])
  questions_bank.append(new_question)

quiz = Quiz(questions_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{len(questions_bank)}")