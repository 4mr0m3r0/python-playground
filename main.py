from algorithms.arrays import TransposeMatrix


def run_script():
    result = TransposeMatrix.transpose_matrix(
        matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    )
    print(result)


if __name__ == '__main__':
    run_script()
