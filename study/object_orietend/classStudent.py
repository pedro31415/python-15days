from classPerson import Person

class Student(Person): 
    def __init__(self, name, age, cpf, courses):
        super().__init__(name, age, cpf)
        self.courses = courses

    def run(self):
        print("My name is ", self.name, "and a course is ", self.courses)

student1 = Student("Pedro", 21, "00.000.000-34", "Ciência da Computação")

student1.hello()

student1.run()