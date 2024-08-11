class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def print_list(self):
        current = self
        while current:
            print(current.val, end=" ")
            current = current.next
        print()
    
def list_to_linked_list(l):
    if not l:
        return None
    
    head = ListNode(l[0])
    current = head
    for value in l[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head


N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
mums = list(map(int, input().strip().split()))

linked_N = list_to_linked_list(nums)
linked_M = list_to_linked_list(mums)

current_N = linked_N
current_M = linked_M

dummy = ListNode()
current_output = dummy

while current_N and current_M:
    if current_N.val <= current_M.val:
        current_output.next = ListNode(current_N.val)
        current_N = current_N.next
    else:
        current_output.next = ListNode(current_M.val)
        current_M = current_M.next
    current_output = current_output.next

while current_N:
    current_output.next = ListNode(current_N.val)
    current_N = current_N.next
    current_output = current_output.next

while current_M:
    current_output.next = ListNode(current_M.val)
    current_M = current_M.next
    current_output = current_output.next

dummy.next.print_list()