v = []
for i in range (6):
    valor = int(input(f"asigna un valor{i+1}: "))
    v.append(valor)
pos = 0
ac = 0
while pos < len(v):
    ac = ac + v[pos]
    pos += 1
print(ac)
print(v)