decimal=int(input("Enter a number:"))
binary=""
temp=decimal
while temp>0:
    remainder=temp%2
    binary=str(remainder)+binary
    temp=temp//2
print(f"The binary of {decimal} is {binary}")