
class add(int):
    def __call__(self,n):
        return add(self+n)

print(add(3))
print(add(3)(9))
print(add(3)(4)(9))