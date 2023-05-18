"""
目录：
1.数据容器入门
2.数据容器：list(列表)
3.list(列表) 的遍历
4.数据容器：tuple(元组)
5.数据容器：str(字符串)
6.数据容器的切片
7.数据容器：set(集合)
8.数据容器：dict(字典、映射)
8.5拓展：数据容器的总结
9.数据容器的通用操作
10.列表推导式、生成器表达式
11.序列的解包
"""








## 1.数据容器入门

# Py中数据容器：
#   一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
#   每一个元素可以是任意类型的数据，如字符串、数字、布尔等


# 数据容器根据特点的不同，如：
#   是否支持重复元素
#   是否可修改
#   是否有序等
# 分为5类，分别是：
# 列表(list)、元组(tuple)、字符串(str)、集合(set)、字典(dict)










## 2.数据容器：list(列表)
### (1)列表的定义
### (2)列表的下标索引
### (3)列表的常用操作



### (1)列表的定义

# 列表内的每一个数据，称之为元素
#   以 [] 作为标识
#   列表内每一个元素之间用,逗号隔开
#
# 列表可以一次存储多个元素，且元素可以为不同的数据类型，支持嵌套(列表里存列表)

# # 定义格式：
#
# # 字面量
# # [元素1, 元素2, 元素3,....]
#
# # 定义变量
# # 变量名称 = [元素1, 元素2, 元素3,....]
#
# # 定义空列表
# # 变量名称 = []
# # 变量名称 = list()




# name_list = ['haha', 'hihi', '114514']
# print(name_list)    # ['haha', 'hihi', '114514']
# print(type(name_list))  # <class 'list'>

# # 列表中，存储的元素类型可以是不同的数据类型
# my_list = ['114', 514, True, [1,'A']]
# print(my_list)  # ['114', 514, True, [1, 'A']]
# print(type(my_list))  # <class 'list'>








### (2)列表的下标索引

#####
# 列表的下标：从0开始
#（与C语言不同的是:列表下标可以为负，如-1代表最后一个元素下标）
# 按照下标索引，即可取得对应位置的元素
# 注：无论正负，列表下标越界引用会报错

# 格式：
# 列表[下标]



#####
# 列表元素下标可以为负 (无论正负，【下标 % 元素个数 = 从0开始的下标】)
# 列表：[元素1, 元素2, 元素3, 元素4, 元素5]
# 下标：  0      1     2     3     4
#       -5     -4    -3    -2    -1
#
## n个元素的列表，下标允许取的范围是[-n, n-1]
## 列表[下标]，从前向后，从0开始，每次+1； 从后向前，从-1开始，每次-1


# list_1 = [1,2,3,4]
# print(list_1[-2])  # 3



#####
# 如果是嵌套列表，那如何下标索引？
# 如下列表
# 列表 = [['a', 'b'], ['c', 'd']]
# 列表[0] 为 ['a', 'b'] ; 列表[1] 为 ['c', 'd']
# 'a'==列表[0][0] , 'b'==列表[0][1] , 'c'==列表[1][0] , 'd'==列表[1][1]


# list_1 = [['a','b'], ['c','d']]
# print(list_1[0][0])  # 'a'








### (3)列表的常用操作

# 列表还提供以下种种【方法】：
#   插入元素
#   删除元素
#   清空列表
#   修改元素
#   统计元素个数
#   等

# 回忆：函数是一个封装的代码单元，可以实现特定的功能
# 在Py中，如果将函数定义为class(类)的成员，那么函数会称之为：【方法】



# def add(x, y):  # 定义函数
#     return x + y
#
# class Num:
#     def add(self, x, y):  # 定义方法
#         return x + y
#
# num = add(1, 2)  # 函数的调用
#
# num1 = Num() # 定义对象
# num = num1.num(1,2)  # 方法的调用
#
#
# 【函数】与【方法】 功能相同，定义的位置不同，调用时格式不同





## (1)查询某元素的下标(方法) -- index

# 功能：查找指定元素在列表中第一个匹配项的下标，如果找不到，报错ValueError
# 语法: 列表.index(元素)
# 返回值为int型，若元素重复，返回从左到右第一个匹配相
# index 英文： n.索引、注释、指针
# index就是列表对象(变量)的内置方法


# num = [1, '2', 3, [4], (5, ), 6, "7", 8, 9]
# x = num.index(6)
# print(x)  # 5
# print(type(x))  # <class 'int'>

# # 若元素重复，返回第一个匹配项
# num1 = [1,2,3,2]
# print(num1.index(2))  # 1





## (2)修改特定下标的元素值：

# 语法：列表[下标] = 值
# 可用上面语法，直接对指定下标(正向、反向下标均可)的值进行重新赋值(修改)
# 本质上就是赋新值覆盖旧值


# num = [1, 2, 3]
# num[1] = 5
# print(num)  # [1, 5, 3]





## (3)插入元素(方法) -- insert

# 插入元素
# 语法：列表.insert(下标，元素)
# 在指定的下标位置，插入新元素，插入位置以后的元素都被往后顶一格
# insert 英文： v.插入、嵌入  n.插入物


# abc = ['114', 514, '810']
# abc.insert(2, 1919)
# print(abc)  # ['114', 514, 1919, '810']





## (4)追加一个元素(方法) -- append

# 追加一个元素
# 语法：列表.append(元素)
# 将指定元素追加到列表的尾部
# 【注意】：append仅在尾部追加一个元素，若追加的元素为列表，也是将最后一个元素追加为嵌套的列表，而不是拼接两个列表
# append 英文： v.附加、增补


# num = [1, 2, 3]
# num.append(4)
# print(num)  # [1, 2, 3, 4]
#
# my_list = [1, 2, 3]
# my_list.append([4, 5, 6])
# print(my_list)  # [1, 2, 3, [4, 5, 6]]





## (5)列表延申(方法) -- extend

# 列表延申
# 语法：列表.extend(其他数据容器)
# 将其他数据容器的内容取出，依次追加到列表尾部
# 【注意】但凡是序列都可进行extend追加操作，列表、元组、字符串都可以拼接到列表后面。
# extend 英文： v.延申、扩大、延长


# num1 = [1, 2, 3]
# num2 = ['4', '5', '6']
# num1.extend(num2)
# print(num1)  # [1, 2, 3, '4', '5', '6']
# print(num2)  # ['4', '5', '6']

# list_num = [1, 2, 3]
# tuple_num = ('1', '2', '3')
# list_num.extend(tuple_num)  # 注意：extend可以将任意类型序列中元素追加到列表后面
# print(list_num)  # [1, 2, 3, '1', '2', '3']





## (6)删除指定下标元素的两种语法 -- del 与 pop方法

# 语法1：del 列表[下标]
# 语法2：列表.pop(下标)

# del仅能做到将指定下标元素删除
# pop方法能将指定下标的元素删除，并且返回删除的元素，默认下标-1
# pop 英文： v.弹出、伸出 （表示弹出列表中元素并接收返回值）


# num = [1, 2, 3, 4]
# del num[3]
# print(num)  # [1, 2, 3]
# x = num.pop(2)
# print(num)  # [1, 2]
# print(f"pop取出的元素为{x}")





## (7)删除指定内容的元素(方法) -- remove

# 语法：列表.remove(元素)
# 功能：从前到后搜索这个元素，找到的第一个元素被删掉


# num = [1, 3, 2, 3]
# num.remove(3)
# print(num)  # [1, 2, 3]





## (8)清空列表内容(方法) -- clear

# 语法：列表.clear()


# num = [1, 2, 3]
# num.clear()
# print(num)  # []





## (9)统计某元素在列表内的数量(方法) -- count

# 语法：列表.count(元素)
# 返回int类型
# count 英文： v.数数、计数  n.计算、总数


# num = [1, 1, 4, 5, 1, 4]
# x = num.count(1)
# print(x)  # 3
# print(type(x))  # <class 'int'>





## (10)统计列表中元素个数 -- len

# 统计列表内，有多少个元素
# 语法：len(列表)
# 返回int类型


# num = [1, 2, 3, 4, 5]
# print(len(num))  # 5





## (11)列表排序 -- sort()

