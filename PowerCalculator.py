num=int(input("Enter the number:"))
n=int(input("Enter how many powers to calculate:"))
for i in range(1,n+1):
    power=num**i
    print("{num} raised to the power {i} is {power}")