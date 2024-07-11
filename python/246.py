"""
Não finalizado
"""
from collections import deque

def solve(n, nums):
    queue = deque([0])
    visited = set()

    while queue:
        pos = queue.popleft()
        if pos >= 1:
            return "true"
        
        np = pos + nums[pos]
        if 0 <= np < n and np not in visited:
            visited.add(np)
            queue.append(np)
           
    return "false"

n = int(input())
nums = []
for _ in range(n):
    val = int(input())
    nums.append(val)

print(solve(n, nums))


