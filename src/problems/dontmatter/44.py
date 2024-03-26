from math import sqrt

def solve(records, max_distance):
    x, y = 0, 0
    for direction, distance in records:
        if direction == 'N':
            y += distance
        elif direction == 'S':
            y -= distance
        elif direction == 'L':
            x += distance
        elif direction == 'O':
            x -= distance
        
        # Calcula a distância atual da posição de Demasi à delegacia
        current_distance = sqrt(x**2 + y**2)
        
        # Verifica se a distância atual excede a distância máxima permitida
        if current_distance > max_distance:
            return 1  # Demasi se afastou além da distância permitida
    
    return 0  # Demasi nunca se afastou além da distância permitida

def main():
    # Leitura da entrada
    n, max_distance = map(int, input().split())
    records = [input().split() for _ in range(n)]
    
    # Chamada da função para verificar se Demasi se afastou além da distância permitida
    result = solve(records, max_distance)
    
    # Saída do resultado
    print(result)

if __name__ == "__main__":
    main()
