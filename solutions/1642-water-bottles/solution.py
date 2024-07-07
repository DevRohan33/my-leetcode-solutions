class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk = 0
        empty_bottles = 0

        while numBottles > 0:
            # Drink all full bottles
            total_drunk += numBottles
            empty_bottles += numBottles

            # Calculate new full bottles from empty ones
            numBottles = empty_bottles // numExchange
            # Remaining empty bottles after the exchange
            empty_bottles = empty_bottles % numExchange

        return total_drunk
