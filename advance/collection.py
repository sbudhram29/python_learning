from collections import Counter


name = "SeanDoeEricaDoeLoganDoeLandonDoe"

myCounter = Counter(name)

print(myCounter)

print(myCounter.most_common())
print(myCounter.most_common(1))