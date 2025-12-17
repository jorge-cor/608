print("----------------")

file = open("info.txt","r")

print ("------")
print (file.read(7))
print ("------")
print (file.read(7))
print ("------")

file.close()

file = open("info.txt","r")

print ("------")
print (file.readline())
print ("------")
print (file.readline())
print ("------")

file.close()
with open("info.txt","r") as file:
    for line in file:
        print (line)
