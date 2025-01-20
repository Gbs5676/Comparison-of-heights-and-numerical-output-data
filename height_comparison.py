import math

m = [
    {"n": "Bruno", "h": 1.50},
    {"n": "Gabriel", "h": 1.60},
    {"n": "Lucas", "h": 1.70}
]

f = [
    {"n": "Ana", "h": 1.40},
    {"n": "Beatriz", "h": 1.55},
    {"n": "Larissa", "h": 1.65}
]

m.sort(key=lambda x: x["n"])
f.sort(key=lambda x: x["n"])

mm = sum(b["h"] for b in m) / len(m)
mf = sum(g["h"] for g in f) / len(f)

d = abs(mm - mf)
pd = (d / mm) * 100 if mm != 0 else 0

mm = round(mm, 2)
mf = round(mf, 2)
d = round(d, 2)
pd = round(pd, 2)

print("Meninos:")
for boy in m:
    print(f"{boy['n']}: {boy['h']:.2f} metros")

print("\nMeninas:")
for girl in f:
    print(f"{girl['n']}: {girl['h']:.2f} metros")

print(f"\nMédia de altura dos meninos: {mm} metros")
print(f"Média de altura das meninas: {mf} metros")
print(f"Diferença entre as médias: {d} metros")
print(f"Porcentagem de diferença: {pd}%")