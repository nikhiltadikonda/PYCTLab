a=set([i+1 for i in range(10)])
print(a)

print(1 in a)

a.add(11)

a.update([12,13])
print(a)

print(len(a))

fsa=frozenset(a)
print(fsa)
for i in fsa:
    print(i,end=" ")
    