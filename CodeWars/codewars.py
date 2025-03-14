import codewars_test as test

def validate_battlefield(field):
    for x in range(1,9):
        for y in range(1, 9):
            if field[x][y] == 1:
                if field[x-1][y-1] == 1 or field[x-1][y+1] == 1 or field[x+1][y-1] == 1 or field[x+1][y+1] == 1:
                    return False
                if (field[x-1][y] == 1 or field[x+1][y] == 1) and (field[x][y-1] == 1 or field[x][y+1] == 1):
                    return False

    ships = [0, 0, 0, 0, 0]
    for i in range(10):
        shipX = 0
        shipY = 0
        for j in range(10):
            if field[i][j] == 1:
                shipX += 1
            else:
                if shipX > 4:
                    return False
                if shipX > 0:
                    ships[shipX] += 1
                    shipX = 0

            if field[j][i] == 1:
                shipY += 1
            else:
                if shipY > 4:
                    return False
                if shipY > 0:
                    ships[shipY] += 1
                    shipY = 0
        if shipX > 4 or shipY > 4:
            return False
        if shipX > 0:
            ships[shipX] += 1
        if shipY > 0:
            ships[shipY] += 1

    EXPECTED_SHIPS = [0, 24, 3, 2, 1]
    if ships != EXPECTED_SHIPS:
        return False    
    
    return True

@test.describe("Sample test")
def test():
    @test.it("Should return True for valid battlefield")
    def test_valid_battlefield():
        battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        test.assert_equals(validate_battlefield(battleField), True, "Nope, something is wrong!");