a = str(input(""))
x = ""
for i in a.split(" "):
    x = x + i[::-1]
    x += " "
print(x)
