import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    ROWS, COLS = len(A), len(A[0])
    res = np.asarray([np.asarray([0] * ROWS) for _ in range(COLS)])

    for i in range(ROWS):
        for j in range(COLS):
            res[j][i] = A[i][j]

    return res
