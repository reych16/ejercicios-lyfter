#=== Deque ===

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None

class DoubleEndedQueue:
    def __init__(self):
        self.left_end = None
        self.right_end = None
    
    def is_empty(self):
        return self.left_end is None
    
    def push_left(self, value):
        new_node = DoubleNode(value)

        if self.is_empty():
            self.left_end = self.right_end = new_node
        else:
            new_node.next_node = self.left_end
            self.left_end.previous_node = new_node
            self.left_end = new_node
    
    def push_right(self, value):
        new_node = DoubleNode(value)

        if self.is_empty():
            self.left_end = self.right_end = new_node
        else:
            new_node.previous_node = self.right_end
            self.right_end.next_node = new_node
            self.right_end = new_node
    
    def pop_left(self):
        if self.is_empty():
            raise IndexError("The DoubleEndedQueue is empty.")
        
        removed_node = self.left_end

        if self.left_end == self.right_end:
            self.left_end = self.right_end = None
        else:
            self.left_end = self.left_end.next_node
            self.left_end.previous_node = None
        
        return removed_node.value
    
    def pop_right(self):
        if self.is_empty():
            raise IndexError("The DoubleEndedQueue is empty.")
        
        removed_node = self.right_end

        if self.left_end == self.right_end:
            self.left_end = self.right_end = None
        else:
            self.right_end = self.right_end.previous_node
            self.right_end.next_node = None
        
        return removed_node.value
    
    def print_all(self):
        print("Deque (left -> right): ", end="")
        if self.is_empty():
            print("[empty]")
            return
    
        current_node = self.left_end
        while current_node is not None:
            print(current_node.value, end="")
            current_node = current_node.next_node
            if current_node is not None:
                print(" <-> ", end="")
        print()

if __name__ == "__main__":
    dq = DoubleEndedQueue()

    print("Adding values on the left: 2, 1")
    dq.push_left(2)
    dq.push_left(1)

    print("Adding values on the right: 3, 4")
    dq.push_right(3)
    dq.push_right(4)

    dq.print_all()  

    print("Popping left:", dq.pop_left()) 

    print("Popping right:", dq.pop_right()) 

    dq.print_all()
