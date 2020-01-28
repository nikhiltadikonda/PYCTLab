#keyword args
def sum(a,b,c):
    print(f"Sum: {a+b+c}")

sum(a=int(input("Enter a: ")),b=int(input("Enter b: ")),c=int(input("Enter c: ")))
sum(a=int(input("Enter a: ")),c=int(input("Enter c: ")),b=int(input("Enter b: ")))