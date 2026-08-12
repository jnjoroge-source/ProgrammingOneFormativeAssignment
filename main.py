#Testing print statement
#print("I am begining my Formative assignment")
#1) Add homework
#2) Add exam
#3) List assignments
#4) Filter (by subject / type / month)
#5) Show summary
#0) Exit

class Assignment:
    def __init__(self, subject, title, score, max_score, due_date, type):
        self.subject=subject.lower().strip()
        self.title=title
        self.score=float(score)
        self.max_score=float(max_score)
        self.due_date=due_date
        self.type=type
    def __str__(self):
        return f"[{self.type.upper()}] {self.subject.title()} - {self.title} | {self.score}/{self.max_score} | Due: {self.due_date}"

class Homework(Assignment):
    def __init__(self,subject,title,score,max_score,due_date):
        super().__init__(subject,title,score,max_score,due_date,"homework")
    

class Exam(Assignment):
    def __init__(self,subject,title,score,max_score,due_date):
        super().__init__(subject,title,score,max_score,due_date,"exam")

class GradeTracker:
    def __init__(self):
        pass

#homework=Assignment( "Maths","Targeter End Term 2 Exam",80,100, 20260816,"Homework")
#print(homework)
hw=Homework("English","End Term 3 Exam",75,100,20260831)
print(hw)