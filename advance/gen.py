def compute():
    for i in range(10):
        yield i


for val in compute():
    print(val)
