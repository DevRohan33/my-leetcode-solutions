class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # This will store the index of the winner in zero-based indexing
        winner = 0

        # Iterate through each circle size starting from 2 to n
        for i in range(2, n + 1):
            winner = (winner + k) % i

        # Convert zero-based index to one-based index
        return winner + 1

