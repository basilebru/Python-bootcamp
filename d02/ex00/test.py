def count(start=0):
    num = start
    while True:
        yield num
        num += 1

c = count()
for n in c:
    print(n)