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
nums = list(map(float, input().strip().split()))
linked_nums = list_to_linked_list(nums)

current = linked_nums
total = 0
is_valid = True
while current:
    total += current.val
    if total < 0:
        print('invalido')
        is_valid = False
        break
    else:
        current = current.next

if is_valid:
    print(f'{total:.2f}')