year = 19

for i in range(1, 13):
    if i % 2:
        print(f'34{year} FA/WI{year}')
    else:
        print(f'12{year} SP/SU{year}')

    if not i % 2:
        year -= 1
