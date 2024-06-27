class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # The center node will be present in both edges.
        a, b = edges[0]
        c, d = edges[1]
        if a == c or a == d:
            return a
        else:
            return b
