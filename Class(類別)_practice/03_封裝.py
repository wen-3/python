class Person:
    def __init__(self, name, gender, height, weight):
        self.name = name
        self.gender = gender
        self.__height = height
        self.__weight = weight

    def getBMI(self):
        return (self.__weight/ ((self.__height/100)**2))
p1 = Person("Peter", "male", 180.0, 75.0)
p2 = Person("Linda", "female", 160.0, 55.0)

print(round(p1.getBMI(),2))

print(p1.__height)