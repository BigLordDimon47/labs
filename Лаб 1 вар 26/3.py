import math
n = int(input("N="))   
a = []
m = math.inf
l = 1
p = []
for i in range(n):
    s = int(input())
    a.append(s)
    if s >= 0 and s < m:
        m = s
    if s != 0 :
        l *= s
        p.append(s)
p.reverse()
print("Мінімальний додатний елемент - " + str(m))
print("Добуток - " + str(l))
print("Ненульові елементи" + str(p))