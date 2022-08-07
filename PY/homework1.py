import threading
import time

n = 0
class MyThread1(threading.Thread):
    def run(self):
        global n
        n = n + 1

class MyThread2(threading.Thread):
    def run(self):
        global n
        print(n)
        n = 0

def test():
    for i in range(5):
        for j in range(5):
            t1 = MyThread1()
            t2 = MyThread2()
            t1.start()
            t2.start()
        time.sleep(1)
        print("")
if __name__ == "__main__":
    test()
