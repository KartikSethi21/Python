# WAP that accepts any number of keyboard arguments and prints then in the format key : value 

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name='Kartik',power='lazer')
print_kwargs(name="shaktiman")
print_kwargs(name='Kartik',power='lazer',enemy='Dr.J')


