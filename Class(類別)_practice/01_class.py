class Person:
    count = 0   # 類別變數

    def __init__(self, name, age):    # 建構式-建立實體物件時，會被呼叫
        Person.count = Person.count + 1   # 類別變數 count會增加 1
        
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    @classmethod   # 類別方法
    def getCount(num):
        return num.count

# 建立多個實體物件，並將值指定給資料屬性
pr1 = Person("小明", 20)
pr2 = Person("張三", 35)

# 呼叫實體方法
print(pr1.getName(), pr1.getAge(), "歲")
print(pr2.getName(), pr2.getAge(), "歲")

# 呼叫類別方法
print("合計人數為:", Person.getCount(), "人")