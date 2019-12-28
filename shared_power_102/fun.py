s = open('s.txt')
p = s.readline()
print(p)
try:
    a = next(s)
    while bool(a):
        print(a)
        try:
            a = next(s)
        except:
            break
except:
    pass
s.close()




fot = open('s.txt')
content = fot.readline()
while content:
    print(content)
    content = fot.readline()
fot.close()


fot = open('s.txt')
content = fot.readline()
