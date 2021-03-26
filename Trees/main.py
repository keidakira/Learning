from queue import Queue

if __name__ == "main":
    print("This is where I learned about trees")


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val):
        print("Creating a new tree with root {}".format(val))
        self.root = Node(val)

    def left_child(self, val):
        self.root.left = Node(val)

    def right_child(self, val):
        self.root.right = Node(val)

    def search_key(self, x):
        # Search for x in tree
        node = self.root

        while node is not None:
            if x > node.val:
                node = node.right
            elif x == node.val:
                return True
            else:
                node = node.left

        return False

    def bfs(self):
        # This is done using a queue
        queue = Queue()
        queue.put(self.root)

        # Now, for each element in queue, pop it's value and add it's children
        while not queue.empty():
            el = queue.get()

            if el.left is not None:
                queue.put(el.left)

            if el.right is not None:
                queue.put(el.right)

            print(el.val)

    def insert_node(self, val):
        node = self.root
        parent = self.root

        while node is not None:
            parent = node
            if val > node.val:
                node = node.right
            elif val < node.val:
                node = node.left
            else:
                raise Exception("Key already exists!")

        if val > parent.val:
            parent.right = Node(val)
        else:
            parent.left = Node(val)

        print("Node inserted")

    def max_node(self):
        node = self.root

        while node.right is not None:
            node = node.right

        return node.val

    def min_node(self):
        node = self.root

        while node.left is not None:
            node = node.left

        return node.val

    def inorder_traversal(self, node):
        if node is None:
            return

        self.inorder_traversal(node.left)
        print(node.val)
        self.inorder_traversal(node.right)


tree = Tree(2)
tree.insert_node(1)
tree.insert_node(3)

tree.bfs()

print("Maximum Node in tree is", tree.max_node())
print("Minimum Node in tree is",tree.min_node())
