class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def printList(self, listNode):
        if not listNode:
            return []
        result = []
        while listNode.next is not None:
            result.extend([listNode.val])
            listNode = listNode.next
        result.extend([listNode.val])
        return result[::-1]
