def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Liftoff!"

cd = countdown(10)

print(next(cd))
print(next(cd)) 
print(next(cd))  
print(next(cd)) 
print(next(cd))  
print(next(cd))
print(next(cd)) 
print(next(cd))  
print(next(cd)) 
print(next(cd))  
print(next(cd))  
