a=int(input("Enter Marks: "))

print("A" if a>80 else("B" if(a<80 and a>60) else ("C" if(a<60 and a>50) else ("D" if(a<50 and a>40) else ("E" if(a<40 and a>25) else "F")))))