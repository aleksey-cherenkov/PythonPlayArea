def sudoku_solver(puzzle):

    def available_cell_values(x, y, puzzle):
        availableCells = set(range(1, 10))
        for i in range(9):
            availableCells.discard(puzzle[y][i])
            availableCells.discard(puzzle[i][x])
        
        squareX = x // 3 * 3
        squareY = y // 3 * 3
        for i in range(squareX, squareX + 3):
            for j in range(squareY, squareY + 3):
                availableCells.discard(puzzle[j][i])

        return availableCells
    
    def check_puzzle(x, y, puzzle, solution):
        if x == 9:
            x, y = 0, (y + 1) % 9
            if y == startY:
                if solution:
                    return "Multiple solutions"
                else:
                    return [puzzle[j].copy() for j in range(9)]

        if puzzle[y][x] != 0:
            return check_puzzle(x + 1, y, puzzle, solution)

        availableCells = available_cell_values(x, y, puzzle)

        for d in availableCells:
            puzzle[y][x] = d
            result = check_puzzle(x + 1, y, puzzle, solution)
            if result:
                if isinstance(result, list):
                    solution = result
                else:
                    return result

        puzzle[y][x] = 0
        
        return solution

    if len(puzzle) != 9 or any(len(puzzle[y]) != 9 for y in range(9)) or any(puzzle[y][x] > 9 or puzzle[y][x] < 0 for x in range(9) for y in range(9)):
        return 'Invalid grid'

    filledInRows = [sum(int(puzzle[y][x] != 0) for x in range(9)) for y in range(9)]
    startY = filledInRows.index(max(filledInRows))

    solution = check_puzzle(0, startY, puzzle, None)
    return solution

puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8], 
          [0, 8, 0, 0, 9, 0, 0, 3, 0], 
          [2, 0, 0, 0, 0, 5, 4, 0, 0], 
          [4, 0, 0, 0, 0, 1, 8, 0, 0], 
          [0, 3, 0, 0, 7, 0, 0, 4, 0], 
          [0, 0, 7, 9, 0, 0, 0, 0, 3], 
          [0, 0, 8, 4, 0, 0, 0, 0, 6], 
          [0, 2, 0, 0, 5, 0, 0, 8, 0], 
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]
# puzzle = [[5, 0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 4, 0, 2, 0, 8, 0, 6, 0],
#           [0, 0, 3, 0, 0, 0, 0, 0, 5],
#           [9, 0, 6, 0, 7, 0, 4, 0, 3],
#           [0, 0, 0, 4, 0, 0, 2, 0, 0],
#           [0, 7, 0, 0, 2, 3, 0, 1, 0],
#           [0, 3, 0, 7, 0, 0, 0, 5, 0],
#           [0, 0, 7, 0, 0, 5, 0, 0, 0],
#           [4, 0, 5, 0, 1, 0, 7, 0, 8]]
# puzzle = [[9,0,6,0,7,0,4,0,3],
#             [0,0,0,4,0,0,2,0,0],
#             [0,7,0,0,2,3,0,1,0],
#             [5,0,0,0,0,0,1,0,0],
#             [0,4,0,2,0,8,0,6,0],
#             [0,0,3,0,0,0,0,0,5],
#             [0,3,0,7,0,0,0,5,0],
#             [0,0,7,0,0,5,0,0,0],
#             [4,0,5,0,1,0,7,0,8]];
print(sudoku_solver(puzzle))
# a = [1,2,3]
# b = a.copy()
# print(a==b)
# a[1] = 5
# b[1] = 7
# print(a==b)
# print(a,b)
