from cgitb import text
from xxlimited import new
from question_model import Question
from data1 import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nex_question()

print("You have completed the quiz")
print(f"your final score was: {quiz.question_score}/{quiz.question_number}")
