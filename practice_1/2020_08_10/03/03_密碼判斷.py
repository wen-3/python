# 1. 密碼(password)輸入判斷
# 單向式
# accurate = "1234"
# pw = input("請輸入密碼:")
# if pw == accurate:
#     print("歡迎光臨")

# 雙向式
accurate = "1234"
pw = input("請輸入密碼:")
if pw == accurate:
    print("welcome.")
else:
    print("密碼錯誤")
