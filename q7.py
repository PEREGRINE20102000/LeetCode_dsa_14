"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])  # Get the size of the original matrix
        if m * n != r * c:  # Check if reshape operation is possible
            return mat  # If not, return the original matrix
        # Reshape the matrix and fill it with elements in row-traversing order
        flat_mat = [elem for row in mat for elem in row]
        return [flat_mat[i:i+c] for i in range(0, len(flat_mat), c)]