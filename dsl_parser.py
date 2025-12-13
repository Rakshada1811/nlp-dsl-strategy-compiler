def parse_condition(condition_str):
    tokens = condition_str.strip().split()
    return {
        "left": tokens[0],
        "op": tokens[1],
        "right": tokens[2]
    }


def parse_block(block_text):
    if " AND " in block_text:
        conditions = block_text.split(" AND ")
        return {
            "type": "AND",
            "conditions": [parse_condition(c) for c in conditions]
        }
    else:
        return {
            "type": "SINGLE",
            "condition": parse_condition(block_text)
        }


def parse_dsl(dsl_text):
    ast = {}

    lines = [line.strip() for line in dsl_text.splitlines() if line.strip()]

    current_section = None

    for line in lines:
        if line == "ENTRY:":
            current_section = "ENTRY"
        elif line == "EXIT:":
            current_section = "EXIT"
        else:
            ast[current_section] = parse_block(line)

    return ast


if __name__ == "__main__":
    example_dsl = """
    ENTRY:
      close > sma(close,20) AND volume > 1000000

    EXIT:
      rsi(close,14) < 30
    """

    ast = parse_dsl(example_dsl)
    print(ast)
