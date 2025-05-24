# Quiz Runner
# This code is a simple quiz application that allows users to take a quiz, select answers, and view their results.

import tkinter as tk
from tkinter import messagebox

class QuizDataLoader:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        self.questions = []

        def load_questions(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip().split("\n\n")
                for block in content:
                    if not block.strip():
                        continue
                    lines = [line.strip() for line in block.split("\n") if line.strip()]
                    if len(lines) < 6:
                        continue  # skip malformed question blocks
                    question_data = {
                        'question': lines[0].replace("Question: ", ""),
                        'answers': {
                            'a': lines[1].replace("A: ", ""),
                            'b': lines[2].replace("B: ", ""),
                            'c': lines[3].replace("C: ", ""),
                            'd': lines[4].replace("D: ", ""),
                        },
                        'correct': lines[5].replace("Correct Answer: ", "").lower()
                    }
                    self.questions.append(question_data)
            return self.questions
        except FileNotFoundError:
            raise FileNotFoundError(f"Quiz questions file '{self.filename}' not found.")

class QuizSession:   
    def __init__(self, user_name, questions, score_filename="quiz_score.txt"):
        self.user_name = user_name
        self.questions = questions
        self.score_filename = score_filename
        self.current_index = 0
        self.user_answers = []

    def record_answer(self, answer):
        self.user_answers.append(answer)
        self.current_index += 1

    def is_finished(self):
        return self.current_index >= len(self.questions)

