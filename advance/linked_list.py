class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"<Node data: {self.data}>"


class Double_Linked_List:

    def __init__(self, head):
        if type(head) != Node:
            self.head = Node(head)
        else:
            self.head = head

    def __repr__(self):
        return f"<Linked List data: {self.head.data}>"

    def is_empty(self):
        return self.head == None

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return None

        while current.next != None:
            if data == current.next.data:
                if not current.next.next:
                    current.next = None
                else:
                    current.next = current.next.next
                    current.next.prev = current
                return None
            current = current.next

    def size(self):
        if self.head == None:
            return 0

        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next

        return count

    def add(self, data):
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)
        current.next.prev = current


pets = Double_Linked_List('Max')
pets.add('Maxi')
pets.add('Minnie')
pets.add('Mickey')
pets.delete('Minnie')
pets.delete('Max')
pets.delete('Maxi')
pets.delete('Mickey')

print(pets.is_empty())
# print(pets.head.data)
# print(pets.head.next.data)
# print(pets.head.next.next.data)
# print(pets.head.next.next.prev.data)
# print(pets.head.next.prev.data)
