import math

ax, ay = map(float, input("Координаты A (x y): ").split())
bx, by = map(float, input("Координаты B (x y): ").split())
cx, cy = map(float, input("Координаты C (x y): ").split())

dist_b = math.hypot(bx - ax, by - ay)
dist_c = math.hypot(cx - ax, cy - ay)

if dist_b < dist_c:
    print(f"Ближе точка B, расстояние: {dist_b:.2f}")
elif dist_c < dist_b:
    print(f"Ближе точка C, расстояние: {dist_c:.2f}")
else:
    print(f"Точки B и C равноудалены от A, расстояние: {dist_b:.2f}")
