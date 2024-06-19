class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            if self.can_make_m_bouquets(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def can_make_m_bouquets(self, bloomDay, m, k, days):
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m
        
