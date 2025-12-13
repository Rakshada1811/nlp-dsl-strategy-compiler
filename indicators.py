def sma(series, period):
    if len(series) < period:
        return None
    return sum(series[-period:]) / period


def rsi(series, period=14):
    if len(series) < period + 1:
        return None

    gains = []
    losses = []

    for i in range(-period, 0):
        delta = series[i] - series[i - 1]
        if delta >= 0:
            gains.append(delta)
        else:
            losses.append(abs(delta))

    avg_gain = sum(gains) / period if gains else 0
    avg_loss = sum(losses) / period if losses else 1

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
