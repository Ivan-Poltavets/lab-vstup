list = input().split()
a = int(list[0])
c = int(list[2])
if list[1] == "+":
    result = a + c
    print(result)
elif list[1] == "-":
    result = a - c
    print(result)
elif list[1] == "*":
    result = a * c
    print(result)
elif list[1] == "/":
    if c == 0:
        print("На ноль ділити неможна")
    else:
        result = a / c
        print(result)
