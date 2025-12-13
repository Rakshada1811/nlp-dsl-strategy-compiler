{
  "ENTRY": {
    "type": "AND",
    "conditions": [
      {"left": "close", "op": ">", "right": "sma(close,20)"},
      {"left": "volume", "op": ">", "right": 1000000}
    ]
  },
  "EXIT": {
    "type": "SINGLE",
    "condition": {
      "left": "rsi(close,14)",
      "op": "<",
      "right": 30
    }
  }
}
