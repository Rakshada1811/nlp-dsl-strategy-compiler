# Domain-Specific Language (DSL) Specification
## Rule-Based Strategy DSL

### 1. Overview
This DSL is designed to express simple rule-based trading strategies in a clear and unambiguous format.  
It supports entry and exit conditions derived from natural language inputs and is intended to be easily parsed into an AST for execution.

The DSL focuses on clarity, consistency, and extensibility rather than full trading-system complexity.

---

### 2. High-Level Structure

A strategy consists of two main sections:
ENTRY:
<boolean expression>

EXIT:
<boolean expression>

Each section defines conditions under which a position should be entered or exited.

---

### 3. Supported Elements

#### 3.1 Fields (Time Series)
- `open`
- `high`
- `low`
- `close`
- `volume`

These fields refer to columns in the OHLCV dataset.

---

#### 3.2 Indicators
The DSL currently supports the following indicators:

- **Simple Moving Average (SMA)**
sma(close, 20)


- **Relative Strength Index (RSI)**
rsi(close, 14)


Indicators follow the format:
indicator_name(series, period)

---

#### 3.3 Comparison Operators
- `>`
- `<`
- `>=`
- `<=`
- `==`

Used to compare fields or indicators against values or other expressions.

---

#### 3.4 Boolean Operators
- `AND`
- `OR`

Boolean operators combine multiple rules within ENTRY or EXIT blocks.

Parentheses may be added in future extensions for nested logic.

---

### 4. Grammar (Simplified)

strategy := entry_block exit_block
entry_block := "ENTRY:" expression
exit_block := "EXIT:" expression

expression := condition
| condition AND condition
| condition OR condition

condition := operand operator operand

operand := field
| indicator
| numeric_value



---

### 5. Example

ENTRY:
close > sma(close,20) AND volume > 1000000

EXIT:
rsi(close,14) < 30


---

### 6. Assumptions & Design Choices
- The DSL is case-insensitive but written in uppercase keywords for readability.
- Only a limited set of indicators and fields are supported to keep parsing simple.
- The DSL is deterministic and does not allow ambiguous expressions.
- The focus is on correctness and explainability, not performance optimization.

---

### 7. Future Extensions
- Nested expressions using parentheses
- Additional indicators (EMA, MACD)
- Time-based references (yesterday, last week)
- Position sizing and risk rules
