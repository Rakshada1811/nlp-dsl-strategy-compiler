def generate_dsl(structured_rules):
    """
    Convert structured rule representation into DSL text.
    """

    def format_condition(cond):
        return f"{cond['left']} {cond['operator']} {cond['right']}"

    dsl_lines = []

    # ENTRY rules
    if structured_rules.get("entry"):
        entry_conditions = [
            format_condition(cond)
            for cond in structured_rules["entry"]
        ]
        dsl_lines.append("ENTRY:")
        dsl_lines.append("  " + " AND ".join(entry_conditions))

    # EXIT rules
    if structured_rules.get("exit"):
        exit_conditions = [
            format_condition(cond)
            for cond in structured_rules["exit"]
        ]
        dsl_lines.append("\nEXIT:")
        dsl_lines.append("  " + " AND ".join(exit_conditions))

    return "\n".join(dsl_lines)


if __name__ == "__main__":
    example_structured = {
        "entry": [
            {"left": "close", "operator": ">", "right": "sma(close,20)"},
            {"left": "volume", "operator": ">", "right": 1000000}
        ],
        "exit": [
            {"left": "rsi(close,14)", "operator": "<", "right": 30}
        ]
    }

    dsl_text = generate_dsl(example_structured)
    print(dsl_text)
