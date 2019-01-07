from typing import List

def checkio(game_result: List[str]) -> str:
    rotate = list(zip(game_result[0], game_result[1], game_result[2]))
    answer = 'D'
    # diagonal
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != ".":
        answer = game_result[0][0]
    elif game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != ".":
        answer = game_result[2][0]
    else:
        # Horizontal
        for i in game_result:
            if i[0] == i[1] == i[2] and i[0] != ".":
                answer = i[0]
        if answer == "D":
            # vertical
            for i in rotate:
                if i[0] == i[1] == i[2] and i[0] != ".":
                    answer = i[0]
    print("answer = ", answer)
    return answer

if __name__ == '__main__':
    # print("Example:")
    # print(checkio(["X.O",
    #                "XX.",
    #                "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
