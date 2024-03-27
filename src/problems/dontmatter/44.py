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
        
        current_distance = sqrt(x**2 + y**2)
        
        if current_distance > max_distance:
            return 1
    
    return 0

def main():
    n, max_distance = map(int, input().split())
    records = [input().split() for _ in range(n)]
    records = [(direction, int(distance)) for direction, distance in records]
    
    result = solve(records, max_distance)
    
    print(result)

if __name__ == "__main__":
    main()
