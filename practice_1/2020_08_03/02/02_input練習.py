# input (注意型態轉換)
# score = input("請輸入數學成績:")
# print(int(score)+10)

chinese = int(input("chinese:"))  # 86
math = int(input("math:"))   # 78
english = int(input("english:"))  # 92
sum_ = chinese + math + english
print(f"你的成績為{sum_:6.2f}")
