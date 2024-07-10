class Solution(object):
    def minOperations(self, logs):
        # Initialize the counter to keep track of the current depth in the file system
        depth = 0
        
        # Iterate over each log entry
        for log in logs:
            if log == "../":
                # Move to the parent folder, if possible
                if depth > 0:
                    depth -= 1
            elif log == "./":
                # Remain in the same folder
                continue
            else:
                # Move to the child folder
                depth += 1
        
        return depth

# Example usage
solution = Solution()
print(solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]))  # Output: 2
print(solution.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))  # Output: 3
print(solution.minOperations(["d1/", "../", "../", "../"]))  # Output: 0

