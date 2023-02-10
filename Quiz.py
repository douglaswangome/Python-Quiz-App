import html

class Quiz():
  def __init__(self, question_list):
    self.score = 0
    self.question_number = 0
    self.question_list = question_list

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number} {html.unescape(current_question.text)} (True/False)\n")
    self.check_answer(current_question.answer, user_answer)

  def check_answer(self, correct_answer, user_answer):
    if correct_answer.lower() == user_answer.lower():
      self.score += 1
      print("Yay! You got it right.")
    else:
      print("Oops! You got it wrong.")

    print(f"The answer is {correct_answer}")
    print(f"Your score is {self.score}/{len(self.question_list)}\n")
