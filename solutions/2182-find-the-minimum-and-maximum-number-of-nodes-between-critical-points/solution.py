# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        critical_points = []
        prev_node = None
        curr_node = head
        idx = 0

        while curr_node and curr_node.next:
            if prev_node and ((prev_node.val < curr_node.val > curr_node.next.val) or (prev_node.val > curr_node.val < curr_node.next.val)):
                critical_points.append(idx)
            prev_node = curr_node
            curr_node = curr_node.next
            idx += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            distance = critical_points[i] - critical_points[i - 1]
            min_distance = min(min_distance, distance)

        max_distance = critical_points[-1] - critical_points[0]

        return [min_distance, max_distance]

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
        
