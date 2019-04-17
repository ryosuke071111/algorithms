import numpy as np

x = np.array([2, -5, -4, -8, 3, 0, 3, -6, -2, 1, 0, -4])

print("帰無仮説 H0: mu0 = 0")
print("対立仮説 H1: mu0 < 0")

a = 0.01
print(f"有意水準: {a}")

print("x_mean:",x.mean())
t = x.mean() / (x.std(ddof=1) / np.sqrt(x.size))
print(f"検定統計量 t: {t}")

print((x.std(ddof=1) / np.sqrt(x.size)))

ta = -2.718
print(f"下側確率{a} パーセント点: {ta}")

print()
if t < ta:
    print("H0は棄却される")
else:
    print("H0は棄却されない")