# 功能：以key为依据对列表进行排序操作
# 语法：列表.sort(key=选择排序依据的函数, reverse=True|False)
#      参数key：函数key作为列表的排序依据；接受一个函数（或一个lambda匿名函数），该函数【接受一个列表项】并【返回一个用于排序的键】。例如，如果想按字符串长度降序对列表进行排序，可以使用key=len
#      参数reverse：是否反转排序结果，默认升序
#
# 注意：sort方法改变列表自身内容，无返回值（None）


# my_list = [['a',33], ['b', 55], ['c', 11]]
# # key的函数通常是lambda匿名函数
# my_list.sort(key=lambda element:element[1], reverse=False)
# print(my_list)  # [['c', 11], ['a', 33], ['b', 55]]








# 列表的方法总结
# ——————————————————————————————————————————————————————————————————————————————————————————————————————
# 序号 |   使用方式                          |          作用
#  1  | 列表.index(元素)                    |  查找元素，查找指定元素在列表的下标，如果找不到，报错ValueError
#  2  | 列表[下标] = 值                     |  修改特定下标的元素值
#  3  | 列表.insert(下标，元素)              |  插入元素，在指定的下标位置，插入新元素，插入位置以后的元素都被往后顶一格
#  4  | 列表.append(元素)                   |  元素追加，将一个元素追加到列表尾部
#  5  | 列表.extend(其他数据容器)             | 列表延申，将其他数据容器的内容取出，依次追加到列表尾部
#  6  | del 列表[下标]                      | 删除指定下标的元素
#  7  | 列表.pop(下标)                      | 删除指定下标的元素，并且返回删除的元素，默认下标-1
#  8  | 列表.remove(元素)                   | 删除指定内容的元素，从前到后搜索这个元素，找到的第一个元素被删掉
#  9  | 列表.clear()                       | 清空列表的内容
#  10 | 列表.count(元素)                    | 统计某元素在列表内的数量
#  11 | len(列表)                          | 统计列表中元素个数
#  12 | sort(key=排序依据, reverse=False)   | 以key为依据对列表进行排序
# ——————————————————————————————————————————————————————————————————————————————————————————————————————





# 练习：有一个列表，内容为[21, 25, 21, 23, 22, 20]记录一批学生年龄
# 1.定义这个列表，并用变量接收它
# 2.追加一个数字31，到列表的尾部
# 3.追加一个新列表[29, 33, 30]，到列表尾部
# 4.取出第一个元素 21
# 5.取出最后一个元素 30
# 6.查找元素31的下标位置

# age = [21, 25, 21, 23, 22, 20]
# age.append(31)
# age.extend([29, 33, 30])
# print(age)
# print(age[0])
# print(age[-1])  # 或者 age[len(age)-1]
# print(age.index(31))












## 3.list(列表) 的遍历

# 遍历、迭代：将容器内元素依次取出进行处理的行为
# 我们可以用 while、for 循环来遍历列表


# # while循环：
#
# index = 0
# while index < len(列表):
#     元素 = 列表[index]
#     对元素进行处理
#     index += 1


# # for循环：
#
# for 临时变量 in 列表:
#     对临时变量进行处理



# # 练习：用while、for两种循环将 [1, 2, 3, 4, 5, 6, 7, 8, 9]的奇偶数分别存入两个新列表
#
# def list_while(list):
#     index = 0
#     new_list = []
#     while index < len(num):
#         if list[index] % 2:  # 奇
#             new_list.append(list[index])
#         index += 1
#     return new_list
#
# def lest_for(list):
#     new_list = []
#     for element in list:
#         if not(element % 2):  # 偶
#             new_list.append(element)
#     return new_list
#
#
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list1 = list_while(num)
# list2 = lest_for(num)
# print(list1,'\n',list2)  # [1, 3, 5, 7, 9] 和  [2, 4, 6, 8]
















## 4.数据容器：tuple(元组)
### (1)元组的定义格式
### (2)元组的常见操作
### (3)元组元素的修改问题



### (1)元组的定义格式及特点

## 元组 -- tuple
# 列表是可以修改的，如果想传递信息，不被篡改，列表就不合适了
# 【元组】同列表一样，都是可以封装多个、不同类型的元素在内
# 【元组：一旦定义完成，就不可修改】
# 元组支持下标索引


## 元组的定义：使用小括号()，且用逗号隔开各个数据
#
## 定义元组字面量:
## (元素1, 元素2,...)
#
## 定义元组变量：
## 变量名称 = (元素1, 元素2,...)
#
## 定义空元组：
## 变量名称 = ()       # 方式1
## 变量名称 = tuple()  # 方式2 （得到了一个元组的类对象）
#
#
## 【特别注意】
## 若定义1个元素的元组，必须在元素后面加【逗号,】
## 否则()不会被认为是元组的标志，而是被识别为普通括号
## 变量名称 = (元素, )
## 如  t = ('hello', )
#
#
## 元组支持【元组嵌套】,可通过下标索引取出内容
## t = ((1, 2), (3, 4))
## 对嵌套元组下标索引和列表一样



# # 定义元组
# t1 = (1, 'hi', True)
# t2 = ()
# t3 = tuple()
# print(t1)  # (1, 'hi', True)
# print(t2,t3)  # () ()
# print(type(t1))  # <class 'tuple'>


# # 单个元素的元组定义
# # 加逗号
# t = ('hello', )
# print(f"t变量类型为{type(t)},值为{t}")  # t变量类型为<class 'tuple'>,值为('hello',)
# # 不加逗号
# t0 = ('hello')
# print(f"t变量类型为{type(t0)},值为{t0}")  # t变量类型为<class 'str'>,值为hello


# # 元组的嵌套
# t4 = ((1, 2, 3), (4, 5, 6))
# print(t4)  # ((1, 2, 3), (4, 5, 6))
# print(t4[1][2])  # 6









### (2)元组的常见操作

# 元组的常见方法(和列表相同，但是由于元组不可修改，所以不能增删改等)
# ————————————————————————————————————————————————————————————————————————————————————
# 序号 |   使用方式               |          作用
#  1  | 元组.index(元素)         |  查找元素，查找指定元素在元组中第一个匹配项的下标，找不到则报错
#  2  | 元组.count(元素)         |  统计某元素在元组内的出现次数数量
#  3  | len(元组)               |  统计元组中元素个数
# ————————————————————————————————————————————————————————————————————————————————————



## (0)下标索引去取出内容
# 元组的下标索引与列表用法相同
# num = (1,2,3)
# print(num[1])  # 2
# num1 = (1,2,(3,4),'5')
# print(num1[3][0])  # 5


## (1)查找元素下标(方法) -- index
# num = (1, 2, 3, 4, 5)
# x = num.index(3)
# print(x)  # 2


## (2)统计元素在元组中出现的次数(方法) -- count
# num = (1, 2, 1, 3, 1)
# print(num.count(1))  # 3


## (3)获得元组中元素数量 -- len
# num = (1, 2, 3, 4, 5)
# print(len(num))



## 元组的遍历
# 分为while、for两种，与遍历列表操作一致

# def tuple_while(tuple_1):
#     index = 0
#     while index < len(tuple_1):
#         print(tuple_1[index], end = ' ')
#         index += 1
#
# def touple_for(tuple_1):
#     for element in tuple_1:
#         print(element, end=' ')
#
# num = (1, 2, 3, 4, 5)
# tuple_while(num)
# print()
# touple_for(num)








### (3)元组元素的修改问题
## 不可修改内容(特例：可以修改【内部list的内部元素】)


## 元组元素不可修改
# num = (1, 2, 3)
# num[0] = 5  #报错


## 但是存在特例：即元组中有list类型的元素
## 可以修改元组内的list的内容(增删查改反转等)
## 元组的元素是不可以修改的，【list不能变，但是list内部的内容可变】；如不能通过引索直接该改变list，但可以通过两次引索找到list内部的元素，对其赋值


# num = (1, 2, [3, 4, 5])
#
# # 不可以直接对list赋值
# # num[2] = ['1', '2']  #报错#【注意】：元组内不允许将索引直接赋值，即使是list也不行
#
# num[2][0] = '123'  # 可以通过引索找到list内部元素赋值
# print(num)  # (1, 2, ['123', 4, 5])
#
# num[2].append('qwe')  # 可以使用方法改变list内部元素
# num[2].remove(4)
# num[2].extend(['s', 'd'])
# print(num)  # (1, 2, ['123', 5, 'qwe', 's', 'd'])







