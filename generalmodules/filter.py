
my_list = [-2, -1, 0, 1, 2]


# 基本
# filter(関数object, リテラルobject)
# イテレータを返す点に注意
my_filter = filter(lambda x: x > 0, my_list):

# filter
for ival in my_filter:
    print(ival)

# list に変換する方法
list_from_filter = list(my_filter)



# 補足：比較
# map() は各要素に処理を行う
# reduce()関数はすべての要素を一つの値に