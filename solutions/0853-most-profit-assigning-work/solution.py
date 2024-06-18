class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        i = 0
        j = 0
        current_max_profit = 0
        while i < len(worker) and j < len(jobs):
            if worker[i] >= jobs[j][0]:
                current_max_profit = max(current_max_profit, jobs[j][1])
                j += 1
            else:
                max_profit += current_max_profit
                i += 1
        max_profit += current_max_profit * (len(worker) - i)
        return max_profit
