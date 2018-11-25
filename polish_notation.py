# parenthesis-free notation

while True:
    try:
        expression = input('Введите выражение в режиме польской нотации: оператор и 2 положительных числа через пробелы.\n\n Доступные операции:\n + сложение\n - вычитание\n * умножение\n / деление\n\nНапример, сложение двух положительных чисел: + 4 2.\n\nЕсли вы хотите выйти, введите exit.\n\nВведите данные:')
        if str(expression.lower()) == 'exit':
            break
        else:
            operator, operand1, operand2 = expression.split()
            assert float(operand1) > 0
            assert float(operand2) > 0
            if operator == '+':
                print(float(operand1) + float(operand2))
            elif operator == '*':
                print(float(operand1) * float(operand2))
            elif operator == '-':
                print(float(operand1) - float(operand2))
            elif operator == '/':
                print(float(operand1) / float(operand2))
            else:
                second_operation = input('Для выхода введите exit.\nЧтобы выполнить следующую операцию, нажмите Enter.\n')
                if second_operation.lower() == 'exit':
                    break
    except ValueError:
        print('\nНеверный формат ввода.\n')
    except AssertionError:
        print('\nВведено отрицательно число или 0. Введите положительные числа.\n')
