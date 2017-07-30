def fib(num):
    a, b = 1, 1
    for _ in range(num):
        yield a
        a, b = b, a+b


n = int(input("plz enter:"))
for i in fib(n):
    print(i)