### 练习：定义一个元组，内容是:('bob', 11, ['football', 'music'])，记录的是一个学生的信息(姓名、年龄、爱好)
# 1.查询其年龄所在的下标
# 2.查询学生的姓名
# 3.删除爱好中的football
# 4.增加爱好coding到lint中


# student = ('bob', 11, ['football', 'music'])
# print(student.index(11))
# print(student[0])
# student[2].remove('football')
# student[2].append('coding')
# print(student)
















## 5.数据容器：str(字符串)

# 字符串是字符的容器，一个字符串可以存放任意数量的字符(字符串不可修改)
# 和其他容器如：列表、元组一样，字符串也可以通过下标进行访问
#   从前向后，从0开始递增
#   从后向前，从-1开始递减

# # 字符串的下标索引
# str1 = '12345'
# print(str1[2])   # 3
# print(str1[-3])  # 3




# 同元组一样，字符串是一个：【不可修改】的数据容器。
# 所以不能对一个字符串增删改

# str2 = 'hello'
# str2[1] = 'H'  # 报错 #字符串内部不支持修改








###  字符串的常用操作


## (1)寻找特定字符串的下标索引值 -- index
# 语法：字符串.index(字符串)
# 用法与列表、元组中的index基本相同，但是字符串中index可以寻找子串的位置
# 若用来查找子串，则返回子串的【首元素下标】


# str2 = 'hello'
# print(str2.index('l'))  # l (返回第一个相同值的下标)
#
# str3 = 'A and B'
# print(str3.index('and'))  # 2 (返回子串的首元素下标)






## (2)字符串的替换 -- replace
# 语法：字符串.replace(字符串1, 字符串2)
# 功能：将字符串内的【全部】字符串1，都替换为字符串2
# 注意：不是修改字符串本身（字符串不可修改），而是返回一个新的字符串来存储修改后的新字符串


# str4 = 'haha ABC ha'
# new_str4 = str4.replace('ha','69')
# print(f"{str4} 替换后变为 {new_str4}")  # haha ABC ha 替换后变为 6969 ABC 69
# # replace操作保持旧字符串不变的同时，将全部子字符串1改变为字符串2存入新字符串，返回新的字符串






## (3)字符串的分割 -- split
# 语法：字符串.split(分隔符字符串)
# 功能：按照指定的分隔字符串，将字符串划分为多个字符串，并存入列表对象中
# split 英文  v.分裂、分开  n.裂口、分裂
# 注意：字符串本身不变，而是得到了一个列表对象


# str5 = '1 2 3 4 5'
# list_str5 = str5.split(' ') # 以空格为分隔符
# print(f'{str5} 被分割为 {list_str5}')  # 1 2 3 4 5 被分割为 ['1', '2', '3', '4', '5']
# # split操作保留原有字符串的同时，将以分隔符划分出来的新字符串存入列表中，并返回列表
#
# str6 = 'hahaandheheandhihi'
# list_str6 = str6.split('and')  # 分隔符可以是多个字符
# print(list_str6)  # ['haha', 'hehe', 'hihi']






## (4)字符串的规整操作 -- strip
# 语法：字符串.strip(首尾字符串)
# 功能：(1.传参数)删除字符串首尾的【所有】与【括号内字符串中单个字符】相同的字符
#      (2.不传参数)删除字符串首位的空格和回车
# strip 英文  v.除去、夺去
#
# 如对字符串 '123213321a123b123c332121' 进行strip操作，返回 'a123b123c'
#    注意：串如的'123'其实就是：'1' '2' '3'都会移除，是按照单个字符
#
# 【注意】：若字符串.strip()，括号内为空
#         则去掉字符串前后的所有空格、回车


# # 用法：字符串.strip()
# str7 = '    abc '
# print(str7.strip())  # abc
#
#
# # 用法：字符串.strip(首尾字符串)
# str8 = '123abc123'
# str9 = '2131232a123b123c312313123'
# print(str8.strip('123'))  # abc
# print(str9.strip('123'))  # a123b123c






## (5)统计字符串中某字符串的出现次数 -- count
# 语法：字符串.count(字符串)
# 用法与列表、元组中的count基本相同，但是字符串中count可以统计子串的数量

# str10 = 'haha123haha12ha'
# print(str10.count('ha'))  # 5





## (6)统计字符串的长度 -- len
# 语法：len(字符串)
# 用法与列表、元组中的count相同

# str11 = '123456789'
# print(len(str11))  # 9



# 字符串的常用操作汇总(与其他序列的区别在于：字符串操纵方法一般可以操纵【子串】，而非单个元素)
# ————————————————————————————————————————————————————————————————————————————————————
# 序号 |   使用方式                      |          作用
#  1  | 字符串.index(字符串)             |  根据下标索引取出特定位置字符串
#  2  | 字符串.replace(字符串1, 字符串2)  |  将字符串内的全部子串1，都替换为字符串2（不会修改原串，而是返回新字符串）
#  3  | 字符串.split(分隔符字符串)        |  按照指定的分隔字符串，将字符串划分为多个字符串，存入列表对象中，并返回列表
#  4  | 字符串.strip(首尾字符串)          |  删除字符串首尾的所有指定字符
#     | 字符串.strip()                  |  删除字符串首尾空格和换行符
#  5  | 字符串.count(子串)                |  统计某子串在字符串内的出现次数
#  6  | len(字符串)                      |  统计字符串中元素个数
# ————————————————————————————————————————————————————————————————————————————————————






## 练习：给定一个字符串"abc123 abcqwe abcdef"
# 统计字符串内有多少个"abc"
# 将字符串内的空格全部替换为"|"
# 按照"|"进行字符分割，得到列表

# str1 = "abc123 abcqwe abcdef"
# print(str1.count("abc"))  # 3
# new_str1 = str1.replace(" ", "|")
# print(new_str1)  # abc123|abcqwe|abcdef
# list_str1 = str1.split("|")
# print(list_str1)  # ['abc123 abcqwe abcdef']
















## 6.数据容器的切片


### (1)什么是序列

# 【序列】是指：内容连续、有序、可使用下标索引的一类数据容器
# 【列表】【元组】【字符串】，均可以视为序列。



### (2)序列的切片操作

# 【切片】：从一个序列中，取出一个子序列
# 切片 - [start, end, step]，左闭右开
# 切片的使用场景如下：
#   【截取操作】：我们可以通过切片截取并获得指定的子序列，这种操作不改变原序列,list、tuple、str都可使用
#   【赋值操作】：对切片划定的空间进行赋值覆盖，从而实现增、删、替换，这种操作改变原序列，只可对可变序列list进行操作


# 语法：序列[起始下标:结束下标:步长]  -- （左闭右开）
# 可以类比 range(num1,num2,step)

# 功能：在序列中，从起始位置开始，依次取出元素，直到结束位置停止【不含结束下标本身】，得到一个新序列
#   ·起始下标可以留空，留空视作从头开始
#   ·结束下标(不含)，可以留空，视作截取到结尾(留空包含结尾)
#   ·步长：表示取元素的间隔，默认是1，可以省略不写
#           (步长可为负，此时起始下标与结束下标也要反向标记)
#
# 注意：切片操作不影响序列本身，而是得到一个新序列(有些序列不支持修改)



## 案例如下：
#
# # 对list进行切片，步长为1
# my_list = [1, 2, 3, 4, 5, 6]
# result1 = my_list[2:5]  # 步长默认为1，可不写
# print(result1)  # [3, 4, 5]
#
#
# # 对tuple进行切片，从头到最后结束，步长为1
# my_tuple = (1, 2, 3, 4)
# result2 = my_tuple[:]  # 留空默认 从头开始/到尾结束(含)
# print(result2)  # (1, 2, 3, 4)
#
#
# # 对str进行切片，步长为2
# my_str = '1234567890'
# result3 = my_str[2:8:2]
# print(result3)  # 357
#
#
# # 对str进行切片，从头到尾，步长-1
# my_str = '123456789'
# result4 = my_str[::-1]  # 这种写法默认直接反转字符串
# print(result4)  # 987654321
#
#
# # 对list进行切片，从7到2，步长-1
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result1 = my_list[7:2:-1]  # 步长为负，同样不包含结尾
# print(result1)  # [8, 7, 6, 5, 4]
#
#
# # 对tuple进行切片，从头到最后结束，步长为-2
# my_tuple = (1, 2, 3, 4)
# result2 = my_tuple[::-2]
# print(result2)  # (4, 2)



