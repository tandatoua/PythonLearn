#<center>  practice make perfect
# 1 Palindrome
   &emsp; &emsp;回文数判断
# 2 Thread 
   &emsp; &emsp;后台线程无法等待，不过，这些线程会在主线程终止时自动销毁。法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作。  
   &emsp; &emsp;如果线程执行一些像I/O这样的阻塞操作，那么通过轮询来终止线程将使得线程之间的协调变得非常棘手。 可利用超时循环来小心操作线程。   
&emsp; &emsp;由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。所以，Python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等），而不是需要多处理器并行的计算密集型任务。
## 2.1 线程间通信--队列--单向通信
&emsp; &emsp;使用队列来进行线程间通信或者每个把线程当作一个Actor，利用Actor模型来控制并发。  
&emsp; &emsp;创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。  
&emsp; &emsp;Queue 对象已经包含了必要的锁，所以可以通过它在多个线程间多安全地共享数据。  
&emsp; &emsp;在生产者和消费者关闭问题时，可在生产者结束时，添加一个特殊的值，如果消费者读到该值，则消费者可停止，每个消费者读取之后，将该值继续放到队列中，可将监听该值的消费者都正常停止。
## 2.2 线程间通信--其他数据结构并加锁的机制
&emsp; &emsp;Queue可使用使用 threading 库中的 Lock 对象。  
    self._value_lock = threading.Lock()  
&emsp; &emsp;Lock 对象和 with 语句块一起使用可以保证互斥执行，就是每次只有一个线程可以执行 with 语句包含的代码块。with 语句会在这个代码块执行前自动获取锁，在执行结束后自动释放锁。  
&emsp; &emsp;为了避免出现死锁的情况，使用锁机制的程序应该设定为每个线程一次只允许获取一个锁。
&emsp; &emsp;使用threading.RLock()，没有对每一个实例中的可变对象加锁，取而代之的是一个被所有实例共享的类级锁。可以保证一次只有一个线程可以调用这个类方法。
## 2.3 避免死锁
 &emsp; &emsp;解决死锁问题的一种方案是为程序中的每一个锁分配一个唯一的id，然后只允许按照升序规则来使用多个锁，这个规则使用上下文管理器 是非常容易实现的。  
 &emsp; &emsp;避免死锁的主要思想是，单纯地按照对象id递增的顺序加锁不会产生循环依赖，而循环依赖是 死锁的一个必要条件，从而避免程序进入死锁状态。  
 &emsp; &emsp;死锁的检测与恢复没有太好的办法，一个比较常用的死锁检测与恢复的方案是引入看门狗计数器。（和单片机的看门狗类似）