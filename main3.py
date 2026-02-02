#write a program to find the total number of lines
file=open("codingal.txt","r")
print("file is in read mode")
content=file.read()
content=content.split("\n")
counter=0
for i in content:
    counter=counter+1
    
print(f"THE NUMBER OF LINES ARE {counter}")
file.close()