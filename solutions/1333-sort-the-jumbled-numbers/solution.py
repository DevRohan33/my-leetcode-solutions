class Solution:
    def sortJumbled(self, mapping, nums):
        def map_number(num):
            # Convert number to string to map each digit
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            # Convert back to int to remove any leading zeros
            return int(mapped_str)
        
        # Create a list of tuples (mapped value, original number)
        mapped_nums = [(map_number(num), num) for num in nums]
        
        # Sort based on the mapped value while keeping the original numbers
        mapped_nums.sort(key=lambda x: x[0])
        
        # Extract the sorted original numbers
        return [num for _, num in mapped_nums]

# Example usage
solution = Solution()
mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(solution.sortJumbled(mapping, nums))  # Output: [338, 38, 991]

mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [789, 456, 123]
print(solution.sortJumbled(mapping, nums))  # Output: [123, 456, 789]

