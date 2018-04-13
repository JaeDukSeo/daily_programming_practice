double = lambda x: x**2
triple = lambda x: x * 3
print(double(2))
print(double(34))
print(double(21))

print(triple(21))
print(triple(2))

def good(n):
    return lambda x: x + n
print(good(1)(9))




# -- end code --