def safe_pawns(pawns: set) -> int:

    refPoint = {"a": ["b"], "b": ["a", "c"], "c": ["b", "d"], 
                "d": ["c", "e"], "e": ["d", "f"], "f": ["e", "g"], 
                "g": ["f", "h"], "h": ["g"]}
    pawnCount = 0

    for i in pawns:
        pFile = refPoint[i[0]]
        rankCheck = str(int(i[1]) - 1)

        if i[0] == "a" or i[0] == "h":
            for j in pawns:
                if pFile[0] + rankCheck == j:
                    pawnCount += 1
                    break
        else:
            for j in pawns:
                if pFile[0] + rankCheck == j or pFile[1] + rankCheck == j:
                    pawnCount += 1
                    break

    return pawnCount


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")