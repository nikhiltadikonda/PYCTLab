# Python Functions
### 1.Function with return, without arguments
* Function Type 1
```py
def pie():
    return 3.141592653589793238462643383279502884197169399375105820974944592307816406286


a=int(input("Enter Radius: "))
print(a*a*pie())
 ```
### 2.Function with return, with arguments
* Function Type 2
```py
def area(a):
    return a*a*3.141592653589793238462643383279502884197169399375105820974944592307816406286

print(area(int(input("Enter Radius: "))))
```
### 3.Function without return, with arguments
* Function Type 3
```py
def area(a):
    print(a*a*3.141592653589793238462643383279502884197169399375105820974944592307816406286)

area(int(input("Enter Radius: ")))
```
### 4.Function without return, without arguments
* Function Type 4
```py
def area():
    a=2
    print(a*a*3.141592653589793238462643383279502884197169399375105820974944592307816406286)

area()
```
### 5.Variable length arguments in python functions
* Variablelengthargs
```py
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print (f"{key} == {value}") 
  
myFun(one ='Welcome', two ='To', three='Python')
```
### 6.Keyword arguments in python functions
* Keywordargs
```py
def sum(a,b,c):
    print(f"Sum: {a+b+c}")

sum(a=int(input("Enter a: ")),b=int(input("Enter b: ")),c=int(input("Enter c: ")))
sum(a=int(input("Enter a: ")),c=int(input("Enter c: ")),b=int(input("Enter b: ")))
```
### 7.Default arguments in python functions
* defaultargs
```py
def area(a,pi=3.141592653589793238462643383279502884197169399375105820974944592307816406286):
    return a*a*pi

print(area(int(input("Enter Radius: "))))
```