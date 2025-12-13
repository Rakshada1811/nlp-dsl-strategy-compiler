from indicators import sma, rsi


def evaluate_condition(cond, data):
    left = cond["left"]
    right = cond["right"]
    op = cond["op"]

    def resolve(value):
        if isinstance(value, (int, float)):
            return value

        if value in data:
            return data[value][-1]


        if value.startswith("sma"):
            period = int(value.split(",")[1].replace(")", ""))
            return sma(data["close"], period)

        if value.startswith("rsi"):
            period = int(value.split(",")[1].replace(")", ""))
            return rsi(data["close"], period)

        return float(value)

    l = resolve(left)
    r = resolve(right)

    if l is None or r is None:
        return False

    if op == ">":
        return l > r
    if op == "<":
        return l < r
    if op == ">=":
        return l >= r
    if op == "<=":
        return l <= r
    if op == "==":
        return l == r

    raise ValueError("Unsupported operator")


def evaluate_ast(ast, data):
    def eval_block(block):
        if block["type"] == "SINGLE":
            return evaluate_condition(block["condition"], data)

        if block["type"] == "AND":
            return all(
                evaluate_condition(cond, data)
                for cond in block["conditions"]
            )

    return {
        "ENTRY": eval_block(ast["ENTRY"]),
        "EXIT": eval_block(ast["EXIT"])
    }
