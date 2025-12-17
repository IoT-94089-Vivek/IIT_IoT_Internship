def str_rev(str1):
    str1 =str1[::-1] 
    print("reversed string is :",str1)


def find_vowels(str1):
    count = 0
    str1=str1.replace(" ","")
    l=len(str1)   
    for i in range(l):
        if str1[i] == 'a' or str1[i] == 'e' or str1[i] =='i' or str1[i] == 'o' or str1[i] == 'u' or str1[i] == 'A' or str1[i] == 'I' or str1[i] == 'O' or str1[i] == 'E' or str1[i] == 'U':
            count +=1
    print("no of vowels is :",count)
    
