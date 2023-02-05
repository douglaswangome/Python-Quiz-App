import requests

def get_questions():
  amount = 0
  difficulty = "3"

  while amount<5 or amount>30:
    amount = int(input("How many questions do you want to be asked? (5-30)\n"))

  while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
    difficulty = input("Choose a difficulty (easy/medium/hard): \n")

  parameters = {
    "amount": amount,
    "difficulty": difficulty,
    "type": "boolean"
  }

  response = requests.get(url="https://opentdb.com/api.php", params=parameters)
  response.raise_for_status()
  all_questions = response.json()["results"]

  return all_questions

questions = get_questions()