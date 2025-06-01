import re

print("Calculator")
print("Operator symbols: +, -, *, /,^,%,//")
print("NOTE: KINDLY WRITE FRACTIONS IN BRACKETS")

def inf(expression):
    expression = expression.replace(" ", "")
    tokens = re.findall(r'-?\d+/\d+|-?\d+\.\d+|-?\d+|[+\-*/()^%]', expression)
    return tokens

def no_alpha(x):
    for i in x:
        if i.isalpha():
            return False
    return True

def prec(c):
    if c == "^":
        return 3
    elif c in ("/", "*","%"):
        return 2
    elif c in ("+", "-"):
        return 1
    else:
        return -1

def inf_to_pos(exp):
    L = []
    res = []
    for c in exp:
        if c not in "+-*/()":
            res.append(c)
        elif c == '(':
            L.append(c)
        elif c == ')':
            while L and L[-1] != '(':
                res.append(L.pop())
            L.pop()
        else:
            while L and prec(c) <= prec(L[-1]):
                res.append(L.pop())
            L.append(c)
    while L:
        res.append(L.pop())
    return res

def post_eval(exp):
    L = []
    for token in exp:
        if token not in "+-*/":
            L.append(eval(token))
        else:
            val1 = L.pop()
            val2 = L.pop()
            if token == "*":
                L.append(val2 * val1)
            elif token == "+":
                L.append(val2 + val1)
            elif token == "-":
                L.append(val2 - val1)
            elif token == "/":
                L.append(val2 / val1)
            elif token == "%":
                L.append(val2%val1)
            elif token =="^":
                L.append(val2**val1)
            elif token=="//":
                L.append(val2//val1)
    return L.pop()

# Main loop
while True:
    exp = input("Enter expression: ")
    exp = inf("(" + exp + ")")  # Wrap in parentheses for easier handling
    print("Tokens:", exp)
    conv = inf_to_pos(exp)
    print("Postfix:", conv)
    output = post_eval(conv)
    print(f"Output: {output}")
    x = input("Would you like to stop? (y/n): ")
    if x.lower() == 'y':
        break

    


    
