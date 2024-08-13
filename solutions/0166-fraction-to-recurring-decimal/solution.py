class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values to avoid negative number complications
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Append the integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        # Calculate the remainder
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)  # No fractional part
        
        # Append the decimal point
        result.append(".")
        
        # Map to store seen remainders and their corresponding positions in the result
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                # Repeating part found, enclose it in parentheses
                start_index = remainder_map[remainder]
                result.insert(start_index, "(")
                result.append(")")
                break
            
            # Store the current remainder and its index in the result
            remainder_map[remainder] = len(result)
            
            # Long division step to determine the next digit in the fractional part
            remainder *= 10
            next_digit = remainder // denominator
            result.append(str(next_digit))
            
            # Update the remainder
            remainder %= denominator
        
        return "".join(result)

# Example usage:
solution = Solution()
print(solution.fractionToDecimal(1, 2))   # Output: "0.5"
print(solution.fractionToDecimal(2, 1))   # Output: "2"
print(solution.fractionToDecimal(4, 333)) # Output: "0.(012)"

