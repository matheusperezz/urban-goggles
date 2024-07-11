n = int(input())
man = list(map(int, input().strip().split()))
woman = list(map(int, input().strip().split()))

man.sort()
woman.sort()

left, right = 0, n-1
while left < n:
    print(f'{man[right]} {woman[left]}')
    left += 1
    right -= 1
