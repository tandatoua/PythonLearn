
# 什么情况下需要扩展python
    1.需要python没有的额外功能时。

2.改善瓶颈性能。中所周知，由于解释型语言的代码在运行时即时转换，因此执行起来比编译语言慢。

3.隐藏专有代码。
# 编写python扩展主要涉及的三个步骤
1.创建应用代码（一定要保证应用代码的准确性）

2.根据样板编写封装代码

  样板代码主要含有四个部分：

  （1）包含python头文件（一定要安装python需要的库，centos：yum -y install python-devel）。

  （2）为每一个模块函数添加形如PyObject*Module_func()的封装函数。

  （3）为每一个模块函数添加一个PyMethoDef Module Methods[]数组/表。

  （4）添加模块初始化函数void initModule()。
## 对于CPU密集型python程序的编写，由于python的GIL锁的存在，所有无法支持多核多线程运行：解决方案，可以采用python + C多线程运行
