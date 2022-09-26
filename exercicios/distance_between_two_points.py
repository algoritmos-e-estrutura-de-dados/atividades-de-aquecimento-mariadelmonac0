import math

px1 = float(input(" x1: "))
py1 = float(input(" y1: "))
px2 = float(input(" x2: ")) 
py2 = float(input(" y2: "))

dist = math.sqrt((px2 - px1)**2 + (py2 - py1)**2)

print(f"{dist:.4f}")