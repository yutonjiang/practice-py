import numpy

# 對python內的資料型態和一些基本函數進行複習
score = [1,2,3,4,5] # 小括號表示tuple(有順序序列)，中括號表示list(無順序序列)，大括號表示集合(沒有順序)
                    # tuple的元素不能更改
score.append(6) # append 可以為list加入元素
strings = ["a","b","c","d"]

{"apple":"蘋果","data":"資料"} # 字典 dictionary 由{鍵:值}組成

print(score[1:4])  # list的排列是由0開始計算

# score.extend(strings)    # extend可用於將兩個不同的list合併

score.insert(3,3.5) #insert函數需要兩個參數，前面表示插入的list中的序位，後者表示插入的值
                    #remove可以把已存在的元素從序列中移除，clear可以清空序列中的所有元素，pop是移除最後一個元素
                    #sort是把序列做有序排列(小到大)，reverse是反轉序列的順序，index可以查找某元素在序列中的序位
                    #count可以計算某元素在序列中的數量
print(score)