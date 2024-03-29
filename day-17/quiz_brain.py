class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        answer = input(
            f'Q{self.question_number+1}. {self.question_bank[self.question_number].text} (True/False): ')
        self.check_answer(answer, self.question_bank[self.question_number])
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number >= len(self.question_bank)-1:
            return False
        return True

    def check_answer(self, answer, question):
        if question.answer.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong")
        print(f"The correct answer is {question.answer}")
        print(f"Current Score {self.score}/{self.question_number+1}")
        print('\n')
