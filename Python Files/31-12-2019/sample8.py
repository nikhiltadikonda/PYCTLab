a=int(input("Enter Total Classes: "))
b=int(input("Enter Attended Classes: "))

print(float(b/a)*100,"%")
if((b/a)>0.75):
    print("Allowed")
else:
    if(input("Medica cause?:")=='Y' or 'y'):
        print("Allowed")
    else:
        print("Not Allowed")