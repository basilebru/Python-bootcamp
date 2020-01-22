class GotCharacter:
    def __init__(self, al = True, fn = None):
        self.is_alive = al
        self.first_name = fn

class Stark(GotCharacter):
    """poor Starks..."""
    def __init__(self, fna = None, ali = True, rep = None):
        #GotCharacter.__init__(self, is_alive = True, first_name = None)
        super().__init__(al = ali, fn = fna)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"
        self.reputation = rep

    def print_house_words(self):
        print(self.house_words)
    
    def print_house_reputation(self):
        print(self.reputation)

    def die(self):
        self.is_alive = False

class Brunet(GotCharacter):
    """nice class"""
    pass
    number = 12

    def multiply(self):
        self.number = 2 * self.number
