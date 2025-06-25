def increment(n):
    return lambda x:x+n

f=increment(3)
print(f)
print(increment(5))