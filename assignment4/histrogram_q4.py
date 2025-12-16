list1 = map(int,input("enter the list").split())

def histogram(lst):
    for i in lst:
        print(i,":",'*' * i)

histogram(list1)