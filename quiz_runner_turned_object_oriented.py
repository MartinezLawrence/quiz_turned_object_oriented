# Quiz Runner
# This code is a simple quiz application that allows users to take a quiz, select answers, and view their results.

import tkinter as tk
from tkinter import messagebox

class QuizDataLoader:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        self.questions = []