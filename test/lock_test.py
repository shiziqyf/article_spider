
import threading
import time

num = 0


def add():
    print("add...")
    global num
    for i in range(10_000_000):
        a = num
        a = a + 1
        num = a
    print("add end")

def sub():
    print("sub...")
    global num
    for i in range(10_000_000):
        num = num - 1
        print("num = ", num)


if __name__ == "__main__":
    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    # subThread02.start()

    subThread01.join()
    # subThread02.join()


    print("num result : %s" % num)
