def sun_angle(time):

    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])

    angle = (hour - 6) * 15 + minute * 0.25

    if (0 <= angle <= 180):
        return angle 
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")