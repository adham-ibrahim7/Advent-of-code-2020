def evaluate(expression: str, evaluation_function):
    left = expression.find("(")
    if left == -1:
        tokens = expression.split(" ")
        return evaluation_function(tokens)
    depth = 0
    for right in range(left, len(expression)):
        if expression[right] == "(":
            depth += 1
        elif expression[right] == ")":
            depth -= 1
        if depth == 0:
            break

    return evaluate(expression[:left] + str(evaluate(expression[left+1:right], evaluation_function)) + expression[right+1:], evaluation_function)


def equal_precedence(tokens):
    value = int(tokens[0])
    for i in range(2, len(tokens), 2):
        if tokens[i-1] == "+":
            value = value + int(tokens[i])
        else:
            value = value * int(tokens[i])
    return value


def addition_first(tokens):
    while True:
        if "+" not in tokens:
            value = 1
            for i in range(0, len(tokens), 2):
                value *= int(tokens[i])
            return value
        i = tokens.index("+")
        tokens = tokens[:i-2+1] + [int(tokens[i-1]) + int(tokens[i+1])] + tokens[i+2:]


with open("../inputs/day18.txt", "r") as f:
    lines = f.read().split("\n")
    print("p1:", sum(evaluate(line, equal_precedence) for line in lines))
    print("p2:", sum(evaluate(line, addition_first) for line in lines))
