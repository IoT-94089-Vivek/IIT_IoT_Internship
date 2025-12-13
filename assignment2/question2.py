num = int(input("enter 5 digit no :"))

def len(i):
    u=0
    l =int(i)
    for k in range(1,100):
        if(l!=0):
           l= l/10
           u=u+1 
           l=int(l) 
    return u

def rev(m):
    while num > len(num):
        d = m % 10
        d = int(d) 
        re = re * 10 + d
    return re    

if len(num)== 5:
    print(f"the no is :{num}")
    r =  rev(num)
    
    if num == r:
        print("the no is palindrom")
    else:
        print("the no is not palindrom")
    
     
    
  
   
