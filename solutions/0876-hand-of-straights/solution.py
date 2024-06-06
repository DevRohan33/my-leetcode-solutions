class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1
        for card in sorted(count):
            if count[card] > 0:
                for i in range(1, groupSize):
                    if card + i not in count or count[card + i] < count[card]:
                        return False
                    count[card + i] -= count[card]
        return True
