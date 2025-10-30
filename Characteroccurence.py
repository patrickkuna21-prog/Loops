string=input("Please enter your word:")
chr=input("Please enter the character:")
i=0
count=0
while(i<len(string)):
    if (string[i]==chr):
        count=count+1
    i=i+1
print("The total numbers of times",chr ,"Has Occured=",count)
