class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        n=len(customers)
        current_time= 0
        total_waiting_time = 0
        for arrival , preparation in customers:
            start_time = max(current_time,arrival) 
            current_time = start_time + preparation
            total_waiting_time += (current_time - arrival)
        averageWaitingTime= total_waiting_time/float(n)
        return averageWaitingTime
