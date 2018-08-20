students = []

class Student:

	school_name = "My School"
	
	def __init__(self, name, student_id=332):
		student = {"name": name, "student_id": student_id}
		students.append(student)
	
	def __str__(self):
		return "Student " + self.name
		
	def get_name_capitalize(self):
		return self.name.capitalize()
		
		
mark = Student("Mark")
print(mark)
print(Student.school_name)