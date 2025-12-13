from code_generator import evaluate_ast


def run_backtest(ast, price_data):
    in_position = False

    for i in range(len(price_data["close"])):
        data_slice = {
            "close": price_data["close"][: i + 1]
        }

        signals = evaluate_ast(ast, data_slice)

        if signals["ENTRY"] and not in_position:
            print(f"BUY at index {i}")
            in_position = True

        elif signals["EXIT"] and in_position:
            print(f"SELL at index {i}")
            in_position = False
