from random import randint

board = []

for x in range(4):
    board.append(["O"] * 4)

ships = []

for i in range(0, 3):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)
    ships.append([ship_row, ship_col])

print('1) Легкий: 12 попыток')
print('2) Средний: 8 попыток')
print('3) Сложный: 4 попытки')
print('4) Невозможный: 2 попытки')
level = int(input('Выберите уровень сложности'))

attempts = 10
if level == 1:
    attempts = 12
elif level == 2:
    attempts = 8
elif level == 3:
    attempts = 4
elif level == 4:
    attempts = 2

print("Начнем игру в Морской бой!")
for row in board:
    print((" ").join(row))

for turn in range(attempts):
    print("Ход: ", turn)
    guess_row = int(input("Строка 0-3:"))
    guess_col = int(input("Столбец 0-3:"))

    hit = 0
    for i in range(0, len(ships)):
        if (ships[i] == [guess_row, guess_col]):
            hit = 1
            del ships[i]
            board[guess_row][guess_col] = "S"
            break

    if hit > 0:
        print("Поздравляю, ты потопил мой корабль!")
        if len(ships) == 0:
            print('Вы победили!')
    else:
        if (guess_row < 0 or guess_row > len(board)) or (guess_col < 0 or guess_col > len(board)):
            print("Oops, эти координаты не в нашем океане.")
        elif (board[guess_row][guess_col] == "X"):
            print("Эти координаты вы уже называли.")
        else:
            print("Мимо!")
            board[guess_row][guess_col] = "X"

    for row in board:
        print((" ").join(row))

    if turn == attempts - 1:
        print("Игра окончена! Я уплываю в закат!")