# ## 题目：从"abc 6543210 abc"中取出“12345”
#
# my_str = "abc 654321 abc"
# # 法1
# new_str = my_str[my_str.index('1'):my_str.index('6'):-1]
# print(new_str)
# # 法2
# new_str1 = my_str[::-1][4:9]  # 可以对切片的返回值继续切片
# print(new_str1)




# # 在完成上面的案例学习后，我们想要了解一些切片的用法：
# # 切片可以对序列：截取/增/删/替换
# # 学习下面的例子，我们可以发现，我们之前常用的使用切片【直接截取】序列元素，由于截取操作无序对原序列赋值，【不改变原序列的值，而是返回新的序列】，所以list、tuple、str都可以进行该操作
# #              除了截取外，我们还会进行【增、删、替换】序列元素操作，这些操作的本质都是【对切片选定的空间进行赋值覆盖操作，会改变原序列】，所以要求可变序列list
#
#
# # [1]使用切片获取序列元素
# # 注意：由于仅用切片获取元素，返回新序列，所以这种操作list、tuple、str都可以使用
#
# a = (1, 2, 3, 4, 5)
# a1 = a[::]
# print(a1)  # (1, 2, 3, 4, 5)，返回包含原本序列元素的新元组
# a2 = a[::-1]
# print(a2)  # (5, 4, 3, 2, 1)，返回逆序元组
# a3 = a[::2]
# print(a3)  # (1, 3, 5)，返回从头取得步长为2的元组
# a4 = a[1:3]
# print(a4)  # (2, 3)，返回指定下标间(左闭右开)的元组
# a5 = a[:100]
# print(a5)  # (1, 2, 3, 4, 5)，切片结束位置大于表长时，从表尾截断
# print(a)  # (1, 2, 3, 4, 5)，切片不改变原序列内容
#
#
#
# # [2]使用切片为list增加元素
# # 用切片增加元素的操作，本质是【对切片选定区域赋值】，【改变原序列内容】。
# # 由于用切片增加元素属于赋值操作，所以【只能作用于可变的序列】，即list。
# # 注意：切片可以在list的任意位置插入新元素，不影响可变序列的内存地址，属于原地操作
#
# b = [3, 5, 7]
# b[len(b):] = [9]
# print(b)  # [3, 5, 7, 9]，将3下标后(含3)位置赋值为9
# b[:0] = [1, 2]
# print(b)  # [1, 2, 3, 5, 7, 9]，将0下标前(不含0)位置赋值为[1, 2]
# b[3:3] = [4]
# print(b)  # [1, 2, 3, 4, 5, 7, 9]，将3到3(不含3)下标间区域赋值为4，实现插入操作
#
# # 从这些操作，我们可以看出，用切片操作增加元素，即对切片所选中的区域进行赋值操作。切片左闭右开至关重要
#
#
#
# # [3]使用切片替换和修改list元素
#
# c = [3, 5, 7, 9]
# c[:3] = [1, 2, 3]
# print(c)  # [1, 2, 3, 9]，将3下标前(不含3)的空间赋值为[1,2,3]
# c[3:] = [4, 5, 6]
# print(c)  # [1, 2, 3, 4, 5, 6]，将3下标后(含3)的空间赋值为[4,5,6]
# c[::2] = ['a', 'b', 'c']
# print(c)  # ['a', 2, 'b', 4, 'c', 6]，从0下标(含0)开始，隔一个赋值一个【等号两边的长度相等】
# c[1::2] = ['1', '2', '3']
# print(c)  # ['a', '1', 'b', '2', 'c', '3']，从1下标(含1)开始，隔一个赋值一个【等号两边的长度相等】
# # c[::2] = [1]
# # print(c)  # 报错，【等号两边长度不等(左右元素个数无法匹配)，直接报错】
#
# # 我们发现，替换list元素的操作，本质上还是对选定下标区域间序列进行覆盖赋值操作，不过注意，步长不为1时，记得将保证等号左右长度要相等。
#
#
#
# # [4]使用切片删除list元素
#
# d = [3, 5, 7, 9, 11]
# d[:3] = []
# print(d)  # [9, 11]，将3前空间(不含3)替换为空列表，可以删除元素
#
# d = [3, 5, 7, 9, 11]
# del d[:3]
# print(d)  # [9, 11]，我们也可以对对切片进行del操作，进行删除元素的
# d = [1, 2, 3, 4, 5, 6]
# del d[1::2]
# print(d)  # [1, 3, 5]，从1下标(含1)，隔一个删除一个，这种步长不唯一的删除只能用del删除；若直接用[]替换，左右元素不等，报错
















## 7.数据容器：set(集合)

### (1)集合的定义
### (2)集合的常用操作
### (3)集合的遍历


# 我们已经学习了一些数据容器，通过特性来分析：
#   列表可修改、支持重复元素且有序
#   元组、字符串不可修改、支持重复元素且有序
#
# 如果场景需要对内容做去重处理，列表、元组、字符串就不方便了。
# 【集合】：不支持重复元素(自带去重功能)，并且内容无序






### (1)集合的定义

# 基础语法
#
# # 定义集合字面量
# {元素1, 元素2,...}
#
#
# # 定义集合变量
# 变量名称 = {元素1, 元素2,...}
#
#
# # 定义空集合
# 变量名称 = set()


# my_set = {1,1,1,2,2,3}
# print(f"{my_set},类型为{type(my_set)}")  # {1, 2, 3},类型为<class 'set'>
# my_set_empty = set()
# print(f"{my_set_empty},类型为{type(my_set_empty)}")  # {1, 2, 3},类型为<class 'set'>
#
# # 可以看出集合不重复，且无序











### (2)集合的常用操作


# 首先，应为集合是无序的，所以集合【不支持:下标索引访问】
# 但集合和列表一样，是允许修改的，所以存在集合的修改方法。





## (1)添加新元素 -- add
# 语法：集合.add(元素)
# 功能：将指定元素，添加到集合内
# 结果：集合本身被修改，添加了新元素


# set1 = {1, '2'}
# set1.add(1)  # 自动去重
# set1.add((3, ))
# print(set1)  # {1, (3,), '2'}





## (2)移除元素 -- remove
# 语法：集合.remove(元素)
# 将相应内容的元素从集合内移除，与list中用法相同
# 结果：集合本身被修改，移除了元素


# set2 = {1, 2, 3}
# set2.remove(2)
# print(set2)  # {1, 3}





## (3)随机取出一个元素 -- pop
# 语法：集合.pop()
# 功能：从集合中随机取出一个元素，与list中用法基本相同 (由于集合不支持下标，所以没有参数，只能随机)
# 结果：集合中的一个元素被移除，并返回这个元素


# set2 = {'ha', 'he', 'hi'}
# str1 = set2.pop()
# print(f"取出元素为{str1},集合剩下元素有{set2}")  # 取出元素为ha,集合剩下元素有{'he', 'hi'}
# # 取出任意一个元素，集合中剩下另两个元素





## (4)清空集合 -- clear
# 语法：集合.clear()
# 功能：清空集合，与其他数据容器clear相同

# set2 = {1, 2, 3}
# set2.clear()
# print(set2)  # set()





## (5)取两个集合的差集 - difference
# 【差集】：集合1与集合2的差集 = 集合1 - 集合2 (集合1有而集合2没有)
# 语法：集合1.difference(集合2)
# 功能：取集合1和集合2的差集(相当于数学上的 A1-A2)
# 结果：得到一个新集合，集合1和集合2不变


# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3, 4, 6, 7}
# set3 = set1.difference(set2)
# print(set1,set2)  # 原本集合未改变
# print(set3)  # {1, 5} 取得差集





## (6)取差集并更新集合 -- difference_update
# 语法：集合1.difference_update(集合2)
# 功能：取集合1和集合2的差集，并将集合1的值更新为其差值 (无返回值)
# 结果：集合1被修改，集合2不变


# set1 = {1, 2, 3, 4}
# set1.difference_update({2,3,5,7})
# print(set1)  # {1, 4}





## (7)取两个集合的并集 -- union
# 【并集】：相当于合并两个集合 (集合1 + 集合2)
# 语法：集合1.union(集合2)
# 功能：返回集合1与集合2的并集
# 结果：得到新集合，集合1和集合2不变


