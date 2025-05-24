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

    def start_quiz(self):
        user_name = self.name_entry.get().strip()
        if not user_name:
            messagebox.showerror("Error!", "Please enter your name!")
            return

        try:
            questions = self.data_loader.load_questions()
            if not questions:
                messagebox.showerror("Error!", "No questions found!")
                self.window.destroy()
                return
        except FileNotFoundError as e:
            messagebox.showerror("Error!", str(e))
            self.window.destroy()
            return

        self.session = QuizSession(user_name, questions)

        # Clear start screen widgets
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_btn.pack_forget()

        self._display_question()

    def _display_question(self):
        if self.session.is_finished():
            self._show_results()
            return

        question_data = self.session.questions[self.session.current_index]

        self.q_frame = tk.Frame(self.window)
        self.q_frame.pack(pady=40, padx=100)

        self.question_label = tk.Label(
            self.q_frame, 
            text=question_data['question'], 
            wraplength=500,
            font=("Arial", 14, "bold")
        )
        self.question_label.pack(pady=10, padx=10)

        self.answer_var = tk.StringVar(value=None)

        for option in ['a', 'b', 'c', 'd']:
            answer_text = f"{option.upper()}: {question_data['answers'][option]}"
            rb = tk.Radiobutton(
                self.q_frame,
                text=answer_text,
                variable=self.answer_var,
                value=option,
                wraplength=400,
                justify='left',
                font=("Arial", 12)
            )
            rb.pack(anchor='w', pady=10)

        self.nav_frame = tk.Frame(self.window)
        self.nav_frame.pack(pady=10)

        if self.session.current_index < len(self.session.questions) - 1:
            next_btn = tk.Button(self.nav_frame, text="Next", command=self._next_question)
            next_btn.pack(side='right', padx=10)
        else:
            submit_btn = tk.Button(self.nav_frame, text="Submit", command=self._show_results)
            submit_btn.pack(side='right', padx=10)

    def _next_question(self):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showerror("Error!", "Please select an answer!")
            return

        self.session.record_answer(selected)
        self.q_frame.destroy()
        self.nav_frame.destroy()
        self._display_question()

    def _show_results(self):
        selected = self.answer_var.get()
        if selected:
            self.session.record_answer(selected)
        else:
            # If user tries to submit without selecting last answer
            messagebox.showerror("Error!", "Please select an answer!")
            return

        score = self.session.save_results()
        total = len(self.session.questions)

        messagebox.showinfo("Results", f"Thank you, {self.session.user_name}!\nYour score: {score}/{total}")
        self.window.destroy()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = QuizRunnerGUI()
    app.run()