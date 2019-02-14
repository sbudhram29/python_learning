nums = range(5, 201)

halves = []

for num in nums:
    halves.append(num / 2)

print(halves)

halves = [num/2 for num in nums]

print(halves)

fizzBuzz = (lambda x: 'Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0) or str(x))

print([fizzBuzz(x) for x in range(1, 101)])

print(1 * (2 % 2 == 1) or False)
print(1 * (2 % 2 == 0) or False)

