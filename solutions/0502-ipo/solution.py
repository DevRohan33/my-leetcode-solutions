import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        i, h = 0, []
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(h, -projects[i][1])
                i += 1
            if h:
                w -= heapq.heappop(h)
            else:
                break
        return w
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        
