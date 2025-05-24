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

    def _create_widgets(self):
        # Question
        tk.Label(self.window, text="Question:").pack(anchor="w", padx=10, pady=(10, 0))
        self.question_entry = tk.Text(self.window, height=5, width=50)
        self.question_entry.pack(padx=10)

        # Answers A-D
        self.answer_a_entry = self._create_labeled_entry("Answer A:")
        self.answer_b_entry = self._create_labeled_entry("Answer B:")
        self.answer_c_entry = self._create_labeled_entry("Answer C:")
        self.answer_d_entry = self._create_labeled_entry("Answer D:")

        # Correct answer
        self.correct_answer_entry = self._create_labeled_entry("Correct Answer (A/B/C/D):")

        # Buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        save_button = tk.Button(button_frame, text="Save Question", command=self.save_question)
        save_button.pack(side="left", padx=5)

        exit_button = tk.Button(button_frame, text="Exit", command=self.window.destroy)
        exit_button.pack(side="left", padx=5)

    def _create_labeled_entry(self, label_text):
        tk.Label(self.window, text=label_text).pack(anchor="w", padx=10, pady=(10, 0))
        entry = tk.Entry(self.window, width=50)
        entry.pack(padx=10)
        return entry

    def save_question(self):
        question = self.question_entry.get("1.0", tk.END)
        answer_a = self.answer_a_entry.get()
        answer_b = self.answer_b_entry.get()
        answer_c = self.answer_c_entry.get()
        answer_d = self.answer_d_entry.get()
        correct_answer = self.correct_answer_entry.get()

        quiz_question = QuizQuestion(question, answer_a, answer_b, answer_c, answer_d, correct_answer)

        if quiz_question.is_valid():
            try:
                self.file_handler.save_question(quiz_question)
                self._clear_fields()
                messagebox.showinfo("Success!", "Question saved successfully!")
            except Exception as e:
                messagebox.showerror("Error!", f"Failed to save question: {e}")
        else:
            messagebox.showerror("Error!", "Please fill out all fields correctly.")

    def _clear_fields(self):
        self.question_entry.delete("1.0", tk.END)
        self.answer_a_entry.delete(0, tk.END)
        self.answer_b_entry.delete(0, tk.END)
        self.answer_c_entry.delete(0, tk.END)
        self.answer_d_entry.delete(0, tk.END)
        self.correct_answer_entry.delete(0, tk.END)