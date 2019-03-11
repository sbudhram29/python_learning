class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"A Node with {self.data} and {self.next}"


class Linked:
    count = 0

    def __init__(self, data):
        self.head = Node(data)
        self.count += 1

    def add(self,data):
        current = self.head

        while current.next != None:
            current = current.next
        self.count += 1
        current.next = Node(data)

    def delete(self, data):

        current = self.head

        if current.data == data:
            self.head = current.next
            self.count -= 1
            return None

        while current.next != None:
            if data == current.next.data:
                current.next = current.next.next
                self.count -= 1
                return None
            current = current.next

    def __str__(self):
        current = self.head
        print_str = ""

        while current.next:
            print_str += f"{current.data}-->"
            current = current.next

        print_str += f"{current.data}"

        return print_str

    def __repr__(self):
        current = self.head
        print_str = ""

        while current.next:
            print_str += f"Node({current.data})-->"
            current = current.next

        print_str += f"Node({current.data})"

        return print_str



link = Linked(1)

link.add(2)
link.add(2)

link2 = Linked(1)

link2.add(2)
link2.add(2)

print(link)
print(link2)
print(repr(link2))


