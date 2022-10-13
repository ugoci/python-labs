# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class DoctorsForm:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def visit(self):
        print(f"{self.name} the doctor will see you now")
        self.name = "visit" + self.name

jon = DoctorsForm("Jon", 35, 90, 5.8)
barry = DoctorsForm("Barry", 28, 80, 6.1)

print(jon.name)
print(jon.age)
jon.visit()
barry.visit()
