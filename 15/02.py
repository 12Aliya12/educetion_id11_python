def num_digits(number):
    s = 0
    for i in number:
        s +=1
    print(s)


number = list(str(input()))
num_digits(number)