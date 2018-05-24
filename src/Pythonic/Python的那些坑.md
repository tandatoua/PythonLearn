# <center>Python的那些坑
# 0 简介
 &emsp; &emsp;在python开发过程中，难免会遇到一些坑，在此设立文件对遇到的，看到的坑进行总结。
# 1 数值不一定相等哟
    >>a = 4.2
    >>b = 1.1
    >>print(a+b == 6.3)
    >>Flase
这个其实不算是Python的坑，和计算机原理有一定关系。
    >>a = 4.2 
    >>b = 1.123
    >>print(a+b == 5.323)
    >>True
   