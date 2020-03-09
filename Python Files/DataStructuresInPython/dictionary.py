sample={
        1:"Hello",
        2:"World",
        3:"Thor"}
print(sample)

print('\n',sample[1],sep="")

print('\n',sample.get(1),sep="")

sample[4]="Thunder"
print(sample)

for x in sample:
    print(x)

for x in sample.values():
    print(x)

for x,y in sample.items():
    print(x,':',y)

if 1 in sample:
    print(sample.get(1))

print(len(sample))