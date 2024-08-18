class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Min-heap to keep track of the smallest ugly number
        heap = [1]
        # Set to keep track of the ugly numbers we've seen so far
        seen = {1}
        # The prime factors
        primes = [2, 3, 5]
        
        # Extract the smallest number n times from the heap
        for _ in range(n):
            ugly = heapq.heappop(heap)
            # Generate new ugly numbers by multiplying the current ugly number with 2, 3, and 5
            for prime in primes:
                new_ugly = ugly * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        # The nth ugly number is the last number popped from the heap
        return ugly
