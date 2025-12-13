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
    ],
    "volume": [
        800000, 850000, 900000, 950000, 1000000,
        1050000, 1100000, 1200000, 1300000, 1400000,
        1500000, 1600000, 1700000, 1800000, 1900000,
        2000000, 2100000, 2200000, 2300000, 2400000,
        2500000
    ]
}

run_backtest(ast, price_data)
