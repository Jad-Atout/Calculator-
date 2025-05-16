# Learning Journey: Tkinter Calculator

A simple GUI calculator built as part of a Python learning project. It demonstrates core Tkinter skills, basic arithmetic logic, and clean code organization.

## Features

* **Basic Operations**: +, -, ×, ÷, %
* **Decimal Support**: Enter and calculate floating-point numbers
* **Chained Calculations**: Continue computing on the previous result
* **Delete & Clear**: Backspace last entry or reset everything
* **Interactive UI**: Button hover effects for better UX

## Quick Start

1. Ensure Python 3.x is installed (Tkinter comes bundled).
2. Run:

   ```bash
   python calculator.py
   ```
3. Click buttons or use the keyboard to input numbers and operators.

## How It Works

* **Input Handling**: `click()` captures button presses and updates display.
* **Display**: A `Label` shows the current expression; an `Entry` shows the result.
* **Calculation Engine**:

  * `operate()` parses the input tokens into numbers and operators.
  * `create_digit()` builds multi-digit and decimal numbers.
  * `calculate()` performs the arithmetic and stores the result.
* **State Management**: Uses simple global variables (`data`, `label_str`, `previous_value`) to track input and results.

## Why I Built It

This project was my hands‑on exploration of:

* Tkinter’s widget layout and event binding
* Parsing and evaluating expressions in Python
* Structuring code into reusable functions and clear logic

It was a valuable stepping stone in mastering GUI development with Python.
