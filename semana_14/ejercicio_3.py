#---- Binary Tree ----
class TreeNode: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else: 
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def print_all(self):
        def _print(node, depth=0, side="root"):
            if node is None:
                return
            _print(node.left, depth + 1, "L")
            print(" " * depth + f"[{side}] {node.value}")
            _print(node.right, depth + 1, "R")
        if self.root is None:
            print("BinaryTree: [empty]")
        else:
            print("BinaryTree (in-order with structure):")
            _print(self.root)

bt = BinaryTree()
for x in (5, 3, 7, 2, 4, 6, 8):
    bt.insert(x)
bt.print_all()