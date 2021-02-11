openList = ["[","{","("]
closeList = ["]","}",")"]
def balance(myStr):
    stack= []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
print balance("{[()](){}}")




####second solution counts and matches parenthesis from string: 

def do_parentheses_match(input_string):
    s = []
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0
