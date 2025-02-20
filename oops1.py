# initiate a class
class employee: 
    # Assign attributes: special method / magic method / dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    # create method / function
    def travel(self, destination):
        print(f"employee is now travelling to {destination}")

# create and Obj / Instance of the class
sam = employee()

#printing attribute
#print(sam.id)

#calling a method
#sam.travel("kerala")

print(type(sam))