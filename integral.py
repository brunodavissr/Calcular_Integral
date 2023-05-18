import math

def f(x):
    return 5*x*(math.sqrt(4-(3*x**2)))

n = 1000000
a = 0
b = 1
area_total = 0

i = a
while(i < b):
    p1 = i
    p2 = p1 + b/n
    area_retangulo = (p2-p1)*(f(p2))
    area_triangulo = (f(p1)-f(p2))*(p2-p1)/2
    area_total += area_retangulo + area_triangulo
    i += b/n

print(area_total)