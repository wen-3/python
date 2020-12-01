# 定義基礎類別
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

# 定義衍生類別
class Customer(Person):
    def __init__(self, name, age, mail, tel):   # 定義衍生類別的建構子
        super().__init__(name, age)   # 為了將基礎類別的資料屬性初始化，而呼叫基礎類別的建構子
        
        # 新增資料屬性
        self.mail = mail
        self.tel = tel

    # 新增可以覆寫基礎類別的方法
    def getName(self):
        self.name = "客戶 " + self.name
        return self.name
    
    # 新增方法
    def getMail(self):
        return self.mail
    
    def getTel(self):
        return self.tel

pr = Person("小明", 20)
print(pr.getName())

cs = Customer("小明", 20, "123@gmail.com", "0912345678")
print(cs.getName())