from statistics import StatisticsError, mode

def checkio(text: str) -> str:

    stripped_text = []

    for i in text:
        if i.isalpha():
            stripped_text.append(i.lower())

    try:
        most = mode(stripped_text)
    except StatisticsError:
        most = sorted(stripped_text)
        most = max(most, key = most.count)

    return most