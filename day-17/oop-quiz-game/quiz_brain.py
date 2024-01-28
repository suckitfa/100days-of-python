'''
Date: 2024-01-28 14:02:29
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-28 16:44:54
FilePath: \100days-of-python\day-17\oop-quiz-game\quiz_brain.py
'''
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.q_text}(True/False):")
        self.check_answer(user_answer,current_question.q_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Incorrect!")
        print(f"THe correct answer is: {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number+1}")
        print('\n')