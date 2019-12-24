tupdemo=tuple([i+1for i in range(10)])
print(tupdemo)

print(tupdemo[2:5])

print(tupdemo[-8:-1])

print(tupdemo[::-1])

x=list(tupdemo)
x.append(11)
tupdemo=tuple(x)
print(tupdemo)

for x in tupdemo:
    print(x,end=' ')

if 1 in tupdemo:
    print("\nYep you found it Boy..!")

print(len(tupdemo))

#oneitemtuple
onetup=("Hello",)
print(onetup)

tupdemo=tupdemo+onetup
print(tupdemo)
