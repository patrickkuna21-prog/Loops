num=int(input("Enter the number:"))
n=int(input("Enter how many powers to calculate:"))
print(f"\nPowers of {num} are:")
for i in range(1,n+1):
    power=num**i
    print(f"{num}^{i}={power}")