# set1 = {1, 2, 3}
# set2 = {1, 4, 5}
# set3 = set1.union(set2)
# print(set1,set2)  # # 原本的集合未改变
# print(set3)  # {1, 2, 3, 4, 5}





## (8)统计集合元素数量 -- len
# 语法：len(集合)

# set1 = {1, 2, 3, 4, 5}
# print(len(set1))  # 5
# set2 = {1,2,3,3,1,2,3}  # 去重
# print(len(set2))  # 3





## (9)将一个集合的内容更新到另一个集合中 -- update
# 语法：set1.update(set2)
# 功能：将一个集合合并到另一个集合中，自动去重

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.update(set2)
# print(set1)  # {1, 2, 3, 4, 5, 6}





# 集合的常用操作
# ————————————————————————————————————————————————————————————————————————————————————————————
# 序号 |   使用方式                     |          作用
#  1  | 集合.add(元素)                 |  在集合内添加一个元素
#  2  | 集合.remove(元素)              |  移除集合中指定的元素
#  3  | 集合.pop()                    |  随机取出一个元素，即集合中的随机一个元素被移除，并返回这个元素
#  4  | 集合.clear()                  |  清空集合
#  5  | 集合1.difference(集合2)        |  返回集合1和集合2的差集
#  6  | 集合1.difference_update(集合2) |  将集合1的值更新为集合1和集合2的差集
#  7  | 集合1.union(集合2)             |  返回集合1和集合2的并集
#  8  | len(集合)                     |  统计集合元素数量
#  9  | set1.update(set2)            |  将一个集合的内容更新到另一个集合中
# ————————————————————————————————————————————————————————————————————————————————————————————








### (3)集合的遍历

# 注意：集合不支持下标索引，所以不支持while循环
# 可以用for循环

# set1 = {1, '2', 3, (4,), "5"}
# for element in set1:
#     print(f"集合的元素有{element},类型为{type(element)}")



## 练习：信息去重 - 有如下列表对象：['abc', '123', 'qwe', 'abc', 'hello', 'hi', '123']
#   定义一个空集合
#   通过for循环遍历列表
#   在for循环中将列表的元素添加至集合
#   最终得到元素去重后的集合，并打印输出

# my_list = ['abc', '123', 'qwe', 'abc', 'hello', 'hi', '123']
# set1 = set()
# for element in my_list:
#     set1.add(element)
# print(set1)
















## 8.数据容器：dict(字典、映射)

### (1)字典的定义
### (2)字典的常用操作
### (3)字典的遍历




### (1)字典(dict)的定义

# 生活中的字典，可以通过【字】找到对应的【含义】
# Python中的字典，可以通过【Key 键】找到对应的【Value 值】



# # 【字典】 - dict (dictionary缩写)
# # 字典用于储存【键值对】 - 【键(key) : 值(value)】，字典可变。
# # 字典的定义，同样使用大括号{}，不过存储的每一个元素都是【键值对】
# 如：contacts = {"小明":"114514","小花":"1919810"}
#
#
# # 定义字典字面量
# {key1:value1, key2:value2,...}
#
#
# # 定义字典变量
# my_dict = {key1:value1, key2:value2,...}
#
#
# # 定义空字典
# my_dict = {}      # 方式1
# my_dict = dict()  # 方式2



# # 定义字典
# stu_grade = {"小明":75, "小美":83, "小刚":66}
# print(type(stu_grade))  # <class 'dict'>
# print(stu_grade)  # {'小明': 75, '小美': 83, '小刚': 66}
#
# # 定义空字典
# my_drict = {}
# my_drict1 = dict()
# print(my_drict,'\t',type(my_drict))   # {} 	 <class 'dict'>
# print(my_drict1,'\t',type(my_drict))  # {} 	 <class 'dict'>






# # 生活中的字典，不会出现两个相同的字，同理：
# # 【字典的 Key键 不可以重复】
#
# stu_grade = {"小明":75, "小明":83, "小刚":66}  # 若键重复
# print(stu_grade)  # {'小明': 83, '小刚': 66}
#
# # 如上，只打印了1个'小明'，且后面的值把前面的值覆盖掉了
# # 可以看出，字典的键不能重复





# # 字典数据的获取
# # 字典同集合一样，都是【无序】的，【不可以使用下标索引】
# # 但字典可以【通过 Key键 来取得对应的 Value值】

# # 语法：字典[key]
# # 功能：可以取得键对应的值
#
# grade = {"小明":75, "小美":83, "小刚":66}
# print(grade['小明'])  # 75
# print(grade['小美'])  # 83
# print(grade['小刚'])  # 66
# print(grade['小夫'])  # 输入不存在的键，报错





# # 字典的嵌套
# # 字典的Key必须是不可变类型，如字符串、数组、浮点、元组
# # 字典的Value可以是任意类型，可以嵌套

# grade = {"小明":{'数学':55, '英语':66}, # 注意：像字典、列表等数据容器可以分成多行，因为其元素间分隔完全看逗号
#          "小美":{'数学':85, '英语':96},
#          "小刚":{'数学':65, '英语':76}}
# print(grade)
# print(grade['小明']['英语'])  # 66
# print(grade['小刚']['数学'])  # 65











### (2)字典的常用操作



## (1)新增/更新元素
# 语法：字典[Key] = Value
# 当Key为新键，则该操作代表添加新元素
# 当Key已经存在，则该操作代表更新Value的值 (字典的Key不可重复)


# my_dict = {'小明': 1,'小美': 2, '小刚': 3 }
# my_dict['小夫'] = 4
# print(my_dict)  # {'小明': 1, '小美': 2, '小刚': 3, '小夫': 4}
# my_dict['小明'] = 18
# print(my_dict)  # {'小明': 18, '小美': 2, '小刚': 3, '小夫': 4}





## (2)删除元素 -- pop
# 语法：字典.pop(Key)
# 功能：返回指定Key的Value，同时字典中指定Key的数据被删除
# 注意：对于其他数据容器，pop参数为下标，对于字典，pop参数为Key


# grade = {"小明":75, "小美":83, "小刚":66}
# score = grade.pop('小明')
# print(f'被移除的小明分数为{score}')  # 75
# print(grade)  # {'小美': 83, '小刚': 66}





## (3)清空元素 -- clear
# 语法：字典.clear()

# grade = {"小明":75, "小美":83, "小刚":66}
# grade.clear()
# print(grade)  # {}





## (4)获取全部的Key -- keys
# 语法：字典.keys()
# 功能：以列表形式返回字典中全部的Key

# grade = {"小明":75, "小美":83, "小刚":66}
# list_key = grade.keys()
# print(list_key)   # dict_keys(['小明', '小美', '小刚'])





## (5)获取全部的Value -- value
# 语法：字典.values()
# 功能：以列表形式返回字典中全部Value

# grade = {"小明":75, "小美":83, "小刚":66}
# list_value = grade.values()
# print(list_value)  # dict_values([75, 83, 66])





## (6)获取全部的键值对 -- items
# 语法：字典.items()
# 功能：将每一个键值对的Key与Value存放在一个元组中，将全部元组放入列表，之后返回这个列表
# item  n.项目  v.逐条列出

# grade = {"小明":75, "小美":83, "小刚":66}
# list_item = grade.items()
# print(list_item)  # dict_items([('小明', 75), ('小美', 83), ('小刚', 66)])





## (7)统计字典元素个数 -- len

# grade = {"小明":75, "小美":83, "小刚":66}
# print(len(grade))  # 3





## (8)获得字典键对应的值 -- get
# 语法：字典.get(键, default=None)
#   default：可选参数，如果指定的键不存在时，返回该默认值。
# 功能：get方法用于获取字典中指定键对应的值。如果该键不存在，则返回默认值（如果提供了默认值），否则返回None。

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.get('a', '该键不存在'))  # 1，返回键对应的值
# print(my_dict.get('d'))  # None，键不存在，默认返回Non
# print(my_dict.get('d', '该键不存在'))  # 该键不存在，返回我们指定的语句





# (9)将一个字典的内容更新到另一个字典中 -- update
# 语法：dict.update(dict2)
# 功能：将另一个字典的键值对一次性全添加到当前字典中。若两字典中存在相同的键，则以另一个字典中的值为准，对当前字典进行更新

# my_dict1 = {'a': 1, 'b': 2, 'c': 6}
# my_dict2 = {'c': 3, 'd': 4}
# my_dict1.update(my_dict2)
# print(my_dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}，可见，update操作将dict2的值更新到了dict1中，并覆盖同名键值对






