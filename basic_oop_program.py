"""
Basic OOP Program
"""
class Student:
  
    school_name = "Laxmi International School"

    
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        self.marks = []

    
    def add_mark(self, score):
        self.marks.append(score)

  
    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    
    def display_info(self):
        avg = self.calculate_average()
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")
        print(f"Average Marks: {avg:.2f}")
        print("-" * 30)

if __name__ == "__main__":
  
    student1 = Student("Rahul Agrawal", 3, "10th")
    student2 = Student("Keshav Jha", 2, "10th")

    # Adding marks for student 1
    student1.add_mark(85)
    student1.add_mark(90)
    student1.add_mark(78)

    # Adding marks for student 2
    student2.add_mark(92)
    student2.add_mark(88)
    student2.add_mark(95)

   
    print("--- Student Details ---\n")
    student1.display_info()
    student2.display_info()

"""
--> Output

Name: Rahul Agrawal
Roll No: 3
Grade: 10th
School: Laxmi International School
Average Marks: 84.33

Name: Keshav Jha
Roll No: 4
Grade: 10th
School: Laxmi International School
Average Marks: 91.67
"""