from collections import deque

def print_queue(queue):
    for q in queue:
        print(q, end=' ')
    print()

q = deque()
N = int(input())
for _ in range(N):
    operation = input()
    if operation == 'FILA':
        if len(q) == 0:
            print('Todos os pacientes foram atendidos')
        else:
            print_queue(q)
    elif operation == 'ATENDIMENTO':
        p = q.popleft()
        print(p)
    else:
        # Operação de chegada
        operation, name = operation.split(" ")
        q.append(name)