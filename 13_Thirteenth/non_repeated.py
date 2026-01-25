# print first character with count 1 => 1st non duplicating character

iu = "cjnsdlkcmdsklndchdslz"

for char in iu:
    print(f"char {char}",x:=iu.count(char))
    if x ==1:
        print(f"char with 1 count is {char}",x)
        break