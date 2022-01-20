from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
RED = "#FFB5B5"
GREEN = "#91C483"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   width=280,
                                                   text="",
                                                   font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        self.score_label = Label(text="", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=2, row=1)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.press_false)
        self.true_button.grid(column=1, row=3)
        self.false_button.grid(column=2, row=3)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of this quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(500, self.get_next_question)