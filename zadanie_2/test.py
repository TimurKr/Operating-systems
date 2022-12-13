def eval_expr(expr, variables={}):
    buf = []
    for w in expr.strip().split():
        if w.isnumeric():
            buf.append(float(w))
            continue
        elif w == "+":
            buf[-2] += buf[-1]
        elif w == "-":
            buf[-2] -= buf[-1]
        elif w == "*":
            buf[-2] *= buf[-1]
        elif w == "/":
            buf[-2] /= buf[-1]
        elif w in variables:
            buf.append(variables[w])
            continue
        else:
            raise Exception("Invalid input expression")
        buf.pop()
    return buf[0]


def to_infix(expr):
    buf = []
    for w in expr.strip().split():
        if w == "+":
            buf[-2] = f"( {buf[-2]} + {buf[-1]} )"
        elif w == "-":
            buf[-2] = f"( {buf[-2]} - {buf[-1]} )"
        elif w == "*":
            buf[-2] = f"( {buf[-2]} * {buf[-1]} )"
        elif w == "/":
            buf[-2] = f"( {buf[-2]} / {buf[-1]} )"
        else:
            buf.append(w)
            continue
        buf.pop()
    return buf[0]


def to_postfix(expr):
    expr = expr.strip().split()
    while True:
        try:
            end = expr.index(")")
        except ValueError:
            break
        
        start = end

        while True:
            start -= 1
            if expr[start] == "+":
                expr[end] = "+"
                expr.pop(start)
            elif expr[start] == "-":
                expr[end] = "-"
                expr.pop(start)
            elif expr[start] == "*":
                expr[end] = "*"
                expr.pop(start)
            elif expr[start] == "/":
                expr[end] = "/"
                expr.pop(start)
            elif expr[start] == "(":
                expr[start] = " ".join(expr[start+1:end])
                expr.pop(start+1)
                expr.pop(start+1)
                expr.pop(start+1)
                break

    return expr

# print(eval_expr("1 x +",{"x":2}))
# print(eval_expr("x x +",{"x":2}))
# print(eval_expr("2 x * x +",{"x":3}))
# print(eval_expr("x",{"x":3}))
# print(eval_expr("x y +",{"x":3,"y":2}))
# print(eval_expr("x y + 2 *",{"x":3,"y":2}))
# print(eval_expr("x y + y *",{"x":3,"y":2}))

# print(to_infix("1 2 *"))
# print(to_infix("1 2 * 3 +"))
# print(to_infix("1 2 3 * +"))
# print(to_infix("1"))


# print(to_postfix("1"))
# print(to_postfix("( 1 + 2 )"))
# print(to_postfix("( 10 * ( 1 + 2 ) )"))
# print(to_postfix("( ( 10 + 1 ) * ( 2 / 3 ) )"))
