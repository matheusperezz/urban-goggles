length_road, tax_range = map(int, input().split())
cost_per_km, tax_price = map(int, input().split())

road_price = length_road * cost_per_km
tax = (length_road // tax_range) * tax_price

print(road_price + tax)
