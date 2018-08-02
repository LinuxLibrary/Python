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

		
class HighSchoolStudent(Student):
	school_name = "My High School"
	
	def get_school_name(self):
		return "This is a High School Student"
		
	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"
		
james = HighSchoolStudent("james")
print(james.get_name_capitalize())