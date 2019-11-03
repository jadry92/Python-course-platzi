class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eyes Color -"+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


#papa = Parent("suarez","brown")
#print(papa.last_name)
yo = Child("suarez", "black", 2)

print(yo.number_of_toys)
yo.show_info()
