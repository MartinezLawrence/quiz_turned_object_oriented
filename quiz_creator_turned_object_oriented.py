# quiz creator program using tkinter in python
 # this program will create a quiz file with questions and answers
 # and save it to a file the user can also load an existing quiz file 
 
 # first is initialize the GUI
import tkinter as tk 
from tkinter import messagebox

# create a window with fields for:
class QuizQuestion:
    def __init__(self, question, answer_a, answer_b, answer_c, answer_d, correct_answer):
        self.question = question.strip()
        self.answer_a = answer_a.strip()
        self.answer_b = answer_b.strip()
        self.answer_c = answer_c.strip()
        self.answer_d = answer_d.strip()
        self.correct_answer = correct_answer.lower().strip()


        # save button
        self.save_button = tk.Button(self.window, text="Save Question", command=self.save_question)
        self.save_button.pack()

        # exit button
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.pack()

    # this is where input validation occurs
    # check if all fields are filled out
    def save_question(self):
        question = self.question_entry.get("1.0", tk.END).strip()
        answer_a = self.answer_a_entry.get()
        answer_b = self.answer_b_entry.get()
        answer_c = self.answer_c_entry.get()
        answer_d = self.answer_d_entry.get()
        correct_answer = self.correct_answer_entry.get().lower()

        # check if the correct answer is one of the options
        if question and answer_a and answer_b and answer_c and answer_d and correct_answer in ['a', 'b', 'c', 'd']:
            with open("quiz_questions.txt", "a") as file:
                
                # if input is valid, save the question and answers to a file
                file.write(f"Question: {question}\n")
                file.write(f"A: {answer_a}\n")
                file.write(f"B: {answer_b}\n")
                file.write(f"C: {answer_c}\n")
                file.write(f"D: {answer_d}\n")
                file.write(f"Correct Answer: {correct_answer}\n\n")
        
            # after saving, clear all fields for the next question
            self.question_entry.delete("1.0", tk.END)
            self.answer_a_entry.delete(0, tk.END)
            self.answer_b_entry.delete(0, tk.END)
            self.answer_c_entry.delete(0, tk.END)
            self.answer_d_entry.delete(0, tk.END)
            self.correct_answer_entry.delete(0, tk.END)
 
            # after saving, display a success message to the user
            messagebox.showinfo("Success!", "Question saved successfully!")
        else:
            messagebox.showerror("Error!", "Please fill out all fields correctly.")

    # this starts tkinter's event loop
    def run(self):    
        self.window.mainloop()
     
 # this will run the program and keep it open until the user exits
if __name__ == "__main__":
    quiz_creator = QuizCreator()
    quiz_creator.run()