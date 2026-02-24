# ==== stack ====

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        node = self.top
        self.top = self.top.next
        return node.value
    
    def print_all(self):
        current = self.top
        print("Stack(top -> bottom): ", end="")
        if current is None:
            print("[empty]")
            return
        while current is not None:
            print(current.value, end="")
            current = current.next
            if current is not None:
                print(" -> ", end="")
        print()

if __name__ == "__main__":
    s = Stack()
    print("Pushing 10, 20, 30...")
    s.push(10)
    s.push(20)
    s.push(30)

    s.print_all()

    top = s.pop()
    print("Popped:", top)

    s.print_all