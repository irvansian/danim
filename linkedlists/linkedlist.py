class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(values):
    dummy = Node()
    cur = dummy

    for value in values:
        cur.next = Node(val=value)
        cur = cur.next

    return dummy.next


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


def findIntersections(head1, head2):
    cur1 = head1
    cur2 = head2
    seen = set()

    while cur1:
        if cur1 in seen:
            return cur1

        seen.add(cur1)
        cur1 = cur1.next

    while cur2:
        if cur2 in seen:
            return cur2

        seen.add(cur2)
        cur2 = cur2.next

    return None


def reverseLinkedList(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt

    return prev
