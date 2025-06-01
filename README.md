# 🧮 Python CLI Calculator

A command-line calculator built in Python that evaluates mathematical expressions, including fractions and decimals. It uses infix-to-postfix conversion and supports operator precedence.

---

## 📚 Features

- Supports:
  - Fractions (`1/2`)
  - Decimals (`3.14`)
  - Integers (`10`)
  - Operators: `+`, `-`, `*`, `/`, `%`, `^`
- Handles parentheses and operator precedence
- Converts infix expressions to postfix and evaluates them
- Cleanly tokenizes input using regex
- Basic error handling

---

## 🛠️ How to Run

Make sure Python is installed, then run:

```bash
python CalculatorV1.py
```

You’ll see:

```
Calculator
Operator symbols: +, -, *, /
NOTE: KINDLY WRITE FRACTIONS IN BRACKETS
```

Example:

```
Enter expression: (1/2 + 3.5) * 2
Tokens: ['(', '1/2', '+', '3.5', ')', '*', '2']
Postfix: ['1/2', '3.5', '+', '2', '*']
Output: 8.0
```

---

## ⚠️ Notes

- Wrap all **fractions in brackets** to avoid parsing errors, e.g., `(1/2 + 3/4)`
- Avoid variables or letters — the calculator only works with numeric expressions

---

## 👨‍💻 Author

**Prakhar Srivastava**

This is part of my ongoing learning journey through the **60 Python Projects** list (see image below). I'm gradually building more complex projects — stay tuned!
