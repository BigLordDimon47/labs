x = int(input("x="))
y = int(input("y="))
s = 0
for u in range(x, y):
    if u % 3 == 0:
        s += u
print(s)