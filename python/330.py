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


N = int(input())
nums = list(map(int, input().strip().split()))
mums = list(map(int, input().strip().split()))

linked_N = list_to_linked_list(nums)
linked_M = list_to_linked_list(mums)

current_N = linked_N
current_M = linked_M

dummy = ListNode()
current_output = dummy
carry = 0

# Soma as listas
while current_N or current_M or carry:
    val1 = current_N.val if current_N else 0
    val2 = current_M.val if current_M else 0
    total = val1 + val2 + carry
    carry = total // 10
    current_output.next = ListNode(total % 10)
    
    if current_N:
        current_N = current_N.next
    if current_M:
        current_M = current_M.next
    current_output = current_output.next

dummy.next.print_list()