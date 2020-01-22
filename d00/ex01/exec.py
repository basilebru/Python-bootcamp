import sys
len = len(sys.argv)
y = 'input one or more argument'
if len > 1:
	y = sys.argv[1]
	for x in sys.argv[2::]:
		y = y + ' ' + x
print(y.swapcase()[::-1])
