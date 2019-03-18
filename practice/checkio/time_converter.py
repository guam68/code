def time_converter(time):
    hour = int(time.split(":")[0])
    half = time.split(":")[1]
    minute = half.split(" ")[0]
    period = half.split(" ")[1]
    converted = ""

    if period[0] == "p" and hour < 12:
        hour += 12
        converted = str(hour) + ':' + minute 
    elif hour < 10:
        converted = "0" + str(hour) + ':' + minute
    elif period[0] == "a" and hour == 12:
        converted = "00:00"
    else:
        converted = str(hour) + ':' + minute

    return converted

if __name__ == '__main__':
    # print("Example:")
    # print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")