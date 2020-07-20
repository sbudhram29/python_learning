class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        current = self.root

        while current.next:
            current = current.next

        current.next = Node(data)

        return

    def to_array(self):
        res = []

        current = self.root

        while current:
            res.append(current.data)
            current = current.next

        return res

    def reverse(self):
        reverse_list = None
        current = self.root

        while current:
            next_node = current.next
            current.next = reverse_list
            reverse_list = current
            current = next_node

        self.root = reverse_list

    def delete(self, data):
        if data == self.root.data:
            self.root = self.root.next
            return

        current = self.root

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            else:
                current = current.next

    def remove_duplicate(self):
        current = self.root

        while current and current.next:
            runner = current
            while runner.next:
                if current.data == runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.next

    def remove_first(self):
        self.root = self.root.next




ll = LinkedList()
ll.insert(10)
ll.insert(12)
ll.insert(11)
ll.insert(11)
ll.insert(12)
ll.insert(11)
ll.insert(10)

print(ll.to_array())
ll.remove_duplicate()
ll.remove_first()
print(ll.to_array())

