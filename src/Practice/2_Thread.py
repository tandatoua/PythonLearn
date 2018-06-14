# from threading import Thread, Event
# import time
#
#
# def count_down(n: int,started_evt) -> None:
#     print("CountDown start!")
#     started_evt.set()
#     while n > 0:
#         print("The number is ", n)
#         time.sleep(2)
#         n -= 1
#
#
# started_evt = Event()  # 线程设置的标志位，用于判断某个线程的状态来确定自己下一步的操作
# print("Launching countdown")
# t = Thread(target=count_down, args=(5, started_evt))  # demon =true 为后台程序，非后台线程在主线程退出前，如果仍在运行，不会自动退出，直到运行结束
# t.start()
# time.sleep(1)
# started_evt.wait()
# print('countdown is running')
# if t.is_alive():
#     print("Hello, I'm still alive!")
# else:
#     print("Oh no!")

import threading
import time


# 信号量线程通信
def worker(n, sema):
    sema.acquire()
    print("working on ", n)


sema = threading.Semaphore(0)
nworker = 10
for n in range(nworker):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

for n in range(nworker):
    sema.release()
    time.sleep(1)

import threading
#类级锁

class SharedCounter:
    _lock = threading.RLock()

    def __init__(self, initial_value=0):
        self._value = initial_value

    def incr(self, delta=1):
        with SharedCounter._lock:
            self._value += delta

    def decr(self, delta=1):
        with SharedCounter._lock:
            self.incr(-delta)
