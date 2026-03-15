def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(11):
    print(num)

def demo_yield():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")
gen = demo_yield()

print(next(gen))
print(next(gen))