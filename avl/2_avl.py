class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class Avl:
    def __init__(self):
        pass

    def insert(self,root, value):

        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = self.set_height(root)
        balance = self.get_balance(root)

        ## left left heavy
        ## needs to rotate right
        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)

        ## left right heavy
        ## needs to rotate left right
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        ## right right heavy
        ## needs to rotate left
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)
        ## right left heavy
        ## needs to rotate right left
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root


    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def set_height(self, node):
        if not node:
            return 0

        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_left(self, node):
        temp = node.right
        temp_left = temp.left

        temp.left = node
        node.right = temp_left

        temp.height = self.set_height(temp)
        node.height = self.set_height(node)

        return temp

    def rotate_right(self, node):
        temp = node.left
        temp_right = temp.right

        temp.right = node
        node.left = temp_right

        temp.height = self.set_height(temp)
        node.height = self.set_height(node)

        return temp

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(node.value, end=" ")
        self.in_order(node.right)

    def pre_order(self, node):
        if not node:
            return
        print(node.value, end=" ")
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

myTree.pre_order(tree)
print()
print('=' * 20)
myTree.in_order(tree)
print()
print('=' * 20)
myTree.post_order(tree)
print()
print('=' * 20)
print(Avl.get_height(tree))