import re


def parse_natural_language(text: str):
    """
    Convert simple natural language trading rules
    into a structured JSON-like representation.
    """

    text = text.lower()

    result = {
        "entry": [],
        "exit": []
    }

    # ---- Close price vs Moving Average ----
    ma_match = re.search(
        r"close price is above the (\d+)[- ]day moving average",
        text
    )
    if ma_match:
        period = int(ma_match.group(1))
        result["entry"].append({
            "left": "close",
            "operator": ">",
            "right": f"sma(close,{period})"
        })

    # ---- Volume condition ----
    volume_match = re.search(
        r"volume is above (\d+(?:\.\d+)?)(?:\s*)(million|m)?",
        text
    )
    if volume_match:
        value = float(volume_match.group(1))
        if volume_match.group(2):
            value *= 1_000_000

        result["entry"].append({
            "left": "volume",
            "operator": ">",
            "right": int(value)
        })

    # ---- RSI exit rule ----
    rsi_match = re.search(
        r"rsi\((\d+)\) is below (\d+)",
        text
    )
    if rsi_match:
        period = int(rsi_match.group(1))
        threshold = int(rsi_match.group(2))

        result["exit"].append({
            "left": f"rsi(close,{period})",
            "operator": "<",
            "right": threshold
        })

    return result


if __name__ == "__main__":
    nl_input = (
        "Buy when the close price is above the 20-day moving average "
        "and volume is above 1 million. "
        "Exit when RSI(14) is below 30."
    )

    parsed_rules = parse_natural_language(nl_input)
    print(parsed_rules)
