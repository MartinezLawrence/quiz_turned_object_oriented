# quiz creator program using tkinter in python
 # this program will create a quiz file with questions and answers
 # and save it to a file the user can also load an existing quiz file 
 
 # first is initialize the GUI
import tkinter as tk 
from tkinter import messagebox

# create a window with fields for:
class QuizQuestion:
    """Represents a quiz question with multiple answers and the correct answer."""
    def __init__(self, question, answer_a, answer_b, answer_c, answer_d, correct_answer):
        self.question = question.strip()
        self.answer_a = answer_a.strip()
        self.answer_b = answer_b.strip()
        self.answer_c = answer_c.strip()
        self.answer_d = answer_d.strip()
        self.correct_answer = correct_answer.lower().strip()

    def is_valid(self):
        """Validate that all fields are filled and correct answer is valid."""
        if not all([self.question, self.answer_a, self.answer_b, self.answer_c, self.answer_d]):
            return False
        if self.correct_answer not in ['a', 'b', 'c', 'd']:
            return False
        return True

    def format_for_file(self):
        """Format the question and answers for saving to a file."""
        return (
            f"Question: {self.question}\n"
            f"A: {self.answer_a}\n"
            f"B: {self.answer_b}\n"
            f"C: {self.answer_c}\n"
            f"D: {self.answer_d}\n"
            f"Correct Answer: {self.correct_answer}\n\n"
        )
    
class QuizCreatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Creator 6969")

        self.file_handler = QuizFileHandler()

        self._create_widgets()

        