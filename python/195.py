word = input()
is_palindrome = True
left, right = 0, len(word) - 1
while left < right:
    if word[left] != word[right]:
        is_palindrome = False
    left += 1
    right -= 1

if is_palindrome:
    print('Sim')
else:
    print('Nao')
