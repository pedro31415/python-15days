class Person:
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf
    
    def hello(self):
        print("Hello my name is ", self.name)


person1 = Person("Pedro", 21, "000.000.000-58")


person1.hello()
