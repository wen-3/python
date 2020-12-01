class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Customer(Person):
    def __init__(self, name, age, mail, tel): 
        super().__init__(name, age)  
        
        self.mail = mail
        self.tel = tel

    def getName(self):
        self.name = "客戶 " + self.name
        return self.name
    
    def getMail(self):
        return self.mail
    
    def getTel(self):
        return self.tel
