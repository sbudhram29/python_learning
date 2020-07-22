class TreeNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = None
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
            root.left.parent = root

        else:
            root.right = self.insert(root.right, value)
            root.right.parent = root

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
        new_node.parent = node.parent

        node.right = new_node.left
        if node.right:
            node.right.parent = node
        new_node.left = node

        new_node.left.parent = new_node


        new_node.height = self.set_height(new_node)
        node.height = self.set_height(node)

        return new_node

    def rotate_right(self, node):
        new_node = node.left
        new_node.parent = node.parent

        node.left = new_node.right
        if node.left:
            node.left.parent = node
        new_node.right = node
        new_node.right.parent = new_node

        new_node.height = self.set_height(new_node)
        node.height = self.set_height(node)

        return new_node

    def in_order(self, node):
        if not node:
            return

        self.in_order(node.left)
        print(node.value, end = " ")
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

    def find_node(self, root, value):
        if not root:
            return None

        if value == root.value:
            return root

        if value < root.value:
            return self.find_node(root.left, value)
        else:
            return self.find_node(root.right, value)




def find_in_order_successor(node):
    if not node:
        return None

    if node.right:
        return left_most(node.right)

    while node.parent:

        if node.parent.value > node.value:
            return left_most(node.parent)
        else:
            node.parent = node.parent.parent

    return None




def left_most(node):

    if not node.left:
        return node.value

    return left_most(node.left)



myTree = Avl()
tree = None

tree = myTree.insert(tree, 20)
tree = myTree.insert(tree, 9)
tree = myTree.insert(tree, 25)
tree = myTree.insert(tree, 12)
tree = myTree.insert(tree, 11)
tree = myTree.insert(tree, 14)
tree = myTree.insert(tree, 5)

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

print(myTree.find_node(tree, 5).parent.value)
print(myTree.find_node(tree, 14).parent.value)
print(myTree.find_node(tree, 11).parent.value)

print(find_in_order_successor(myTree.find_node(tree, 12)))
print(find_in_order_successor(myTree.find_node(tree, 11)))
print(find_in_order_successor(myTree.find_node(tree, 14)))
print(find_in_order_successor(myTree.find_node(tree, 25)))
