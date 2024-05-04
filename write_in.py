#讀取和寫入

# open ("檔案路徑",mode = "開啟模式")
#絕對路徑  ex:C:\Users\10\Desktop\code_learning\python\test.txt
#相對路徑  test.txt

# mode = "r" 讀取
# mode = "w" 複寫
# mode = "a" 在原先資料後面寫入東西

file = open ("test.txt", mode ="r", encoding ="utf-8") #utf-8支援中文
#print(file.readlines()) #讀取每一行的資料
file.write("\n hey")
file.close() #關閉檔案避免佔用效能

with open ("test.txt", mode ="r", encoding ="utf-8") as file:
     file.write("\n 測試一下") #with會自動進行關閉動作
