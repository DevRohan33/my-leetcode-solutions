class Solution:
    def luckyNumbers(self, matrix):
        min_row_elements = [min(row) for row in matrix]
        max_col_elements = [max(col) for col in zip(*matrix)]

        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_row_elements[i] and matrix[i][j] == max_col_elements[j]:
                    lucky_numbers.append(matrix[i][j])

        return lucky_numbers

# Test cases
solution = Solution()

matrix1 = [[3,7,8],[9,11,13],[15,16,17]]
matrix2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
matrix3 = [[7,8],[1,2]]

print(solution.luckyNumbers(matrix1))  # Output: [15]
print(solution.luckyNumbers(matrix2))  # Output: [12]
print(solution.luckyNumbers(matrix3))  # Output: [7]
  
