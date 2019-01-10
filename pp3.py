print("Enter expression")
test=input()

obr=['{','[','(']
cbr=['}',']',')']

stk=[]

for i in test:
    if i in obr:
        stk.append(i)

    elif i in cbr:
        if stk[-1]==obr[cbr.index(i)]:
            stk.pop()

        else:
            print("Invalid")
            exit(-2)

print("Valid")



