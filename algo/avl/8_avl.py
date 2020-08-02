class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class Avl:
    def __init__(self):
        pass

    def add(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.add(root.left, value)
        else:
            root.right = self.add(root.right, value)

        root.height = self.set_height(root)
        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def set_height(self, node):
        if not node:
            return 0

        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        newNode = node.right
        node.right = newNode.left
        newNode.left = node

        node.height = self.set_height(node)
        newNode.height = self.set_height(newNode)

        return newNode


    def rotate_right(self, node):
        newNode = node.left
        node.left = newNode.right
        newNode.right = node

        node.height = self.set_height(node)
        newNode.height = self.set_height(newNode)

        return newNode


    def in_order(self, node):
        if not node:
            return ""
        self.in_order(node.left)
        print(node.value, end=" ")
        self.in_order(node.right)

    def pre_order(self, node):
        if not node:
            return ""
        print(node.value, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):
        if not node:
            return ""
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value, end=" ")

myTree = Avl()
tree = None

tree = myTree.add(tree, 10)
tree = myTree.add(tree, 20)
tree = myTree.add(tree, 30)
tree = myTree.add(tree, 40)
tree = myTree.add(tree, 50)
tree = myTree.add(tree, 25)

myTree.pre_order(tree)
print()
print('=' * 20)
myTree.in_order(tree)
print()
print('=' * 20)
myTree.post_order(tree)
print()
