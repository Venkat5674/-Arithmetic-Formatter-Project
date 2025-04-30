# Arithmetic Formatter

## Project Overview
The Arithmetic Formatter is a Python project that formats arithmetic problems vertically and side-by-side. It optionally displays the answers when specified. The project ensures proper formatting and validates various input constraints.

## Features
- Formats arithmetic problems (addition and subtraction) vertically.
- Optionally displays the answers.
- Handles up to 5 arithmetic problems at a time.
- Ensures proper validation of input (e.g., operator type, number size).

## Example Usage
```python
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# Output:
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
# Output:
#    32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#    40     -3800     19998      474
```

## Rules
1. **Input Validation**:
   - Maximum of 5 problems.
   - Only addition and subtraction are supported.
   - Numbers must only contain digits and should not exceed 4 digits in width.

2. **Formatting**:
   - Numbers are right-aligned.
   - Each problem is separated by 4 spaces.
   - Dashes underline each problem.

## How to Run
- Implement the `arithmetic_arranger` function in Python and pass a list of arithmetic problems.
