import threading
import time

num = 0


def add():
    for i in range(50):
        lock.acquire()
        global num
        a = num
        print("a1 = ", a)
        time.sleep(0.1)
        a = a + 1
        num = a
        print("num1 = ", num)
        lock.release()


def sub():
    for i in range(50):
        lock.acquire()
        global num
        # print("num222 = ", num)
        a = num
        print("a2 = ", a)
        time.sleep(0.1)
        a = a - 1
        num = a
        print("num2 = ", num)
        lock.release()


if __name__ == "__main__":
    lock = threading.Lock()
    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)
