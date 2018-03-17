# prints a number without any trialing zeros

def no_boring_zeros(n):

    test = str(n) 
    length = len(test) - 1
    num = ""
    zeros = 0
    i = 0

    if test[0] == "0":
        return 0
    else:
        while length >= 0:
            if test[length] == "0":
                zeros += 1
                length -= 1
            else:
                break

    length = len(test) - zeros
       
    while i < length:
        num += test[i]
        i += 1
                    
    return num

# test cases
print(no_boring_zeros(1460)) # expected: 146
print(no_boring_zeros(193000)) # expected: 193
print(no_boring_zeros(0)) # expected: 0
print(no_boring_zeros(1060)) # expected: 106
print(no_boring_zeros(40070)) # expected: 4007