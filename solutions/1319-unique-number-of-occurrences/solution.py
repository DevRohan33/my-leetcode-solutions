class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return len(count.values()) == len(set(count.values()))
