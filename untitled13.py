#1
def PowerA3(n):
    return n ** 3

# Foydalanish
A, B, C = 2.5, 3.1, 4.2
D, E = 5, 6

print(f"A^3 = {PowerA3(A)}")
print(f"B^3 = {PowerA3(B)}")
print(f"C^3 = {PowerA3(C)}")
print(f"D^3 = {PowerA3(D)}")
print(f"E^3 = {PowerA3(E)}")
#2
def PowerA234(a):
    p2 = a ** 2
    p3 = a ** 3
    p4 = a ** 4
    return p2, p3, p4

# A, B, C sonlari uchun
for n in [2.0, 3.5, 5.0]:
    daraja2, daraja3, daraja4 = PowerA234(n)
    print(f"Son: {n} -> 2-daraja: {daraja2}, 3-daraja: {daraja3}, 4-daraja: {daraja4}")
#3
import math

def MEAN(x, y):
    am = (x + y) / 2
    gm = math.sqrt(x * y)
    return am, gm

A, B, C, D = 4, 9, 16, 25

# Juftliklar: (A,B), (A,C), (A,D)
for pair in [(A, B), (A, C), (A, D)]:
    arif, geom = MEAN(pair[0], pair[1])
    print(f"Juftlik {pair}: O'rta arifmetik = {arif}, O'rta geometrik = {geom:.2f}")
#4
import math

def Triangle(a):
    P = 3 * a
    S = (math.sqrt(3) / 4) * (a ** 2)
    return P, S

# 3 ta teng tomonli uchburchak uchun
tomoni = [3.0, 5.0, 7.5]

for a in tomoni:
    perimetr, yuza = Triangle(a)
    print(f"Tomoni {a} bo'lgan uchburchak: P = {perimetr}, S = {yuza:.2f}")
    