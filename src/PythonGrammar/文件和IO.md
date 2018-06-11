# <center> 文件读取与IO
# 1 操作文件
# 1.1 读取文件:使用带有 rt 模式的 open() 函数读取文本文件
    with open('somefile.txt', 'rt') as f:
        data = f.read()
## 1.2 写文件：使用带有 wt 模式的 open() 函数，如果之前文件内容存在则清除并覆盖掉
    with open('somefile.txt', 'wt') as f:
        f.write(text1)
        f.write(text2)
## 1.3 如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数
## 1.4 不使用with打开，需手动关闭文件。
    f = open('somefile.txt', 'rt')
    f.read()
    f.close()
## 1.4 输出至文件中(不能以二进制形式打开)
    with open('somefile.txt','wt') as f:
        print('Hello world!',file=f)
## 1.5 文件不存在才能写进去（xt模式）(Python 3特有)
    with open('somefile','xt') as f:   
        f.write('Hello ')
## 1.6 字符串IO，模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。
    io.StringIO()文本操作
    io.BytesIO() 二进制操作
# 2 文件操作
## 2.1 文件路径名操作
 使用OS.path的函数操作。   
    >>> import os  
    >>> path = '/Users/beazley/Data/data.csv'  
    >>> os.path.basename(path)  
    >>> os.path.dirname(path)  
    >>> os.path.join('tmp', 'data', os.path.basename(path))   

    >>> path = '~/Data/data.csv'
    >>> os.path.expanduser(path)
    '/Users/beazley/Data/data.csv'
## 2.2测试文件是否存在
    >>> os.path.exists('/etc/passwd') 是否存在
    >>> os.path.isfile('/etc/passwd') 是否为文件
    >>> os.path.isdir('/etc/passwd') 是否为路径
    >>> os.path.islink('/usr/local/bin/python3') 是否为连接文件
    >>>os.path.realpath('/usr/local/bin/python3') 路径
## 2.3获取文件夹中的文件列表
    names = os.listdir('somedir')
    import os.path

    # Get all regular files
    names = [name for name in os.listdir('somedir')
        if os.path.isfile(os.path.join('somedir', name))]

    # Get all dirs
    dirnames = [name for name in os.listdir('somedir')
        if os.path.isdir(os.path.join('somedir', name))]

    字符串的 startswith() 和 endswith() 方法用于过滤目录内容。
    pyfiles = [name for name in os.listdir('somedir')
            if name.endswith('.py')]