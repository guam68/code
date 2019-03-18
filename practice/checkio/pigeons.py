def checkio(number):
    n = 1 
    birds = 1

    while number >= 0:
        number = number - birds 
        if number == 0:
            print(birds)
            return birds 
        elif number < 0 and (birds + number) < birds - n:
            return birds - n
        elif number < 0:
            print("help!\t", end="", flush=True),
            print(birds + number)
            return birds + number 
        else:
            n += 1
            birds += n
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    assert checkio(3) == 2, "5th example"