# 字典的常用操作
# ————————————————————————————————————————————————————————————————————————————————————————————
# 序号 |   使用方式              |       作用
#  1  | 字典[Key]              |  获取Key对应的Value
#  2  | 字典[Key] = Value      |  添加或更新键值对
#  3  | 字典.pop(Key)          |  取出Key对应的Value，并再字典中删除此Key的键值对
#  4  | 字典.clear()           |  清空字典
#  5  | 字典.keys()            |  以列表形式返回字典中全部的Key
#  6  | 字典.values()          |  以列表形式返回字典中全部Value
#  7  | 字典.items()           |  将每一个键值对的Key与Value存放在一个元组中，将全部元组放入列表，之后返回这个列表
#  8  | len(字典)              |  统计字典元素个数
#  9  | get(key,default=None) |  获得键对应的值，若键不存在，返回自定义的内容，默认返回None
#  10 | dict.update(dict2)    |  将另一个字典的内容更新到指定字典中，同名键值对新覆盖旧
# ————————————————————————————————————————————————————————————————————————————————————————————











### (3)字典的遍历
# 由于字典无序，所以无法对其直接进行while循环；for循环变量接收的是键值对的Key
# 或者我们也可以通过Keys/values/items等函数来对字典进行转换后再遍历


# # 方式1：直接对字典进行for循环，每一次循环都是直接得到Key
#
# grade = {"小明":75, "小美":83, "小刚":66, '小夫':56, '小虎':72}
# for x in grade:
#     print(f'key:{x}对应value:{grade[x]}')  # key:小明对应value:75 .....



# # 方式2：通过取得的全部key来完成遍历
#
# grade = {"小明":75, "小美":83, "小刚":66, '小夫':56, '小虎':72}
# for key in grade.keys():
#     print(f'key:{key}对应value:{grade[key]}')  # key:小明对应value:75 ......



# # 方式3：通过items()直接对键值对进行遍历
# grade = {"小明":75, "小美":83, "小刚":66, '小夫':56, '小虎':72}
#
# for tuple1 in grade.items():
#     print(f'key:{tuple1[0]}对应value:{tuple1[1]}')
#
# for (key,value) in grade.items():  # 或者这种写法也对，用两个变量去接收元组的两个元素值
#     print(f'key:{key}对应value:{value}')





# ## 练习：记录员工信息(如：姓名：小明、部门：科技部、工资：3000、级别：1)
# ##      请实现基本的增删查改功能,员工信息用字典存储。


# member = {}
#
# def menu():
#     print("--------------主菜单--------------")
#     print(f"您好，欢迎来到员工系统。请选择操作：")
#     print("增加员工\t\t\t【输入1】")
#     print("删除员工\t\t\t【输入2】")
#     print("打印员工信息\t\t【输入3】")
#     print("对指定级别增加薪水\t【输入4】")
#     print("退出员工系统\t\t【输入0】")
#
# def add_fun():
#     name = input('请输入员工姓名：')
#     where = input('请输入员工部门：')
#     salary = int(input('请输入员工工资：'))
#     grade = int(input('请输入员工级别：'))
#     member[name] = {'部门':where, '工资':salary, '级别':grade}
#     print('添加成功')
#
# def del_fun():
#     name = input('请输入要删除的员工姓名：')
#     del member[name]
#     print('删除成功')
#
# def pri():
#     if len(member) == 0:
#         print('暂无员工信息')
#     for (name,information) in member.items():
#         print(f'员工{name}, {information}')
#
# def upgrade_salary():
#     grade = int(input('请输入想要加薪的员工级别：'))
#     salary = int(input('请输入增加的工资：'))
#     for name in member:
#         if member[name]['级别'] == grade:
#             member[name]['工资'] += salary
#
# while True:
#     menu()
#     num = int(input('请选择操作：'))
#     if num == 1:
#         add_fun()
#     elif num == 2:
#         del_fun()
#     elif num == 3:
#         pri()
#     elif num == 4:
#         upgrade_salary()
#     elif num == 0:
#         break
#     else:
#         print('输入无效数据，请重新输入')
#     input('按任意键继续...')
# print('系统已退出')

















### 8.5拓展：数据容器的总结

# 数据容器的分类

# 是否支持下标索引(有序)？
# 支持：列表、元组、字符串 -- 序列类型
# 不支持：集合、字典 -- 非序列类型

# 是否支持重复元素？
# 支持：列表、元组、字符串 -- 序列类型
# 不支持：集合、字典 -- 非序列类型

# 是否可以修改？
# 支持：列表、集合、字典 -- 可变
# 不支持：元组、字符串 -- 不可变



# 记忆各类数据的特点，它们的应用场景如下：
# 列表：一批数据，可修改、可重复的存储场景
# 元组：一批数据，不可修改、可重复的存储场景
# 字符串：遗传字符串的存储场景
# 集合：一批数据，去重存储场景
# 字典：一批数据，可用Key检索Value的存储场景

















## 9.数据容器的通用操作



### (1)容器的通用遍历

# 首先，在遍历上：
#   （都支持遍历）
# 5类数据容器都支持for循环遍历
# 列表、元组、字符串支持while循环；集合、字典不支持(无法下标索引)





### (2)容器的通用函数

# 数据容器可以通用非常多的功能函数或方法
# 如：len()、max()、min()等
# 注意：字符比大小，比较的是每个字符的ASCII码值
#      字典比大小，比的是Key，与Value无关；若Key是字符串，则比较字符串的大小：即对应下标字符进行逐一比较，直到一个字符与另一个不相同为止。
#      如： 'a'>'A' , 'ABD'>'ABC' , 'ABCD'>'ABC' , 'key3'>'key2'


# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# my_str = 'abcde'
# my_set = {1,2,3,4,5}
# my_dict = {'key1':None, 'key2':None, 'key3':None, 'key4':None, 'key5':None}


# 返回最大的元素 -- max()
# print(max(my_list))  # 5
# print(max(my_tuple))  # 5
# print(max(my_str))  # e
# print(max(my_set))  # 5
# print(max(my_dict))  # key5


# # 返回最大的元素 -- min()
# print(min(my_list))  # 1
# print(min(my_tuple))  # 1
# print(min(my_str))  # a
# print(min(my_set))  # 1
# print(min(my_dict))  # key1






### (3)容器的通用类型转换

# 我们还可以通用类型转换
# list(容器)
# str(容器)
# tuple(容器)
# set(容器)
# dict(容器)

# 使用字符串转换函数时，我们需要注意数据容器所包含的内容：
# 如：列表[1,2,3]，存储的数据自然是1、2、3。元组(1,2,3)、字符串"123"、集合{1,2,3}同理，这些字符串存储的内容一目了然
# 字典{1:'a',2:'b',3:'c'}存储的内容是三个键值对，但是很多情况下，仅字典的键生效，忽略值
#     如：print(list({1:'a', 2:'b', 3:'c'}))  # [1, 2, 3]，将dict转换为list后，list中仅存储着键
#
# # 字符串转换函数很特殊，str()，会将里面的全部内容转换为字符串，包括数据容器的括号[]和逗号,以及空格
# print(str([1, 2, 3]))  # [1, 2, 3]
# # 由于str()的内容全部转换的性质，导致了一个list数据，str()后，再用list()转换回来，得到的数据不同，如下：
# data = str([1, 2, 3])  # data的内容是"[1, 2, 3]"
# print(list(data))  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ']']



# 知晓了”先确定数据容器存储的内容，之后按照各自数据容器转化函数的规则去转换“这一规则后，
# 例子如下：

# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# my_str = 'abcde'
# my_set = {1,2,3,4,5}
# my_dict = {'key1':1, 'key2':2, 'key3':3, 'key4':4, 'key5':5}


# # 转列表操作
# print(list(my_tuple))  # [1, 2, 3, 4, 5]
# print(list(my_str))  # ['a', 'b', 'c', 'd', 'e']  #  【每个字符单独拆开存入列表】
# print(list(my_set))  # [1, 2, 3, 4, 5]
# print(list(my_dict))  # ['key1', 'key2', 'key3', 'key4', 'key5']  # 【将Value抛弃，只转换Key】


