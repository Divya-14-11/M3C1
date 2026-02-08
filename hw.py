file = open("codingal.txt", "r")
print("file is in read mode")
content = file.read()
lines = content.split("\n")
file.close()
file1 = open("c2", "w")
file1.close()
file1 = open("c2", "a")
for i in lines:
    word = ""
    for j in i:
        if j == " ":
            break
        word = word + j

    if word != "Coding" and word != "Codingal":
        print(i)
        file1.write(i)
        file1.write("\n")

file1.close()

