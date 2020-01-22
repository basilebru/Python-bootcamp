class Vector:
    def __init__(self, argument = None):
        if argument == None:
            print("Please enter an argument")
            exit()
        
        if (isinstance(argument, list) == False
        and isinstance(argument, int) == False and isinstance(argument, tuple) == False):
            print("Please enter a list of floats, a size (int) or a range")
            exit()
        
        if isinstance(argument, list) == True:
            for i in argument:
                if isinstance(i, float) == False:
                    print("List must contain only floats")
                    exit()
            self.values = argument
            self.size = len(argument)

        if isinstance(argument, int) == True:
            self.size = argument
            self.values = [float(i) for i in range(argument)]

        if isinstance(argument, tuple) == True:
            self.size = argument[1] - argument[0]
            self.values = [float(i) for i in range(argument[0], argument[1])]
    
    def __add__(self, add):
        if isinstance(add, int):
            new = [elem + add for elem in self.values]
            return(Vector(new))
        if isinstance(add, Vector):
            if self.size != add.size:
                print("Cant add vectors with different size")
                exit()
            new_values = [self.values[i] + add.values[i] for i in range(self.size)]
            return(Vector(new_values))
    
    def __radd__(self, add):
        if isinstance(add, int):
            new = [elem + add for elem in self.values]
            return(Vector(new))
    
    def __sub__(self, add):
        if isinstance(add, int):
            new = [elem - add for elem in self.values]
            return(Vector(new))
        if isinstance(add, Vector):
            if self.size != add.size:
                print("Cant sub vectors with different size")
                exit()
            new_values = [self.values[i] - add.values[i] for i in range(self.size)]
            return(Vector(new_values))
    
    def __rsub__(self, add):
        if isinstance(add, int):
            new = [elem - add for elem in self.values]
            return(Vector(new))

    def __truediv__(self, add):
        if isinstance(add, int):
            new = [elem / add for elem in self.values]
            return(Vector(new))
    
    def __rtruediv__(self, add):
        if isinstance(add, int):
            new = [elem / add for elem in self.values]
            return(Vector(new))

    def __mul__(self, add):
        if isinstance(add, int):
            new = [elem * add for elem in self.values]
            return(Vector(new))
        if isinstance(add, Vector):
            if self.size != add.size:
                print("Cant dot product vectors with different size")
                exit()
            new_values = [self.values[i] * add.values[i] for i in range(self.size)]
            return(sum(new_values))

    def __rmul__(self, add):
        if isinstance(add, int):
            new = [elem * add for elem in self.values]
            return(Vector(new))

    def __str__(self):
        return("Values: " + str(self.values))

    def __repr__(self):
        return self.values