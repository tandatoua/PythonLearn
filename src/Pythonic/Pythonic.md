# <center> Pythonic
# 0 简介
 &emsp; &emsp;所谓的Pythonic，就是极具Python特色的Python代码，即明显区别与其他语言的写法的代码。
 &emsp; &emsp;在保证可读性的前提下，代码越短越好。

# 1 变量交换
    Python ： a,b = b, a
# 2 大小判断
    Python : 1<a<100

# 3 文件处理
    Python：
    with open(path, mode ) as f:
        pass
# 4 字符串操作
    names=['tom','nicy','nio']
    ','.join(names)
# 5 带索引位置的循环遍历
    names=['tom','James','Kobe']
    for i,name in enumerate(names):
        print('the',i,'is','name')
# 6 列表推导式
    a = [i*i for i in range(10) if 2<i<8]
# 7 集合推导式
    a = { i*i for i in range(10) if 2<i<8 }
# 8 生成器
    a = (i*i for i in range(10) if 2<i<8)
# 9 字典推导式
    names = ['Tom','James','Kobe']
    a = { name:n for n,name in enumerate(names)}
# 10 序列解包
    names =  'Tom','James','Kobe','Joden' or
    names =  ['Tom','James','Kobe','Joden'] 
    a,b,c,d = names
# 11 三元操作
    name = 'Kobe' if num == 24 else 'James'
# 12 简化判断
    if 'Kobe' in names : 
        print('Hello,Kobe!')
# 13 字符串反转
    name = 'Kobe'
    rename=name[::-1]
# 14 for .. else .. 语句
    for x in range(1,20):
        if x ==  24:
            print("Hello, Kobe")
            break
    else:
        print("Sad,this's not Kobe")
