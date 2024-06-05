class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        
        char_count = {}
        for char in words[0]:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for word in words[1:]:
            temp_char_count = {}
            for char in word:
                if char in temp_char_count:
                    temp_char_count[char] += 1
                else:
                    temp_char_count[char] = 1
            
            for char in char_count:
                if char in temp_char_count:
                    char_count[char] = min(char_count[char], temp_char_count[char])
                else:
                    char_count[char] = 0
        
        result = []
        for char, count in char_count.items():
            for _ in range(count):
                result.append(char)
                
        return result

solution = Solution()
print(solution.commonChars(["bella","label","roller"]))
        
