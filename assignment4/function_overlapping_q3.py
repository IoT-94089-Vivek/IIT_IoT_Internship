list1 = list(map(int,input("enter the 1st list").split()))
list2 = list(map(int,input("enter the 2nd list").split()))
def overlapp():
    for i in list1:
        for j in list2:
            if i == j:
                return 1
    return 0
          

if overlapp() == 1:
    print("True")
else:
    print("False")             
