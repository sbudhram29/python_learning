class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BST:
    def __init__(self):
        pass

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left,value)
        else:
            root.right = self.insert(root.right, value)

        root.height = self.set_height(root)

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

    def get_average(self, node):
        if not node:
            return 0

        result = []

        queue = [node]

        while len(queue):
            count = len(queue)
            sum = 0

            for i in range(count):
                p = queue.pop(0)

                sum += p.value

                if p.left:
                    queue.append(p.left)

                if p.right:
                    queue.append(p.right)

            result.append(float(sum / count))

        return result


def pre_order(node):
    if not node:
        return ""

    print(node.value, end = " ")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if not node:
        return ""

    in_order(node.left)
    print(node.value, end = " ")
    in_order(node.right)

bst = BST()

tree = None

tree = bst.insert(tree, 3)
tree = bst.insert(tree, 9)
tree = bst.insert(tree, 20)
tree = bst.insert(tree, 15)
tree = bst.insert(tree,7)
tree = bst.insert(tree,2)
tree = bst.insert(tree,1)

pre_order(tree)
print()
print('=' * 20)
in_order(tree)
print()
print('=' * 20)
print(bst.get_average(tree))

