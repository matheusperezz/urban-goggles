def last_rank(students):
    ordered_students = sorted(students.items(), key=lambda x: (-x[1][1], x[0]))
    return ordered_students[-1][0], ordered_students[-1][1][0]

instance = 0
n = int(input())
students = {}
for _ in range(n):
    name, problems = input().strip().split()
    students[name] = (instance, int(problems))
    instance += 1

r = last_rank(students)
print(f'Instancia {r[1]}')
print(r[0])
print()