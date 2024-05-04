# if 判斷句練習
#if首先要判斷資料的布林值，當所有資料都是false時，才會進入else判斷
#在資料前使用not()可以直接使資料的判斷值為false


# score = 100 
# sunny = True
#if score == 100 and not(sunny):
#   print ("waht a good day")
#else:
#   print("oh no")




#設計一個函數可以從三個數字裡挑出最大的
num1 = input("num1:")
num2 = input("num2:")
num3 = input("num3:") 
def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num1:
        print(num3)
max_num(num1,num2,num3) 

