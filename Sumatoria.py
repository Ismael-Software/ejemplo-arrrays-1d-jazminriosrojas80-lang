'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
v = []
for i in range (5):
    valor = int(input("ingrese el valor: "))
    v.append(valor)
pos = 0
ac = 0 
while pos < len(v):
    ac = ac + v[pos]
    pos = pos + 1 
print ("la suma es: ",ac)
