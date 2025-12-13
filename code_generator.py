from indicators import sma, rsi


def evaluate_condition(cond, data):
    # Defensive programming
    assert isinstance(data, dict), "Runtime data must be a dictionary"

    left = cond["left"]
    right = cond["right"]
    op = cond["op"]

    def resolve(value):
        # Numeric literal
        if isinstance(value, (int, float)):
            return value

        # Time-series field (close, volume, etc.)
        if value in data:
            return data[value][-1]

        # SMA indicator
        if isinstance(value, str) and value.startswith("sma"):
            period = int(value.split(",")[1].replace(")", ""))
            return sma(data["close"], period)

        # RSI indicator
        if isinstance(value, str) and value.startswith("rsi"):
            period = int(value.split(",")[1].replace(")", ""))
            return rsi(data["close"], period)

        # Numeric string
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

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

    raise ValueError(f"Unsupported operator: {op}")


def evaluate_ast(ast, data):
    def eval_block(block):
        if block["type"] == "SINGLE":
            return evaluate_condition(block["condition"], data)

        if block["type"] == "AND":
            return all(
                evaluate_condition(cond, data)
                for cond in block["conditions"]
            )

        raise ValueError("Unsupported block type")

    return {
        "ENTRY": eval_block(ast["ENTRY"]),
        "EXIT": eval_block(ast["EXIT"])
    }
