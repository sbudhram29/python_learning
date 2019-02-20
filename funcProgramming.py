def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = a + b, a
        yield a


for i,x in enumerate(fib(100)):
    print(f"fib {i}: {x}")

wrong = fib(15)

for x in wrong:
    print(x)