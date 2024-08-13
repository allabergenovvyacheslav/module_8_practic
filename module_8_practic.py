# -*- coding: utf-8 -*-

# Есть файл calc.txt с записями операций - текстовый калькулятор. Записи вида
#
# 100 + 34
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделенные пробелами.
# Операндны - целые числа. Операции - арифметические, целочисленное деление и остаток от деления.
#
# Нужно вычислить все операции и найти сумму их результата.

def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == "+":
        value = operand_1 + operand_2
    elif operation == "-":
        value = operand_1 - operand_2
    elif operation == "//":
        value = operand_1 // operand_2
    elif operation == "/":
        value = operand_1 / operand_2
    elif operation == "*":
        value = operand_1 * operand_2
    elif operation == "%":
        value = operand_1 % operand_2
    else:
        raise ValueError('Unknown operation {operation}')
    return value


count = 0
total = 0

with open('calc.txt', 'r') as file:
    for line in file:
        count += 1
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Error in line: {count}, не хватает данных для ответа')
            else:
                print(f'Error in line: {count}, значение нельзя перевести в число')
print(f'Total = {total}')
