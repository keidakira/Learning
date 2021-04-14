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


def search_key(root, x):
    # Search for x in tree
    node = root
    parent = root

    while node is not None:
        if x > node.val:
            parent = node
            node = node.right
        elif x == node.val:
            return [node, parent]
        else:
            parent = node
            node = node.left

    return [None, None]


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
                return None
            else:
                print("Successor of {0} is {1}".format(node.val, successor_node.val))

        return successor_node

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

    def delete_node(self, val):
        """
        This is used to delete a node from the tree
        1. If node to be deleted is leaf, simple delete it
        2. If node to be deleted has one child, connect parent of node to child of node and then
            remove the node
        3. If node to be deleted has two children, find successor of node and replace node with
            it's successor and then remove successor node
        """

        [node_to_be_deleted, parent] = search_key(self.root, val)

        if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
            # Leaf node so simple remove it
            if parent.left is not None and parent.left.val == val:
                parent.left = None
            else:
                parent.right = None

        elif node_to_be_deleted.left is not None and node_to_be_deleted.right is None:
            # Node with left child then link parent to child
            if parent.left is not None and parent.left.val == val:
                parent.left = node_to_be_deleted.left
            else:
                parent.right = node_to_be_deleted.left
        elif node_to_be_deleted.left is None and node_to_be_deleted.right is not None:
            # Node with right child then link parent to child
            if parent.left is not None and parent.left.val == val:
                parent.left = node_to_be_deleted.right
            else:
                parent.right = node_to_be_deleted.right
        else:
            # Node with two children so find successor and then replace node with successor
            successor_node = self.successor(node_to_be_deleted)
            [successor_node, successor_parent] = search_key(self.root, successor_node.val)
            [node_to_be_deleted, node_to_be_deleted_parent] = search_key(self.root, node_to_be_deleted.val)

            if successor_parent.left is not None and successor_parent.left.val == successor_node.val:
                successor_parent.left = successor_node.right
            else:
                successor_parent.right = successor_node.right

            if node_to_be_deleted_parent.left is not None and node_to_be_deleted_parent.left.val == node_to_be_deleted.val:
                node_to_be_deleted_parent.left = successor_node
            else:
                node_to_be_deleted_parent.right = successor_node

            successor_node.right = node_to_be_deleted.right
            successor_node.left = node_to_be_deleted.left

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

tree.inorder_traversal(tree.root)
tree.delete_node(12)
tree.inorder_traversal(tree.root)