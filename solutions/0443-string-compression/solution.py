class Solution(object):
    def compress(self, chars):
        if not chars:
            return 0

        index_ans = 0
        index = 0

        while index < len(chars):
            count = 1
            while index + 1 < len(chars) and chars[index] == chars[index + 1]:
                index += 1
                count += 1

            chars[index_ans] = chars[index]
            index_ans += 1

            if count > 1:
                for c in str(count):
                    chars[index_ans] = c
                    index_ans += 1

            index += 1

        return index_ans
