class Warrior:
    pass
    health = 50
    attack = 5
    is_alive = True

class Knight(Warrior):
    pass
    attack = 7

def fight(unit_1, unit_2):
    round = 1
    winner = True
    while unit_1.health > 0 and unit_2.health > 0:
        if round % 2 != 0:
            unit_2.health -= unit_1.attack
        if round % 2 == 0:
            unit_1.health -= unit_2.attack
        print("round", round, "P1 health =", unit_1.health, "P2 health =", unit_2.health)
        round += 1
    if unit_1.health < 1:
        unit_1.is_alive = False
        winner = False
    if unit_2.health < 1:
        unit_2.is_alive = False
    print("P1", unit_1.is_alive, "P2", unit_2.is_alive)
    print("winner", winner)
    return winner

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
