import json, random


def run():
    sudoku = getBaseCase()['sudoku']
    randomFactor(sudoku)
    if solve(sudoku):
        for line in sudoku:
            print(line)
    else:
        print("No solution")



def randomFactor(sudoku, n = 20):
    i = 0
    while i < n:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        number = random.randint(1, 9)
        
        if validatePosition(sudoku, (x, y), number):
            sudoku[x][y] = number
            i += 1

def getNextStep(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    
    return -1, -1

def getGrid(pos):
    x, y = pos 
    def valitade(n):
        if n % 3 == 0:
            return n
        elif (n - 1) % 3 == 0:
            return n - 1
        else:
            return n - 2

    return (valitade(x), valitade(y))
    

def validatePosition(sudoku, pos, number):
    x, y = pos

    for i in range(9):
        if sudoku[x][i] == number: return False
        if sudoku[i][y] == number: return False
    
    xGrid, yGrid = getGrid(pos)
    for i in range(xGrid, xGrid+3):
        for j in range(yGrid, yGrid+3):
            if sudoku[i][j] == number:
                return False

    return True

def solve(sudoku):
    pos = getNextStep(sudoku)
    x, y = pos

    if x == -1 and y == -1:
        return True

    else:
        for i in range(1, 10):

            if validatePosition(sudoku, pos, i):
                sudoku[x][y] = i

                complete = solve(sudoku)

                if not complete:
                    sudoku[x][y] = 0

                else:
                    return complete
                
        if sudoku[x][y] == 0:
            return False

def getBaseCase():
    with open("./baseCase.json", "r") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    run()