def remember(thing):
    file = open("database.txt", "a")
    file.write(thing + "\n")
    file.close()


remember('apple juice')
remember('orange')
remember('apple cider')
remember('candy')
remember('water')
