from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your score is: {quiz.score}/{len(quiz.question_list)}")