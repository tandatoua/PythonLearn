# 1、解压序列赋值给多个变量
    _,a,b,c,_ = 'Hello'
    >>a = e ,b=l, c=l
    _,a,b,c,_ = [1,2,3,4,5]
    >>a =2 ,b =3,c=4
# 2、解压可迭代对象赋值给多个变量
    a,b,*c=[1,2,3,4,5....]
    >> a= 1, b=2,c=[3,4,5...]
    a,*b,c=[1,2,3,4,5,6]
    >> a= 1, b=[2,3,4,5],c=[6]
    * 代表可变长
# 3、deque(maxlen = N)
    构造固定大小的队列，新元素加入并且队列已满时，最老的元素会被自动移除    
    在队列两端插入或删除的时间复杂度为0(1),在列表的开头删除或插入元素的时间复杂度为0(n)
# 4、查找最大或最小的 N 个元素
    heapq模块中的nlargest() and nsamllest().
    heapq.nlargest(N,list)  
    heapq.nsamllest(N,list)
    heapq.nlargest(N,list,key='')  
    heapq.nsamllest(N,list,key ='')
    Notes:当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。 如果你仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用 min() 和 max() 函数会更快些。
# 5、字典中的键映射多个值
    collections 模块中的 defaultdict 来构造这样的字典。 defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。  
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
# 6、字典排序
    collections 模块中的 OrderedDict 类能控制一个字典中元素的顺序。
    from collections import OrderedDict
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    for key in d:
        print(key, d[key])
    OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
    需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
# 7、查找两字典的相同点
    a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
    }

    b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
    }

    # Find keys in common
    a.keys() & b.keys() # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys() # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items() # { ('y', 2) }
    & - 适用于集合或字典操作。
    + 适用于集合操作。
# 8 、删除序列相同元素   
    a=[1,2,3,3,2,1]
    b=list(set(a)) //排序会变
    c=list(set(a))
    c.sort(key=a.index)
    或者
    c=sorted(set(a),key = a.index)
    c=[]
    [c.append(i) for i in a if x not in c]
# 9、统计出现的数量
    collections.Counter
# 10、合并多个字典或映射
    collections 模块中的 ChainMap 类
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    print(c['x']) # Outputs 1 (from a)
    print(c['y']) # Outputs 2 (from b)
    print(c['z']) # Outputs 3 (from a)