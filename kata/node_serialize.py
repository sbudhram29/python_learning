class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node('{self.val}', {self.left}, {self.right})"

class Linked:
    def __init__(self, head):
        if type(head) != Node:
            self.head = Node(head)
        else:
            self.head = head

    def __str__(self):
        current = self.head

        result = ""

        while current.left or current.right:
            result += f"Node('{current.val}', "
            if current.left:
                result += f"left = Node({current.left}), "
            else:
                result += f"left = None, "

            if current.right:
                result += f"right = Node({current.right}))"
            else:
                result += f"right = None)"
            current = current.left

        return result







node = Linked(Node('root',Node('left', Node('left.left')),Node('right')))

print(node)

