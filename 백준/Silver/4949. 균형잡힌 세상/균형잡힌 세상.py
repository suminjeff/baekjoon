import sys
input = sys.stdin.readline


def brcheck(string):
    stack = []
    for s in string:
        if s in "()[]":
            if stack:
                if s == "(" or s == "[":
                    stack.append(s)
                else:
                    if s == ")":
                        if stack[-1] == "(":
                            stack.pop()
                        elif stack[-1] == "[":
                            return "no"
                    elif s == "]":
                        if stack[-1] == "[":
                            stack.pop()
                        elif stack[-1] == "(":
                            return "no"
            else:
                if s == "(" or s == "[":
                    stack.append(s)
                elif s == ")" or s == "]":
                    return "no"
    if stack:
        return "no"
    return "yes"


while True:
    string = input().rstrip()
    if string == ".":
        break
    print(brcheck(string))