# 函式 function

def hello(name,age):            #建立函數的定義
    print("hello"+ name + "你今年"+ str(age) + "歲")
    # 有時候直接打數字會造成程式上的邏輯衝突，可以用str轉換成相同資料型態
# name = input("輸入姓名:")
# age = input("今年幾歲:")
# hello(name,age)  # 呼叫函式  


def addfunction(num1,num2):
    print(num1+num2)
    return  0.1   #將函數運行完以後回報數值可以做一些進一步的運算或處理等

value = addfunction(5,6)
print(value)   