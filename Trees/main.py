from queue import Queue

if __name__ == "main":
    print("This is where I learned about trees")


def maximum(root):
    node = root

    while node.right is not None:
        node = node.right

    return node


def minimum(root):
    node = root

    while node.left is not None:
        node = node.left

    return node


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

    def successor(self, node):
        """
        Find successor of a given node
        If node has right sub-tree, then it's min(subtree)
        If node has no right sub-tree then check from root to that node and store latest parent
        who is having val more than val of node
        """

        successor_node = None

        if node.right is not None:
            # Condition 1
            successor_node = minimum(node.right)
            print("Successor of {0} is {1}".format(node.val, successor_node.val))
        else:
            # Condition 2
            current_node = self.root

            while current_node.val != node.val:
                if node.val > current_node.val:
                    current_node = current_node.right
                elif node.val < current_node.val:
                    successor_node = current_node
                    current_node = current_node.left

            if successor_node is None:
                print("Node {0} has no successor".format(node.val))
            else:
                print("Successor of {0} is {1}".format(node.val, successor_node.val))

    def predecessor(self, node):
        """
        Find predecessor of a given node
        If node has left sub-tree, then it's max(subtree)
        If node has no left sub-tree then check from root to that node and store latest parent
        who is having val less than val of node
        """

        predecessor_node = None

        if node.left is not None:
            # Condition 1
            predecessor_node = maximum(node.left)
            print("Successor of {0} is {1}".format(node.val, predecessor_node.val))
        else:
            # Condition 2
            current_node = self.root

            while current_node.val != node.val:
                if node.val > current_node.val:
                    predecessor_node = current_node
                    current_node = current_node.right
                elif node.val < current_node.val:
                    current_node = current_node.left

            if predecessor_node is None:
                print("Node {0} has no successor".format(node.val))
            else:
                print("Successor of {0} is {1}".format(node.val, predecessor_node.val))

    def inorder_traversal(self, node):
        if node is None:
            return

        self.inorder_traversal(node.left)
        print(node.val)
        self.inorder_traversal(node.right)


tree = Tree(20)
tree.insert_node(8)
tree.insert_node(4)
tree.insert_node(12)
tree.insert_node(10)
tree.insert_node(14)
tree.insert_node(22)

tree.predecessor(tree.root)
