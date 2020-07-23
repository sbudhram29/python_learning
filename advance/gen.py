def compute(start, end):
    for i in range(start, end + 1):
        yield i


for val in compute(4, 18):
    print(val)
