n = int(input())
correct_answ = input()
student_answ = input()
score = 0
for i in range(n):
    if correct_answ[i] == student_answ[i]:
        score += 1

print(score)