def eval_expr(expr):
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
        else:
            raise Exception("Invalid input expression")
        buf.pop()
    return buf[0]
