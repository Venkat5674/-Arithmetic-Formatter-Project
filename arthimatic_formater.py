def arithmetic_arranger(problems, display_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        # Check if operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Check if operands are more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the answer if display_answers is True
        if operator == '+':
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))

        # Determine the width of the problem
        width = max(len(operand1), len(operand2)) + 2

        # Format the problem lines
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dashes.append('-' * width)
        answers.append(result.rjust(width))

    # Combine the lines into the arranged output
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)

    if display_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems
