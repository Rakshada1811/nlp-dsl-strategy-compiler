from dsl_parser import parse_dsl
from backtest import run_backtest

dsl = """
ENTRY:
  close > sma(close,20) AND volume > 1000000

EXIT:
  rsi(close,14) < 30
"""

ast = parse_dsl(dsl)

price_data = {
    "close": [
        100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
        110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
        120
    ]
}

run_backtest(ast, price_data)
