a = 250  # global value


def f1():
    global a
    a = 100  # global
    print(a)


def f2():
    a = 50  # local
    print(a)


def f3():
    b = 250 + 10
    print(b)


f1()
f2()
f3()
print(a)
