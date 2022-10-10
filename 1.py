

def print_operation_table(operation=0, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        for j in range(i, i * num_columns + 1, i):
            print(j, end='\t')
        print()
print(print_operation_table())


def operation_table(func, row=9, columns=9):
    for i in range(row):
        for j in range(columns):
            print(f'{func(i + 1, j + 1)}', end=' \t')
        print()


operation_table(lambda x, y: x * y, 6)