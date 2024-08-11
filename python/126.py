def solve(r, g, b):
    y = 16 + (0.257 * r) + (0.504 * g) + (0.098 * b)
    cb = 128 - (0.148 * r) - (0.291 * g) + (0.439 * b)
    cr = 128 + (0.439 * r) - (0.368 * g) - (0.071 * b)
    return round(y), round(cb), round(cr)

r, g, b = map(int, input().strip().split())
y, cb, cr = solve(r, g, b)

print(f"{y} {cb} {cr}")
