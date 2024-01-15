from tkinter import *
from quiz_brain import *
import time
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quizbrain:QuizBrain):
        self.window = Tk()
        self.quiz = quizbrain

        self.score = 0
        self.txt = ""
        self.image = PhotoImage(file="images/true.png")
        self.cnv = Canvas(bg="White", height=250, width=300, highlightthickness=0)
        self.cnv.grid(column=1, row=1, columnspan=2)
        self.lbl = Label(text=f"Score: {self.score}",background=THEME_COLOR,foreground="White",font=("Arial", 15))
        self.lbl.grid(column=2, row=0, pady=30)
        self.window.configure(bg=THEME_COLOR, height=400, width=340, padx=20, pady=20)
        self.window.title("Quizlerr")
        self.image1 = PhotoImage(file="images/false.png")
        self.bttn = Button(image=self.image,command= self.button1)
        self.bttn.grid(column=2,row=2,pady=60)
        self.bttn1 = Button(image=self.image1,command=self.button2)
        self.bttn1.grid(column=1,row=2)
        self.quiztxt = self.cnv.create_text(125, 150,width=250 ,text=self.txt, anchor="center", font=("Arial", 20, "italic"),
                                          fill=THEME_COLOR)
        self.next_quest()
        self.window.mainloop()





    def next_quest(self):
        self.cnv.configure(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.cnv.itemconfig(self.quiztxt, text=q_text)
        else:
            self.cnv.itemconfig(self.quiztxt, text="You've reached end of the quiz")
            self.bttn.config(state="disabled")
            self.bttn1.config(state="disabled")
    def button1(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def button2(self):
        self.give_feedback(self.quiz.check_answer("False"))



    def give_feedback(self, bool):
        if bool:
            self.cnv.config(bg="green")
        else:
            self.cnv.config(bg="red")
        self.lbl.config(text=self.quiz.score)
        self.window.after(1000, func=self.next_quest)











