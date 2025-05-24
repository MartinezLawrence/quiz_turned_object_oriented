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

    def calculate_score(self):
        return sum(
            1 for i, q in enumerate(self.questions) 
            if i < len(self.user_answers) and self.user_answers[i] == q['correct']
        )

    def save_results(self):
        score = self.calculate_score()
        with open(self.score_filename, "a", encoding="utf-8") as file:
            file.write(f"Name: {self.user_name}\n")
            file.write(f"Score: {score}/{len(self.questions)}\n")
            for i, question in enumerate(self.questions):
                user_answer = self.user_answers[i].upper() if i < len(self.user_answers) else "N/A"
                correct_answer = question['correct'].upper()
                file.write(f"Q{i+1}: {question['question']}\n")
                file.write(f"Your Answer: {user_answer}\n")
                file.write(f"Correct Answer: {correct_answer}\n\n")
            file.write("-" * 50 + "\n")
        return score
    
class QuizRunnerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("QuizRunner")

        self.data_loader = QuizDataLoader()
        self.session = None

        self._setup_start_screen()

    def _setup_start_screen(self):
        self.name_label = tk.Label(self.window, text="Enter your name:")
        self.name_label.pack(pady=20)

        self.name_entry = tk.Entry(self.window, width=60)
        self.name_entry.pack(pady=10)

        self.start_btn = tk.Button(self.window, text="Start Quiz", command=self.start_quiz)
        self.start_btn.pack(pady=20)
