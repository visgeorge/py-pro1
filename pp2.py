print("Enter String")
ip=input()

plist=[]

for i in range(len(ip)):
    for j in range(i+1,len(ip)+1):
        txt=ip[i:j]
        plist.append(txt)

plist.sort(key=len,reverse=True)

for i in plist:
    if i==i[::-1]:
        print(i,len(i))
        break
