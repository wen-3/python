# 1. 集合的操作
# 1.1 交集
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
print(math & physics)
# 1.2 聯集
print(math | physics)
# 1.3 差集
print(math - physics)
print(physics - math)
# 1.4 對稱差集
print(math ^ physics)
# 1.5 2個集合是否相等
print(math == physics)
# 1.6 2個集合是否不相等
print(math != physics)

# 2. 實例
students = {'Peter', 'Norton', 'Kevin', 'Mary', 'John',     
            'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom'}
Math = {'Peter', 'Kevin', 'Damon'}         # 數學夏令營參加人員
Physics = {'Nelson', 'Damon', 'Tom'}       # 物理夏令營參加人員

print(Math & Physics)                # 同時參加數學和物理夏令營
print(students - (Math | Physics))   # 沒有參加暑期夏令營

# 3. 集合生成式
newSet1 = { num for num in range(1, 100, 2) }
print(newSet1)

newSet2 = { num*11 for num in range(1, 10, 2) }
print(newSet2)

# 4. 實作練習
listA = [num for num in range(1, 100, 2)]
listB = [num for num in range(0, 101, 5)]
setA = set(listA)
setB = set(listB)
print(setA & setB)   # 交集
print(setA | setB)   # 聯集
print(setA - setB)   # A-B 差集
print(setB - setA)   # B-A 差集
