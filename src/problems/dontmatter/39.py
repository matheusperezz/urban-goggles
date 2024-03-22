def solve(tel_area, stars):
    limit = 40000000
    stars_visible = 0
    
    for flux in stars:
        particles_per_sec = flux * tel_area
        if particles_per_sec >= limit:
            stars_visible += 1
    
    return stars_visible

tel_area = int(input())
n = int(input())
star_flux = []
for _ in range(n):
    fluxo_estrela = int(input())
    star_flux.append(fluxo_estrela)

print(solve(tel_area, star_flux))