# # 转元组操作
# print(tuple(my_list))  # (1, 2, 3, 4, 5)
# print(tuple(my_str))  # ('a', 'b', 'c', 'd', 'e')
# print(tuple(my_set))  # (1, 2, 3, 4, 5)
# print(tuple(my_dict))  # ('key1', 'key2', 'key3', 'key4', 'key5')


# # 转字符串操作 (连括号、逗号一起【原样转换】为字符串)
# print(str(my_list))  # '[1, 2, 3, 4, 5]'
# print(str(my_tuple))  # '(1, 2, 3, 4, 5)'
# print(str(my_set))  # '{1, 2, 3, 4, 5}'
# print(str(my_dict))  # '{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}'


# # 转集合操作 (自带去重，无序)
# print(set(my_list))  # {1, 2, 3, 4, 5}
# print(set(my_tuple))  # {1, 2, 3, 4, 5}
# print(set(my_str))  # {'a', 'd', 'e', 'b', 'c'}
# print(set(my_dict))  # {'key4', 'key2', 'key3', 'key1', 'key5'}


# # 转字典操作
# dict()
# 由于字典类型元素要求键值对，但其他数据容器元素不满足，无法凭空变出一个Value来，所以转换会报错
# 【其他数据容器转字典，由于不是键值对，无法转换】
# 【字典转其他数据容器，丢失Value，只转化Key（除了str()全保留）】
#
# # 虽然其他数据容器无法直接转换为字典，但是可以右其他方法通过dict()创建字典
# print(dict(zip('1234', 'abcd')))  # {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
#
# # dict()可以将符合键值对形式的数据容器转化为字典 - 键值对形式，即(key, value)
# # dict([(key1, value1), (key2, value2), (key3, value3)])，是最好的转换写法
# print(dict([(1, 'a'), (2, 'b'), (3, 'c')]))  # {1: 'a', 2: 'b', 3: 'c'}
# print(dict(((1, 'a'), (2, 'b'), (3, 'c'))))  # {1: 'a', 2: 'b', 3: 'c'}
# 若键值对是[key, value]或{key, value}等，会报警告，最好不要写，且集合的键值对无序
#
# # 以关键字参数的形式创建列表
# print(dict(name = 'dog', age = 4))  # {'name': 'dog', 'age': 4}






### (4)字符串的通用排序

# 通用排序功能
# 功能：将数据容器的排序结果存入一个列表中，并返回该列表内容，不改变数据容器本身的值。
# 语法：sorted(iterable, cmp=None, key=None, reverse=False)
#     iterable：表示数据容器或可迭代对象
#     cmp：暂时不用管
#     key：函数key作为列表的排序依据；接受一个函数（或一个lambda匿名函数），该函数【接受一个列表项】并【返回一个用于排序的键】；key默认为元素本身。例如，如果想按字符串长度降序对列表进行排序，可以使用key=len
#     reverse：英文 反转、相反；默认升序


# 实际案例：
#
# x0 = [5, 4, 3, 2, 1]
# x1 = sorted(x0)
# print(x0)  # [5, 4, 3, 2, 1]，sorted方法不改变数据容器自身内容
# print(x1)  # [1, 2, 3, 4, 5]，sorted方法返回存放内容的列表，默认升序
#
# print(sorted({(1,'c'), (2,'b'), (3,'a')}, key=lambda x: x[0], reverse=True))  # [(3, 'a'), (2, 'b'), (1, 'c')]，以x[0]为依据，降序排列，返回列表
# print(sorted({(1,'c'), (2,'b'), (3,'a')}, key=lambda x: x[1], reverse=True))  # [(1, 'c'), (2, 'b'), (3, 'a')]，以x[1]为依据，升序排列，返回列表
#
# # 对字典进行排序，默认只对键进行处理
# print(sorted({1:3, 3:2, 2:1}))  # [1, 2, 3]，仅返回键所在的列表
# # 虽然sorted()函数无法直接返回带有完整键值对的列表，但是我们可以通过字典的items()方法，间接对字典按想要的键/值进行排序
# x2 = {'c': 1, 'a': 3, 'b': 2}
# print(dict(sorted(x2.items(), key=lambda x:x[1], reverse=True)))  # {'a': 3, 'b': 2, 'c': 1}
# print(dict(sorted(x2.items(), key=lambda x:x[0], reverse=True)))  # {'c': 1, 'b': 2, 'a': 3}


# 简单化使用：
#
# # 如下容器内顺序是乱序
# my_list = [4,2,5,1,3]
# my_tuple = (4,2,5,1,3)
# my_str = 'beadc'
# my_set = {4,2,5,1,3}
# my_dict = {'key4':1, 'key2':2, 'key5':3, 'key1':4, 'key3':5}  # 注意字典需要把Key乱序，而不是Value

# # 排序的结果通通变成了列表对象
# print(sorted(my_list))  # [1, 2, 3, 4, 5]
# print(sorted(my_tuple))  # [1, 2, 3, 4, 5]
# print(sorted(my_str))  # ['a', 'b', 'c', 'd', 'e']
# print(sorted(my_set))  # [1, 2, 3, 4, 5]
# print(sorted(my_dict))  # ['key1', 'key2', 'key3', 'key4', 'key5']

# # 注意：sorted不改变数据容器本身的内容
# print(my_list)  # [4, 2, 5, 1, 3]
# print(my_tuple)  # (4, 2, 5, 1, 3)
# print(my_str)  # beadc
# print(my_set)  # {1, 2, 3, 4, 5}  # 由于集合、字典本身无序，所以这里顺序和定义的不一样
# print(my_dict)  # {'key4': 1, 'key2': 2, 'key5': 3, 'key1': 4, 'key3': 5}

# # 逆序 = True
# print(sorted(my_list, reverse = True))  # [5, 4, 3, 2, 1]
# print(sorted(my_tuple, reverse = True))  # [5, 4, 3, 2, 1]
# print(sorted(my_str, reverse = True))  # ['e', 'd', 'c', 'b', 'a']
# print(sorted(my_set, reverse = True))  # [5, 4, 3, 2, 1]
# print(sorted(my_dict, reverse = True))  # ['key5', 'key4', 'key3', 'key2', 'key1']






### (5) 数据容器的大小比较

# 同种数据容器，可以用比较运算符来比较大小。
# 比较规则：序列(列表、元组、字符串) -- 逐个比较对应位置的元素，直到某个元素比较出大小，或者某一方先结束为止。
#         集合 -- 测试是否为子集
#         字典暂时不考虑


# # 列表
# print([1, 2, 4] > [1, 2, 3, 5])  # True
# print([1, 2, 4] == [1, 2, 3])  # False
#
# # 元组
# print((1, 2, 4) > (1, 2, 3, 5))  # True
# print((1, 2, 4) == (1, 2, 3))  # False
#
# # 字符串(比ascii码大小)
# print('abc' > 'abcd')  # False
# print('abc' < 'ABC')  # False
#
# # 集合(判断是否为子集)
# print({1, 2} < {1, 2, 3})  # True
# print({1, 5} < {1, 2, 4, 5})  # True
# print({1, 2, 3} == {1, 2})  # False

















## (10) 列表推导式、生成器表达式

# (1)列表推导式
# 功能介绍：列表推导式，可以使用非常简单的方式对可迭代对象元素进行遍历、过滤、再次计算，快速生成新的列表。
# 执行顺序：从左到右递进，表示语句之间的嵌套关系。
# 下面通过一些简单的例子，我们就能学会列表推导式。


# # [1]简单模式：只包含循环，不包含判断
# # 常规写法：
# list1 = []
# for x in range(1, 10):
#     list1.append(x)
# print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 列表推导式：
# list_1 = [x for x in range(1, 10)]
# print(list_1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# # [2]不仅包含循环，同时对元素结果进行运算处理
# # 常规写法：
# list2 = []
# for x in range(1, 10):
#     list2.append(x*x)
# print(list2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# # 列表推导式：
# list_2 = [x*x for x in range(1, 10)]
# print(list_2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# # 在列表推导式的第一个for前面，返回的值表示最终列表每个元素的值


# # [3]对添加的元素进行判断和筛选
# # 常规写法：
# list3 = []
# for x in range(1, 10):
#     if x % 2 == 0:  # 筛选偶数
#         list3.append(x)
# print(list3)  # [2, 4, 6, 8]
#
# # 列表推导式：
# list_3 = [x for x in range(1, 10) if x % 2 == 0]
# print(list_3)  # [2, 4, 6, 8]
#
# # 这里我们就可以发现，列表推导式，从左到右就是把常规写法的从上到下。
# # 列表推导式：从左到右将嵌套关系依次写出，再到头部表示元素的值。
# # # 注意：if语句不一定写最后，也可以写中间，具体须依照嵌套关系判断


