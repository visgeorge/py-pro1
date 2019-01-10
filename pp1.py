l1=[1,2,3,4,5]
l2=[3,4]

tf= False

for i in range(len(l1)):
    if l1[i]==l2[0]:
        tf=True

        for j in range(1,len(l2)):
            if i+j>=len(l1):
                tf = False
                break

            if l1[i+j]!=l2[j]:
                tf=False
                break

print(tf)
