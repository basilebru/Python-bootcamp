import sys
lenght = len(sys.argv)
if lenght != 3:
    print("ERROR")
    exit()
stri = sys.argv[1]
n = sys.argv[2]
if stri.isdigit():
    print("ERROR")
    exit()
if n.isdigit() == False:
    print("ERROR")
    exit()
list = stri.split(" ")
list2 = [i for i in list if len(i) > int(n)]
print(list2)