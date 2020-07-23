class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class Avl:
    def __init__(self):
        pass

    def insert(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = self.set_height(root)
        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def set_height(self, node):

        if not node:
            return 0

        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        new_node = node.right
        node.right = new_node.left
        new_node.left = node

        new_node.height = self.set_height(new_node)
        node.height = self.set_height(node)

        return  new_node

    def rotate_right(self, node):
        new_node = node.left
        node.left = new_node.right
        new_node.right = node

        new_node.height = self.set_height(new_node)
        node.height = self.set_height(node)

        return new_node

    def in_order(self, node):
        if not node:
            return

        self.in_order(node.left)
        print(node.data, end = " ")
        self.in_order(node.right)

    def pre_order(self, node):
        if not node:
            return

        print(node.data, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):
        if not node:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=" ")


myTree = Avl()
tree = None

tree = myTree.insert(tree, 10)
tree = myTree.insert(tree, 20)
tree = myTree.insert(tree, 30)
tree = myTree.insert(tree, 40)
tree = myTree.insert(tree, 50)
tree = myTree.insert(tree, 25)
# tree = myTree.insert(tree, 22)

print('=' * 20)
myTree.pre_order(tree)
print()
print('=' * 20)
myTree.in_order(tree)
print()
print('=' * 20)
myTree.post_order(tree)
print()
print('=' * 20)