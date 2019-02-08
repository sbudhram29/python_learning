from collections import Counter


name = "SeanBudhramEricaBudhramLoganBudhramLandonBudhram"

myCounter = Counter(name)

print(myCounter.most_common())
print(myCounter.most_common(1))
