class Solution:
    def sortPeople(self, names, heights):
        # Combine names and heights into a list of tuples
        combined = list(zip(heights, names))
        
        # Sort the combined list by heights in descending order
        combined.sort(reverse=True, key=lambda x: x[0])
        
        # Extract the names from the sorted combined list
        sorted_names = [name for _, name in combined]
        
        return sorted_names

# Example usage
solution = Solution()

# Example 1
names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
print(solution.sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]

# Example 2
names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(solution.sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]

