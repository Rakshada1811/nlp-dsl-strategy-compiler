# nlp-dsl-strategy-compiler
# NLP → DSL → Strategy Compiler & Backtesting Engine

## Overview

This project implements an **end-to-end pipeline** that converts **natural language trading strategies** into **executable Python logic** using compiler design principles.

The system cleanly separates:

* Natural language understanding
* Rule representation via a Domain-Specific Language (DSL)
* Abstract Syntax Tree (AST) generation
* Runtime evaluation and backtesting

The focus of this project is **architecture correctness, clarity, and extensibility**, rather than trading performance.

---

## High-Level Pipeline

```
Natural Language
      ↓
 NLP Parser
      ↓
 Structured Conditions
      ↓
 DSL Generator
      ↓
 Domain-Specific Language (DSL)
      ↓
 DSL Parser
      ↓
 Abstract Syntax Tree (AST)
      ↓
 AST Evaluator
      ↓
 Backtesting Engine
```

---

## Project Structure

```
.
├── nlp_parser.py        # Converts natural language into structured conditions
├── dsl_generator.py    # Generates readable DSL from NLP output
├── dsl_spec.md         # Formal DSL specification
├── dsl_parser.py       # Parses DSL into an AST
├── indicators.py       # Technical indicators (SMA, RSI)
├── code_generator.py   # Evaluates AST against runtime data
├── backtest.py         # Backtesting engine
├── demo.py             # End-to-end execution script
├── LICENSE
└── README.md
```

---

## Core Components

### 1. NLP Parser (`nlp_parser.py`)

* Handles unstructured natural language input
* Extracts strategy intent (indicators, comparisons)
* Produces structured entry and exit conditions
* Does **not** perform execution

---

### 2. DSL Generator (`dsl_generator.py`)

* Converts structured NLP output into a human-readable DSL
* Acts as a safety layer between interpretation and execution

Example DSL:

```text
ENTRY:
  close > sma(close,20) AND volume > 1000000

EXIT:
  rsi(close,14) < 30
```

---

### 3. DSL Specification (`dsl_spec.md`)

* Defines the grammar and structure of the DSL
* Ensures consistency and extensibility

---

### 4. DSL Parser (`dsl_parser.py`)

* Converts DSL text into a deterministic Abstract Syntax Tree (AST)
* Eliminates ambiguity before execution

---

### 5. Indicators (`indicators.py`)

* Implements technical indicators such as SMA and RSI
* Kept independent for modularity and reuse

---

### 6. AST Evaluation (`code_generator.py`)

* Evaluates AST conditions against runtime market data
* Dynamically resolves data fields, indicators, and constants
* Produces ENTRY / EXIT signals

---

### 7. Backtesting Engine (`backtest.py`)

* Simulates strategy execution over historical price data
* Evaluates signals at each timestep
* Tracks BUY / SELL events

---

### 8. End-to-End Demo (`demo.py`)

* Executes the complete pipeline
* Demonstrates DSL parsing, AST evaluation, and backtesting
* Prints sample signals for observability

---

## How to Run (Google Colab / Local)

### 1. Clone the Repository

```bash
git clone https://github.com/Rakshada1811/nlp-dsl-strategy-compiler.git
cd nlp-dsl-strategy-compiler
```

### 2. (Optional) Run Individual Stages

```bash
python nlp_parser.py
python dsl_generator.py
python dsl_parser.py
```

### 3. Run End-to-End Pipeline (Recommended)

```bash
python demo.py
```

Expected output:

```text
BUY at index ...
SELL at index ...
Backtest completed
Sample signals: [{'ENTRY': False, 'EXIT': False}, ...]
```

---

## Design Philosophy

* **Separation of concerns** between language, rules, execution, and simulation
* Deterministic execution through AST-based evaluation
* Extensible architecture for future enhancements

---

## Future Improvements

* Support for OR and nested logical expressions
* Additional indicators
* Visualization of backtest results
* Integration with real market data sources

---

## License

This project is licensed under the MIT License.
