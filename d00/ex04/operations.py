import sys
len = len(sys.argv)
if len != 3:
    print("""
    InputError: too many argments
    Usage: python operations.py
    Example:
    python operations.py 10 3
    """)
    sys.exit()
a = sys.argv[1]
b = sys.argv[2]
if a.isdigit() != True or b.isdigit() != True:
    print("""
    InputError: only numbers
    Usage: python operations.py
    Example:
    python operations.py 10 3
    """)
    sys.exit()
print("Sum:           ", int(a) + int(b))
print("Difference:    ", int(a) - int(b))
print("Product:       ", int(a) * int(b))
if int(b) != 0:
    print("Quotient:      ", int(a) / int(b))
else:
    print("Quotient:       ERROR (div by zero)")
if int(b) != 0:
    print("Remainder:     ", int(a) % int(b))
else:
    print("Remainder:      ERROR (div by zero)")
