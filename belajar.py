import math

r = float(input())
h1, rho1 = map(float, input().split())
h2, rho2 = map(float, input().split())

V1 = math.pi * (r ** 2) * h1
V2 = math.pi * (r ** 2) * h2

m1 = rho1 * V1
m2 = rho2 * V2

delta_m = abs(m2 - m1)

if delta_m < 1e-6:  
    print("BALANCE")
else:
    print(f"{delta_m:.3f}")