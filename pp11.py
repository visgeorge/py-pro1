

file1=open("new_file.txt","r")

str=file1.read()

print(str)

file1.close()


file1=open("new_file.txt","w")

file1.write(str[::-1])

file1.close()

