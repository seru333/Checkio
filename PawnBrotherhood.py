def safe_pawns(pawns: set) -> int:
    count = 0
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    print(pawns_indexes)
    for y in pawns_indexes:
        for z in pawns_indexes:
            if (y[0] == z[0] +1 and y[1] == z[1] + 1) or (y[0] == z[0] +1 and y[1] == z[1] - 1):
                count += 1
                print("y=", y , " z=", z)
                print("count = ", count)
                break
    print("Final count = ", count)
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
