j, z, jm, zm = map(int, input().split())
counter = 0
while j < z:
    j = int((j * 2) - (j * (jm / 100)))
    z = int((z * 2) - (z * (zm / 100)))
    print(f"State: j={j} z={z}")
    counter += 1

print(counter)
