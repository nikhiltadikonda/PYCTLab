#variable length args
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print (f"{key} == {value}") 
  
myFun(one ='Welcome', two ='To', three='Python')