# Quiz Runner
# This code is a simple quiz application that allows users to take a quiz, select answers, and view their results.

import tkinter as tk
from tkinter import messagebox

class QuizRunner:
    def __init__(self):
        # initialize the main window
        self.window = tk.Tk()
        self.window.title("QuizRunner")

        # create an input for users to enter their name
        self.name_label = tk.Label(self.window, text="Enter your name:")
        self.name_label.pack(pady=20)
        self.name_entry = tk.Entry(self.window, width=60)
        self.name_entry.pack(pady=10)

        # create start quiz button
        self.start_btn = tk.Button(self.window, text="Start Quiz", command=self.initialize_quiz)
        self.start_btn.pack(pady=20)    # display a button to start quiz
        
        # define variable to hold quiz data and state
        self.questions = []         # SET questions to an empty list
        self.current_question = 0   # SET current_question_index to 0
        self.score = 0              # SET score to 0
        self.user_answers = []      # SET user_answers_list to an empty list

    # load quiz questions from file
    def load_questions(self):
        try:
            with open("quiz_questions.txt", "r") as file:
                content = file.read().split("\n\n")
                for block in content:
                    if not block.strip():
                        continue
                    lines = [line.strip() for line in block.split("\n") if line.strip()]
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

        # if questions list is empty then display an error message and exit           
        except FileNotFoundError:
            messagebox.showerror("Error!", "Quiz questions file not found!")
            self.window.destroy()

    # get the users name from the entry box
    def initialize_quiz(self):
        self.user_name = self.name_entry.get().strip()
        if not self.user_name:
            messagebox.showerror("Error!", "Please enter your name!")
            return
        # if user name is empty then display an error message and return

        self.load_questions()  # load questions from file
        if not self.questions:
            messagebox.showerror("Error!", "No questions found!")
            self.window.destroy()
            return
        # if questions list is empty then display an error message and return

        # remove name input and start button from window
        self.name_label.pack_forget()  # hide name label
        self.name_entry.pack_forget()  # hide name entry    
        self.start_btn.pack_forget()  # hide start button

        # display the first question and options
        self.display_question()
 
    # create a function to display the current question and options
    def display_question(self):
        # make a frame for the question
        self.q_frame = tk.Frame(self.window)
        self.q_frame.pack(pady=40, padx=100)

        # display the question and options in the window from the questions
        question_text = self.questions[self.current_question]['question']
        self.question_label = tk.Label(self.q_frame, text=question_text, wraplength=500)
        self.question_label.pack(pady=10, padx=10)  

        # show the mupltiple choice options for the current question
        self.answer_var = tk.StringVar()  # variable to hold the selected answer
        answers = self.questions[self.current_question]['answers']
    
        # track if the user selects an option
        for option in ['a', 'b', 'c', 'd']:
            rb = tk.Radiobutton(
                self.q_frame, 
                text=f"{option.upper()}: {answers[option]}", 
                variable=self.answer_var, 
                value=option, 
                wraplength=400, 
                justify='left'
            )
            rb.pack(anchor='w', pady=30)  # pack the radio button to the left

        # navigation buttons for next and submit
        self.nav_frame = tk.Frame(self.window)
        self.nav_frame.pack(pady=10)

        if self.current_question < len(self.questions) - 1:
            next_btn = tk.Button(self.nav_frame, text="Next", command=self.next_question)
            next_btn.pack(side='right', padx=10)
        else:
            submit_btn = tk.Button(self.nav_frame, text="Submit", command=self.show_results)
            submit_btn.pack(side='right', padx=10)

    def next_question(self):
        # check if an answer is selected
        if not self.answer_var.get():
            messagebox.showerror("Error!", "Please select an answer!")
            return

        self.user_answers.append(self.answer_var.get())
        self.answer_var.set(None)   # reset the answer variable
        self.q_frame.destroy()      # remove the question frame
        self.nav_frame.destroy()    # remove the navigation frame
        self.current_question += 1  # move to the next question
        self.display_question()     # display the next question

    # display results
    def show_results(self):
        self.user_answers.append(self.answer_var.get())
        self.score = sum(1 for i, answer in enumerate(self.questions) 
                        if self.user_answers[i] == answer['correct'])

        # save results
        with open("quiz_score.txt", "a") as file:
            file.write(f"Name: {self.user_name}\n")
            file.write(f"Score: {self.score}/{len(self.questions)}\n")
            for i, answer in enumerate(self.questions):
                file.write(f"Q{i+1}: {answer['question']}\n")
                file.write(f"Your Answer: {self.user_answers[i].upper()}\n")
                file.write(f"Correct Answer: {answer['correct'].upper()}\n\n")
            file.write("-"*50 + "\n")

        # display the score and a message to the user
        messagebox.showinfo("Results", 
            f"Thank you, {self.user_name}!\nYour score: {self.score}/{len(self.questions)}")
        self.window.destroy()   # close the window

            
    def run(self):
        self.window.mainloop()

# run the quiz application
if __name__ == "__main__":  
    app = QuizRunner()
    app.run()

# END OF CODE
