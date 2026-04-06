#write 3 student record into file
import pickle
#creat class
class Student:
	def __init__(self,roll,name,mark):
		self.roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self.roll,self.name,self.mark)
#create student object
s1 = Student(1, "Rahul", 85)
s2 = Student(2, "Anita", 90)
s3 = Student(3, "Kiran", 78)

# open file in binary write mode
with open("student.dat", "wb") as f:
    # write objects into file
    pickle.dump(s1, f)
    pickle.dump(s2, f)
    pickle.dump(s3, f)
#ciose file
f.close()

print("3 student records written successfully.")