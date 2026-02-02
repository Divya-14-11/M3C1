file=open("codingal.txt","r")
print("file is in read mode")
content=file.read()
content=content.split("\n")
counter=0
count=0
for i in content:
    counter=counter+1
    if counter==2:
        for j in i :
            count=count+1
        break    
print(f"THE NUMBER OF letter ARE {count}")
file.close()