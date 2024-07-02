class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertValue(head, val, k):
    prev = None
    cur = head

    for _ in range(k - 1):
        prev = cur
        cur = cur.next

    prev.next = Node(val=val, next=cur)

    return head


def deleteNode(head, val):
    cur = head
    prev = None

    while cur:
        if cur.val == val:
            break

        prev = cur
        cur = cur.next

    if not prev:
        return head.next

    prev.next = cur.next

    return head


def deleteGivenNode(node):
    node.val = node.next.val
    node.next = node.next.next


def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def findCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False
