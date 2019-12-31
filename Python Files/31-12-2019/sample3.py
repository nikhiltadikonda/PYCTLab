quant=int(input("Enter Quantity"))*100
if(quant>1000):
    print("Amount to be paid: ",(quant-(quant*0.1)))
else:
    print(quant)