# # [4]循环嵌套的列表推导式
# # 常规写法：（目的：取出tmp的列表元素的内容，将奇数存入新列表中）
# tmp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list4 = []
# for i in tmp:
#     for j in i:
#         if j % 2:
#             list4.append(j)
# print(list4)  # [1, 3, 5, 7, 9]
#
# # 列表推导式
# tmp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list_4 = [j for i in tmp for j in i if j % 2]
# print(list_4)  # [1, 3, 5, 7, 9]
#
# # 写法同理，推导式从左到右，即常规写法的从上到下。
# # 循环嵌套的列表推导式，从左到右将嵌套关系依次写出，并在最开头表示出元素的值



# 案例练习：
#
# # 【①】 去除下面列表元素前后的空格
# fruit = [' banana ', ' apple ', ' lemon ']
# fruit_1 = [x.strip() for x in fruit]
# print(fruit_1)  # ['banana', 'apple', 'lemon']
#
# # 【②】 用列表推导式实现列表的平铺
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# vec_1 = [y for x in vec for y in x]
# print(vec_1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 【③】 保留列表中正数，组成新列表
# num = [-1, 2, -3, -4, 5, -7, 0, 8]
# num_1 = [x for x in num if x > 0]
# print(num_1)  # [2, 5, 8]
#
# # 【④】 生成一个包含20个数字的随机数列表，随机数的范围是1到10
# random_num = [random.randint(1, 10) for x in range(20)]
# print(random_num)  # [10, 4, 7, 10, 8, 10, 8, 6, 10, 6, 7, 1, 4, 8, 5, 9, 8, 10, 8, 7]
# # 注意：并非列表推导式的值都要与x有关，上面列表推导式的range(20)意义仅是循环20次，x也无意义，每次循环中生成一个随机数。
# # 上面列表推导式的常规写法如下：
# random_num = []
# for x in range(20):
#     random_num.append(random.randint(1, 10))
# print(random_num)
# # 由此启发，只要存在for循环，那么也有对应的列表推导式，即使x无意义或样子很奇怪
#
# # 【⑤】 判断下面列表推导式的结果
# result = [(x, y) for x in [1, 2, 3] if x == 1 for y in [3, 1, 4] if x != y]
# # 我们可以按照从左到右的嵌套关系直接判断：
# print(result)  # [(1, 3), (1, 4)]
# # 当然，也可以将列表推导式展开为对应的for循环，如下：
# result = []
# for x in [1, 2, 3]:
#     if x == 1:
#         for y in [3, 1, 4]:
#             if y != x:
#                 result.append((x, y))
# print(result)  # [(1, 3), (1, 4)]





# (2)生成器表达式

# 【生成器表达式】
# 生成器表达式的语法和列表推导式仅一致，形式上生成器表达式用圆括号左定界符，如下：
#    生成器表达式：a = [x for x in range(10)]
#    列表推导式：a = (x for x in range(10))
# 生成器表达式特点：结果是一个生成器对象，具有惰性求值的特点，只在需要时生成新元素(且每个元素只生成一次)，比列表推导式效率更高，空间占用少，适合大数据处理。
#
#
#
# 【生成器对象】（元素：从左到右依次访问，且一个元素只能访问 一次）
# 简介：生成器对象可以转化为list或tuple，也可以用生成器对象的方法__next__()或内置函数next()进行遍历，或者用for循环遍历
#      不管用那种方法访问生成器对象的元素，【都只能从前到后依次访问，每个元素只能访问一次】，不支持下标访问。想再次访问，需要重新生成该对象
#      并非只有生成器表达式才返回生成器对象；enumerate、filter、map、zip等函数返回的对象，也都是生成器对象。
#
# 生成器对象是一个可迭代的对象，它可以在每次迭代中生成一个新的值。生成器对象具有以下性质：
#   ① 生成器对象会在迭代结束时自动关闭，不需要手动调用 close() 方法。
#   ② 生成器对象可以作为其他生成器对象的返回值。
#   ③ 生成器对象的值可以通过 next() 方法获取，直到调用 close() 方法或达到生成器对象的最大迭代次数。
#   ④ 生成器对象的迭代器可以作为其他迭代器对象的参数传递。
#   ⑤ 生成器对象的生成过程是异步的，不会阻塞主线程。
#
#
#
# 【内置函数next()、生成器对象方法__next__()】
# __next__()，是迭代器的内置方法，用于【获取并返回迭代器（相对于现在）的下一个元素】。如果没有更多的元素，那么就应该抛出 StopIteration 异常。
# next()，是python内置函数，当我们调用next()函数时，它会自动调用迭代器对象的__next__()方法。
#
# 无论使用next(迭代器)，还是迭代器.__next__()，函数都可以获取迭代器的下一个元素，只是调用方式不同而已。


# # 案例演示：
# g = (x**2 for x in range(10))
# print(g)  # <generator object <genexpr> at 0x0000029499786E90>，g是生成器对象
# tg = tuple(g)
# print(tg)  # (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)，可以将生成器对象转化为tuple.
# # g.__next__()  # 报错，【一个生成器对象只能从左到右访问其元素一次，tg = tuple(g)语句得到了生成器对象的全部元素，已经访问完了该生成器对象，所以不能再次访问】
#
# g = (x**2 for x in range(10))
# print(g.__next__()) # 0  __next__()方法，向后获取一个生成器对象的元素。由于生成器对象的性质，之后将无法再次获取这个元素，下次获取的将是后面的元素。
# print(next(g))      # 1  next()函数，向后获取一个生成器对象的元素
# print(g.__next__()) # 4
# print(next(g))      # 9
# print(tuple(g))     # (16, 25, 36, 49, 64, 81)，我们发现，这里没有取得以获取过的元素。
# # 这里我们便可以看出，生成器对象是一个可迭代的对象，它可以在每次迭代中生成一个新的值，每个值只能获取一次。
#
# g = (x**2 for x in range(10))
# for x in g:
#     print(x, end=' ')  # 0 1 4 9 16 25 36 49 64 81

















## (11)序列的解包

# 概念：序列的解包是对多个变量同时赋值的简介模式。
#      也就是可以把一个序列或可迭代对象的多个元素的引用同时赋值给多个变量，【要求等号两边的变量和值的数量必须一致】

# # 例子：
# x, y, z = 1, 2, 3
# print(x, y, z)  # 1 2 3
#
# v_tuple = (False, 3.5, 'exp')
# x, y, z = v_tuple
# print(x, y, z)  # False 3.5 exp
#
# x, y, z = range(3)
# print(x, y, z)  # 0 1 2



# 序列的解包可用于数据容器、enumerate对象、filter对象、zip对象等可迭代对象
# 注意：对字典使用序列的解包是，默认对键进行操作；若像对键值对整体操作，可以用items()方法将键值对转化为元组

# # 例子：
# a = [1, 2, 3]
# b, c, d = a
# print(b, c, d)  # 1 2 3
#
# x, y, z = sorted([3, 1, 2], reverse=True)
# print(x, y, z)  # 3 2 1
#
# a, b, c = 'ABC'
# print(a, b, c)  # A B C
#
# s = {'a': 1, 'b': 2, 'c': 3}
# q, w, e = s
# print(q, w, e)  # a b c
# q, w, e = s.items()
# print(q, w, e)  # ('a', 1) ('b', 2) ('c', 3)



# # 解包在循环中也是常见的操作。
# # 例子：
# keys = 'abcde'
# values = [1, 2, 3, 4, 5]
# for k, v in zip(keys, values):
#     print((k, v), end=' ')  # ('a', 1) ('b', 2) ('c', 3) ('d', 4) ('e', 5)
# print()
#
#
# x = ['a1', 'b2', 'c3']
# for i, j in enumerate(x):
#     print(f"index:{i},value:{j}", end=' ')  # index:0,value:a1 index:1,value:b2 index:2,value:c3
# print()
#
#
# s = {'a': 1, 'b': 2, 'c': 3}
# for k, v in s.items():
#     print((k, v), end=' ')  # ('a', 1) ('b', 2) ('c', 3)