#Testing print statement
#print("I am begining my Formative assignment")
#1) Add homework
#2) Add exam
#3) List assignments
#4) Filter (by subject / type / month)
#5) Show summary
#0) Exit

def menu():
        Menu={1:"add_homework",2:"add_exam",3:"list_assignments",4:"filter_assignments",5:"show_summary",0:"Exit"}
        print(Menu)
        while True:
             choice= input("Enter your choice on the menu provided:")
             try:
                  valid_choice=int(choice)
                  if valid_choice==1:
                       execute=add_homework()
                  elif valid_choice==2:
                       execute=add_exam()
                  elif valid_choice==3:
                       execute=list_assignments()
                  elif valid_choice==4:
                       execute=filter_assignments()
                  elif valid_choice==5:
                       execute=show_summary()
                  else:
                       print("Program execution ended")
                       break
             except:
                  print(" Please try again.Enter a valid integer!")
             print("Your response has been recorded")

def add_homework():
        subject=input("Enter the subject:")
        title=input("Enter the assignment title:")
        score=input("Enter your score:")
        max_score=input("Enter the maximum score:")
        due_date=input("Enter the due date in the format:YYYY-MM-DD")
        homework=Homework(subject,title,score,max_score,due_date)
        tracker.add_assignments(homework)
        
def add_exam():
        subject=input("Enter the subject:")
        title=input("Enter the assignment title:")
        score=input("Enter your score:")
        max_score=input("Enter the maximum score:")
        due_date=input("Enter the due date in the format:YYYY-MM-DD")
        exam=Exam(subject,title,score,max_score,due_date)
        tracker.add_assignments(exam)

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
        self.assignments=[]

    def add_assignments(self,assignment):
         self.assignments.append(assignment)


    def list_assignments(self):
        pass

    def filter_assignments(self):
        pass
    def show_summary(self):
        pass



tracker=GradeTracker()

menu()
