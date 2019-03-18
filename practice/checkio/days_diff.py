from datetime import date
def days_diff(date1, date2):
    # * in *date2 is used to take a sequence and return it in
    # the form of positional arguments (passing parameters) 
    return abs(date(date1[0], date1[1], date1[2]) - date(*date2)).days

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238