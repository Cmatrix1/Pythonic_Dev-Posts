from collections import deque

# LiFo
stack = deque()
stack.append("Plate 1")
stack.append("Plate 2")
stack.append("Plate 3")

print(stack.pop())  # Outputs: "Plate 3"
print(stack.pop())  # Outputs: "Plate 2"
print(stack.pop())  # Outputs: "Plate 1"


# Fifo
queue = deque()
queue.append("Person 1")
queue.append("Person 2")
queue.append("Person 3")

print(queue.popleft())  # Outputs: "Person 1"
print(queue.popleft())  # Outputs: "Person 2"
print(queue.popleft())  # Outputs: "Person 3"
