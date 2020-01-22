import sys
if len(sys.argv) != 2:
    print("ERROR")
else:
    try:
        n = (int)(sys.argv[1])
    except ValueError:
        print("ERROR")
    else:
        if n == 0:
            print("I'm zero")
        else:
            n = n % 2
            if n == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
