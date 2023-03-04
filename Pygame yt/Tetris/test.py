l = [1,2,4,5,6]

def inc(lista):
    for i in range(len(lista)):
        lista[i] += 10

f = l.copy()
print(l)
print(f)
inc(l)
print(l)
print(f)
