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
                       execute=tracker.list_assignments()
                  elif valid_choice==4:
                       execute=tracker.filter_assignments()
                  elif valid_choice==5:
                       execute=tracker.show_summary()
                  else:
                       print("Program execution ended")
                       break
             except:
                  print(" Please try again.Enter a valid integer!")

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
        len_list=len(self.assignments)
        if len_list>0:
             for assignment in self.assignments:
                  print(assignment)
        else:
             print("No assignments recorded. Select from the menu to add them")

    def filter_assignments(self):
        options={1:"by type",2:"by subject",3:"by date"}
        print(options)
        option=input("Enter your filter criteria from the options provided:")
        
        try:
            valid_option=int(option)
            if valid_option ==1:
              required_type=input("Please enter 1 for homeworks or 2 for exams:")
              try:
                   valid_type=int(required_type)
                   if valid_type==1:
                        for assignment in self.assignments:
                             if assignment.type=="homework":
                                  print(assignment)
                   if valid_type==2:
                        for assignment in self.assignments:
                             if assignment.type=="exam":
                                  print(assignment)
              except:
                   print("Please enter a valid option")
            elif valid_option==2:
                 required_subject=input("Please enter your preferred subject:")
                 try:
                      valid_subject=str(required_subject)
                      for assignment in self.assignments:
                           if assignment.subject==valid_subject:
                                print(assignment)
                 except:
                      print("Please enter a valid subject")
              
            elif valid_option==3:
                 required_month=input("Enter your preferred month:")
                 try:
                      valid_month=int(required_month)
                      for assignment in self.assignments:
                           month=assignment.due_date[4:6]
                           int_month=int(month)
                           if int_month==valid_month:
                                print(assignment)
                 except:
                      print("Enter a valid month")
                       
        except:
             print("Enter a valid option ")

    def show_summary(self):
         if len(self.assignments)>0:
              total_marks_scored=0
              maximum_marks=0
              highest=self.assignments[0]
              lowest=self.assignments[0]
              subject_scores={}
              for assignment in self.assignments:
                   total_marks_scored=total_marks_scored+assignment.score
                   maximum_marks=maximum_marks+assignment.max_score
                   average_score=total_marks_scored/maximum_marks*100

                   pct = assignment.score / assignment.max_score
                   old_score, old_max = subject_scores.get(assignment.subject, (0, 0))
                   subject_scores[assignment.subject] = (old_score + assignment.score, old_max + assignment.max_score)

                   if pct > (highest.score / highest.max_score):
                    highest = assignment
                   if pct < (lowest.score / lowest.max_score):
                    lowest = assignment
              average_score = total_marks_scored / maximum_marks * 100
              print(f"Overall Average: {average_score:.2f}%")

              print("Per-Subject Averages:")
              for subject, totals in subject_scores.items():
                  subject_avg = totals[0] / totals[1] * 100
                  print(f"  {subject.title()}: {subject_avg:.2f}%")

              print(f"Highest: {highest}")
              print(f"Lowest: {lowest}")
              

         else:
              print("No assignment was given. Please input your assignment to view the summary of the results")

tracker=GradeTracker()
menu()
