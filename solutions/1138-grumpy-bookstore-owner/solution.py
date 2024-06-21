class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        total_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
        max_satisfied = 0
        window_sum = 0
        for i in range(minutes):
            window_sum += customers[i] * grumpy[i]
        max_satisfied = window_sum
        for i in range(minutes, n):
            window_sum += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            max_satisfied = max(max_satisfied, window_sum)
        return total_satisfied + max_satisfied
