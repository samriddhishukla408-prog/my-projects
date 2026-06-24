stack = []
def push(item):
    stack.append(item)
    print(f"Pushed {item}. Stack: {stack}")


def pop():
    if stack:
        item = stack.pop()
        print(f"Popped {item}. Stack: {stack}")
    else:
        print("Stack is empty")
 
def peek():
    if stack:
        print(f"Top of stack: {stack[-1]}")
    else:
        print("Stack is empty")
 
push(10)
push(20)
push(30)
peek()
pop()
push(78)
peek()