file=open("codingal.txt")
print("file is in read mode")
print(file.read())
file.close()

file1=open("codingal.txt","w")
print("file is in write mode")
print(file1.write("hi I am divya"))
file1.close()


file2=open("codingal.txt","a")
print("file is in append mode")
print(file2.write(" how are you"))
file2.close()