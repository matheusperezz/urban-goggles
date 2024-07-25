ip = list(input().split("."))
not_availables = list(map(int, input().strip().split()))
not_availables.append(int(ip[-1]))

availables = [x for x in range(1, 256) if x not in not_availables]
print(f'192.168.0.{availables[0]}')