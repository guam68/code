# Takes a number and rearranges the digits to attain the largest possible number

def super_size(n):

    num = str(n)
    digits = []

    for i in num:
        digits.append(i)

    digits.sort(reverse = True)
    num = ""

    for i in digits:
        num += i
        
    print (num)
    return (int(num))
    

super_size(159753)

