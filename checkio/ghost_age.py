from math import sqrt

def checkio(opacity):
    o = 10000

    for i in range(0, 5000):
        isFib = False

        for j in range(0,20):
            fn = int((((1 + sqrt(5))/2)**j - ((1 - sqrt(5))/2)**j) / sqrt(5))

            if i == fn:
                o -= i
                isFib = True
                break

        if isFib == False:
            o += 1

        if opacity == o:
            return i



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"