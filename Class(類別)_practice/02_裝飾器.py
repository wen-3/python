def deco(func):       # 外側函數接收原本的函數並把它視為引數
    def wrapper(x):
        wx = "---" + x + "---"
        return func(wx)    # 執行內部函數處理的同時，也會處理原來的函數
    return wrapper    # 外側函數會將內側函數當成傳回值返回

@deco
def printmsg(x):
    print("輸入了", x)     # 可以在函數中新增功能

str = input("請輸入訊息:")

printmsg(str)    # 呼叫函數