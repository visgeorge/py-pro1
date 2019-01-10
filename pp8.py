import re

print("Enter a list of comma separated passwords")
ip=input()

pwds=re.split('\s*,\s*',ip)

print("Valid are: ")

for i in pwds:
    c1=re.search(r'[a-z]',i)
    c2=re.search(r'[A-Z]',i)
    c3=re.search(r'[0-9]',i)
    c4=re.search(r'[$@#]',i)
    c5= 6 <= len(i) <= 12

    if c1 and c2 and c3 and c4 and c5:
        print(i,end=',')




