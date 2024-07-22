N1 = int(input())
m_professor = list(input().strip().split())

N2 = int(input())
m_blocked = list(input().strip().split())

N3 = int(input())
m_querys = list(input().strip().split())

for query in m_querys:
    if query in m_blocked:
        print('Proibido')
    else:
        print('Geral')