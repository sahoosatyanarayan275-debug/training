class Parent:
    def parent_info(self):
        print("This is the Parent Class")
class Child(Parent):
    def child_info(self):
        print("This is the Child Class")
class Engineering(Child):
    def eng_info(self):
        print("I am studying Engineering")
obj = Engineering()
obj.parent_info()
obj.child_info()
obj.eng_info()
		
		