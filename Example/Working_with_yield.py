
def a():
    for i in [27,89,00]:
        yield i

s = a()

print(next(s))
print(next(s))
print(next(s))