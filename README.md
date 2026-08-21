Student Grade & Assignment Tracker

Project Overview
The Student Grade & Assignment Tracker is a Python 3 command line program for the Programming 1 Formative Project. It enables students to record their homework and exams, to list assignments that they have entered,to filter the assignments provided and to get a summary of their grades while in the same program session.

Features
•	Add homework and exam assignments.
•	Record subject, title, score, maximum score, and due date.
•	List all recorded assignments in a readable format.
•	Filter assignments by:type (homework/exam), subject or month
•	Display: overall average, per-subject averages, highest-scoring assignment and lowest-scoring assignment.
•	Handle invalid menu and filter inputs
•	Store all data in memory for the current session
How to Run
Requirements
	Python 3.x
	Git (if cloning the repository)
Running the Program
1.	Clone the repository:
git clone <repository-url>
2.	Navigate to the project folder:
cd <project-folder>
3.	Run the program:
python main.py
-No external libraries are required.
 Menu Structure
1. Add homework
2. Add exam
3. List assignments
4. Filter (by subject / type / month)
5. Show summary
0. Exit

Filtering
The filter menu offers:
1. By type- user can choose homework or exam
2. By subject- user can choose their preferred subject out of the ones recorded
3. By date/month- Month filtering uses the month contained in the entered YYYY-MM-DD due date.

 Sample Interactions
 Adding an Assignment
Enter your choice on the menu provided: 1
Enter the subject: Maths
Enter the assignment title: End of semester
Enter your score: 90
Enter the maximum score: 100
Enter the due date in the format: YYYY-MM-DD
2026-08-12

Listing Assignments
Enter your choice on the menu provided: 3
[HOMEWORK] Maths - End of semester | 90.0/100.0 | Due: 2026-08-12

Grade Summary

Enter your choice on the menu provided: 5
Overall Average: 90.00%
Per-Subject Averages:
Maths: 90.00%
Highest: [HOMEWORK] Maths - End of semester | 90.0/100.0 | Due: 2026-08-12
Lowest: [HOMEWORK] Maths - End of semester | 90.0/100.0 | Due: 2026-08-12

Program Design
The program applies Object-Oriented Programming (OOP) and uses inheritance.
•	Assignment – Base class containing the common attributes: subject, title, score, max_score, due_date and type.
•	Homework – Subclass of Assignment that automatically sets the assignment type to homework.
•	Exam – Subclass of Assignment that automatically sets the assignment type to exam.
•	GradeTracker – Manages the assignment collection and provides methods for adding, listing, filtering, and summarizing assignments.
The project also uses functions, conditionals, loops, lists, dictionaries, exception handling, and string formatting to implement the required functionality
 Data Storage
Throughout the running of the program, all the assignments are kept in a list within the `GradeTracker` object. No files or databases are used. All data is erased at the end of a session as required, when the program ends.

 Project Structure
Grade-Tracker/
│
├── main.py
└── README.md

Screenshots
Also included in the repository are screenshots showing the functionality required of the programme:
1. Adding an assignment
2. Listing assignments
3. Filtering assignments
4. Reading the Grade Summary
