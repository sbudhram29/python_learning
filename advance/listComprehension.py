nums = range(5, 201)

halves = []

for num in nums:
    halves.append(num/2)

print(halves)

halves = [num/2 for num in nums]

print(halves)
