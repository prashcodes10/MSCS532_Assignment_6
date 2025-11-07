import time
import random
import matplotlib.pyplot as plt

# Data Structure Implementations 

class Array:
    def __init__(self):
        self.items = []

    def insert(self, index, value):
        self.items.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def access(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            current = current.next

# Empirical Performance Measurement

def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# Defining array sizes to test
sizes = [1000, 5000, 10000, 20000]

# Store results
results = {
    "Array Insert": [],
    "Array Delete": [],
    "Array Access": [],
    "Stack Push": [],
    "Stack Pop": [],
    "Queue Enqueue": [],
    "Queue Dequeue": [],
    "LinkedList Insert": [],
    "LinkedList Traverse": [],
}

for size in sizes:
    print(f"Testing size: {size}")
    
     # Array performance
    arr = Array()
    start_time = measure_time(lambda: [arr.insert(0, i) for i in range(size)])
    results["Array Insert"].append(start_time)
    
    start_time = measure_time(lambda: [arr.delete(0) for _ in range(size)])
    results["Array Delete"].append(start_time)
    
    arr = Array()
    for i in range(size):
        arr.insert(i, i)
    start_time = measure_time(lambda: [arr.access(random.randint(0, size-1)) for _ in range(size)])
    results["Array Access"].append(start_time)
    
     # Stack performance
    stack = Stack()
    start_time = measure_time(lambda: [stack.push(i) for i in range(size)])
    results["Stack Push"].append(start_time)
    
    start_time = measure_time(lambda: [stack.pop() for _ in range(size)])
    results["Stack Pop"].append(start_time)
    
     # Queue performance
    queue = Queue()
    start_time = measure_time(lambda: [queue.enqueue(i) for i in range(size)])
    results["Queue Enqueue"].append(start_time)
    
    start_time = measure_time(lambda: [queue.dequeue() for _ in range(size)])
    results["Queue Dequeue"].append(start_time)
    
     # Linked List performance
    ll = LinkedList()
    start_time = measure_time(lambda: [ll.insert_at_tail(i) for i in range(size)])
    results["LinkedList Insert"].append(start_time)
    
    start_time = measure_time(lambda: ll.traverse())
    results["LinkedList Traverse"].append(start_time)

# Plotting the Results

plt.figure(figsize=(12, 8))

for op, times in results.items():
    plt.plot(sizes, times, marker='o', label=op)

plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (seconds)")
plt.title("Empirical Performance of Basic Data Structures")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
