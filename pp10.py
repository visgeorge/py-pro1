
print("Enter no")

n=int(input())

l1=[x**(2+x%2) for x in range(1,n+1)]

print(l1)