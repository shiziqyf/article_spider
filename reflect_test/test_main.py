if __name__ == '__main__':
    imp = input("模块名:")
    CC = __import__(imp, fromlist=True)
    inp_func = input("请输入要执行的函数：")
    f = getattr(CC, inp_func, None)
    f(name="eee")
