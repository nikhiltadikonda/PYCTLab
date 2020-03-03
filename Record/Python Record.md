# Python Record - Nikhil Tadikonda
#### 1. Write a PHP script to demonstrate any 5 string functions
```php
    <?php
    echo strlen("Hello world!");
    echo str_word_count("Hello world!");
    echo strrev("Hello world!");
    echo strpos("Hello world!", "world");
    echo str_replace("world", "Dolly", "Hello world!");
    ?>
```
#### 2. Write a PHP script to demonstrate indexed and associative arrays
```php
    #Indexed Arrays
    <?php
    $songs = array("Classic", "Jazz", "Retro");
    echo "I like " . $songs[0] . ", " . $songs[1] . " and " . $songs[2] . ".";
    ?>

    #Associative Arrays
    <?php
    $score = array("Kohli"=>"99", "Steve Smith"=>"50", "Dhoni"=>"100");
    echo "Dhoni Scored " . $score['Dhoni'] . " runs.";
    ?>
```
#### 3. Write a python program that takes input number as n and generate n prime numbers
```py

```
#### 4. Write a python program that demonstrates list methods
```py
    #Append
    a = ["bee", "moth"]
    a.append("ant")
    print(a)

    #Insert
    a.insert(4, "fly")
    print(a)

    #Clear
    a.clear()
    print(a)
    a = ["bee", "moth","bee"]

    #Count
    print(a.count("bee"))

    #sort
    a.sort()
    print(a)
```
#### 5. Demonstrate Dictionary methods in python
```py
    sample={
        1:"Hello",
        2:"World",
        3:"Thor"}
    print(sample)

    print('\n',sample[1],sep="")

    print('\n',sample.get(1),sep="")

    #Add Element to a Dictioanry 
    sample[4]="Thunder"
    print(sample)

    for x in sample:
        print(x)
    
    #print values
    for x in sample.values():
        print(x)
    
    #print key-value pairs
    for x,y in sample.items():
        print(x,':',y)
    
    #find whether a value is present in a dictionary or not
    if 1 in sample:
        print(sample.get(1))

    print(len(sample))
```
#### 6. Demonstrate Set methods in python
```py
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
```
#### 7. Demonstrate Tuple methods in python
```py
    tupdemo=tuple([i+1 for i in range(10)])
    print(tupdemo)

    #Tuple Comprehension
    print(tupdemo[2:5])

    print(tupdemo[-8:-1])

    print(tupdemo[::-1])
    
    #Add Element in a Tuple
    x=list(tupdemo)
    x.append(11)
    tupdemo=tuple(x)
    print(tupdemo)

    for x in tupdemo:
        print(x,end=' ')

    if 1 in tupdemo:
        print("\nFound it..!")

    print(len(tupdemo))

    #create a one item tuple
    onetup=("Hello",)
    print(onetup)

    tupdemo=tupdemo+onetup
    print(tupdemo)
```
#### 8. Write a python program to implement list comprehension
```py
```
#### 9. Write a python program that demonstrates try , except and finally using file operations
```py
```
#### 10. Write a python program to implement single and multilevel inheritance
```py
```
#### 11. Write a python program that demonstrates polymorphism using oops concepts
```py
```
#### 12. Write a python program that implements decorators in functions
```py
```
#### 13. Write a python program to read write and display contents of CSV files
```py
```
#### 14. Sample Django App
```py
```
#### 15. Sample ReactJS App
```py
```