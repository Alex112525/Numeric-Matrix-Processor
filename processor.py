def int_or_float(number_str):
    if "." in number_str:
        return float(number_str)
    else:
        return int(number_str)


def get_matrix(no_matrix):
    #if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        #    print("ERROR")
    no = ["", "first ", "second ", "third "]
    size = list(map(int, input("Enter size of {}matrix:".format(no[no_matrix])).split()))
    matrix = []

    print("Enter {}matrix:".format(no[no_matrix]))
    for _ in range(size[0]):
        row = list(map(int_or_float, input().split()))
        matrix.append(row)

    return matrix


def add_matrices(matrix_a, matrix_b):
    matrix_res = []
    rows = []
    if len(matrix_a) != len(matrix_b):
        print("The operation cannot be performed.")
    else:
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                rows.append(matrix_a[i][j] + matrix_b[i][j])
            matrix_res.append(rows)
            rows = []
    return matrix_res


def multiply_by_const(matrix):
    const = int_or_float(input("Enter constant:"))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j] * const
    return matrix


def multiply_matrices(matrix_a, matrix_b):
    columns_b = [[matrix_b[r][c] for r in range(len(matrix_b))] for c in range(len(matrix_b[0]))]
    matrix_res = []
    for row in range(len(matrix_a)):
        new_rows = []
        for column in range(len(columns_b)):
            res = 0
            for i in range(len(columns_b[column])):
                res += matrix_a[row][i] * columns_b[column][i]
            new_rows.append(res)
        matrix_res.append(new_rows)
    return matrix_res


def print_matrix(matrix):
    print("The result is")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], "", end="")
        print()
    print()


if __name__ == "__main__":
    choice = 1
    while choice != 0:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
        choice = int(input("Your choice:"))

        if choice == 1:
            matrixA = get_matrix(1)
            matrixB = get_matrix(2)
            matrixRes = add_matrices(matrixA, matrixB)
            print_matrix(matrixRes)

        elif choice == 2:
            matrixA = get_matrix(0)
            matrixRes = multiply_by_const(matrixA)
            print_matrix(matrixRes)

        elif choice == 3:
            matrixA = get_matrix(1)
            matrixB = get_matrix(2)
            matrixRes = multiply_matrices(matrixA, matrixB)
            print_matrix(matrixRes)


