class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) -1
        # Reversing a matrix 
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            print(matrix)
            l += 1
            r -= 1
        # transpose a matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
