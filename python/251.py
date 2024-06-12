"""
Entrada	Saída
60 20
1 10

90
------------
100 51
2 50

250
"""

T, D = map(int, input().split())
V, P = map(int, input().split())

tax_p = P * (T // D)
tax_t = T * V

print(tax_p + tax_t)