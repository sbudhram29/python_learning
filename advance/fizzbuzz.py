def fizz_buzz(n=100):
    for num in range(1,n+1):
        fizzbuzz = ''

        if num % 3 == 0:
            fizzbuzz += 'Fizz'
        if num % 5 == 0:
            fizzbuzz += 'Buzz'
        if fizzbuzz:
            print(fizzbuzz)
        else:
            print(num)


fizz_buzz()
