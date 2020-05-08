def get_matrix():
    size = list(map(int, input().split()))
    matrix = []

    for _ in range(size[0]):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def sum_matrices(matrix_a, matrix_b):
    matrix_res = []
    rows = []
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            rows.append(matrix_a[i][j] + matrix_b[i][j])
        matrix_res.append(rows)
        rows = []
    return matrix_res


if __name__ == "__main__":
    matrixA = get_matrix()
    matrixB = get_matrix()
    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        print("ERROR")
    else:
        matrix_sum = sum_matrices(matrixA,matrixB)
        for i in range(len(matrix_sum)):
            for j in range(len(matrix_sum[0])):
                print(matrix_sum[i][j], "", end="")
            print()

