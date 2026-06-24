from collections import deque
 
queue = deque()
 
def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item}. Queue: {list(queue)}")
 
def dequeue():
    if queue:
        item = queue.popleft()
        print(f"Dequeued {item}. Queue: {list(queue)}")
    else:
        print("Queue is empty")
 
enqueue("A")
enqueue("B")
enqueue("C")
dequeue()
dequeue()
print("Final queue:", list(queue))