class Parent():
    """docstring for parent"""
    def __init__(self, last_name, eye_color):
        print("Parent constructor Called")
        self.last_name=last_name
        self.eye_color=eye_color

    def show_info(self):
        print("last_name  - "+self.last_name)
        print("eye_color - "+self.eye_color)

class Child(Parent):
    """docstring for Child"""
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor Called")
        Parent.__init__(self, last_name ,eye_color)
        self.number_of_toys=number_of_toys

    def show_info(self):
        print("last_name  - "+self.last_name)
        print("eye_color - "+self.eye_color)
        print("number_of_toys - "+str(self.number_of_toys))

billy_cyrus=Parent("Cyrus","blue")
#billy_cyrus.show_info()

miley_cirus=Child("Cyrus", "blue", 5)
miley_cirus.show_info()
