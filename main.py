
a, b, c = map(float, input().split())
D = b ** 2 - 4 * a * c

if D > 0:
	x1 = (-b + D ** 0.5) / (2 * a)
	x2 = (-b - D ** 0.5) / (2 * a)
	print(f"x1 = {x1:.2}, x2 = {x2:.2}")
elif D == 0:
	x = -b / (2 * a)
	print(f"x = {x:.2}")
else:
	print("Нет корней")