class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class Avl:
    def __init__(self):
        pass

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = self.set_height(root)

        balance = self.get_balance(root)

        """
        LEFT HEAVY so greater than 1
        """
        if balance > 1 and value < root.left.value:
            print(value, "rotate_right")
            return self.rotate_right(root)

        if balance > 1 and value > root.left.value:
            print(value, "rotate_left_right")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        """
        RIGHT Heavy so less than -1
        """
        if balance < -1 and value > root.right.value:
            print(value, "rotate_left")
            return self.rotate_left(root)

        if balance < -1 and value < root.right.value:
            print(value, "rotate_right_left")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def set_height(self, node):
        if not node:
            return 0

        return 1 + max(self.get_height(node.left),self.get_height(node.right))

    @staticmethod
    def get_height(node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z

        y.height = self.set_height(y)
        z.height = self.set_height(z)

        return y

    def rotate_right(self, z):

        y = z.left
        z.left = y.right
        y.right = z

        y.height = self.set_height(y)
        z.height = self.set_height(z)

        return y

    def in_order(self, node):

        if not node:
            return

        self.in_order(node.left)
        print(node.value, end = " ")
        self.in_order(node.right)

    def pre_order(self, node):

        if not node:
            return

        print(node.value, end = " ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):

        if not node:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value, end=" ")


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

