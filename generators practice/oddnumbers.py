class myiter:
    def __init__(self, n):
        self.i = -1
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        self.i += 2
        if self.i < self.n:
            return self.i
        else:
            raise StopIteration
        
odd = myiter(50)

for num in odd:
    print(num)