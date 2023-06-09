THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()

        self.window.title("Quizzlet")

        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score:0",fg ="white", bg =THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=25)

        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="random question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial",20,"italic"))

        self.tick_image=PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick_image,highlightthickness=0,command=self.true_button)
        self.tick_button.grid(row=2,column=0)

        self.cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0,command=self.false_button)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end!")
            self.cross_button.config(state="disabled")
            self.tick_button.config(state="disabled")

    def true_button (self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
