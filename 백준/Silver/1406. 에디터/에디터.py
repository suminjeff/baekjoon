import sys
input = sys.stdin.read
from collections import deque

def main():
    data = input().split()
    initial_string = data[0]
    M = int(data[1])
    commands = data[2:]
    
    left_stack = deque(initial_string)
    right_stack = deque()
    
    i = 0
    while i < len(commands):
        command = commands[i]
        if command == 'L':
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif command == 'D':
            if right_stack:
                left_stack.append(right_stack.popleft())
        elif command == 'B':
            if left_stack:
                left_stack.pop()
        elif command == 'P':
            i += 1
            left_stack.append(commands[i])
        i += 1
    
    result = ''.join(left_stack) + ''.join(right_stack)
    print(result)

if __name__ == "__main__":
    main()
