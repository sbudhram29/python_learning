

fizzbuzz = (lambda n: 'Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or str(n))
# fizzbuzz = (lambda n: 'Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or str(n))

print([fizzbuzz(n) for n in range(1, 101)])
