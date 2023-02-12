import random
import copy

BOX_SIZE = 4
INITIAL_TILE = 2
FINAL_TILE = 2048

score = 0
board = []


def init_game():
    global board
    global score
    board = [[0 for _ in range(BOX_SIZE)] for _ in range(BOX_SIZE)]
    score = 0
    add_number()
    add_number()


# take your turn based on direction
def take_turn(direction):
    previous_board = copy.deepcopy(board)

    if direction == 'UP':
        slide_up()
    elif direction == "DOWN":
        slide_down()
    elif direction == "RIGHT":
        slide_right()
    elif direction == "LEFT":
        slide_left()

    if __has_empty_places and previous_board != board:
        add_number()


def has_possible_moves():
    # global board
    # board = [
    #     [2, 4, 8, 16],
    #     [4, 8, 16, 32],
    #     [2, 4, 8, 16],
    #     [4, 8, 16, 32],
    # ]

    if __has_empty_places():
        return True

    for x in range(BOX_SIZE):
        for y in range(BOX_SIZE - 1):
            if board[x][y] == board[x][y + 1]:
                return True

    for x in range(BOX_SIZE - 1):
        for y in range(BOX_SIZE):
            if board[x][y] == board[x + 1][y]:
                return True
    return False


def slide_right():
    row = []
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE - 1, -1, -1):
            if board[i][j] != 0:
                row.append(board[i][j])

        __merge(row)

        for j in range(BOX_SIZE - 1, -1, -1):
            if len(row) != 0:
                board[i][j] = row.pop(0)
            else:
                board[i][j] = 0
        row.clear()


def slide_down():
    column = []
    for j in range(BOX_SIZE):
        for i in range(BOX_SIZE - 1, -1, -1):
            if board[i][j] != 0:
                column.append(board[i][j])
        __merge(column)

        for i in range(BOX_SIZE - 1, -1, -1):
            if len(column):
                board[i][j] = column.pop(0)
            else:
                board[i][j] = 0
        column.clear()


def slide_up():
    column = []
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if board[j][i] != 0:
                column.append(board[j][i])
        __merge(column)

        for j in range(BOX_SIZE):
            if len(column) != 0:
                board[j][i] = column.pop(0)
            else:
                board[j][i] = 0
        column.clear()


def slide_left():
    row = []
    for j in range(BOX_SIZE):
        for i in range(BOX_SIZE):
            if board[j][i] != 0:
                row.append(board[j][i])
        __merge(row)

        for i in range(BOX_SIZE):
            if len(row) != 0:
                board[j][i] = row.pop(0)
            else:
                board[j][i] = 0
        row.clear()


def __merge(given):
    global score
    for i in range(len(given)):
        if i < len(given) - 1 and given[i] == given[i + 1]:
            merged_tile = given[i] * 2
            given[i] = merged_tile
            given.pop(i + 1)
            given.append(0)
            score += merged_tile


def add_number():
    coordinates = __get_empty_places_coordinates()
    index = random.randint(0, len(coordinates) - 1)
    target_coordinate = coordinates[index]
    row = target_coordinate[0]
    col = target_coordinate[1]

    if random.randint(1, 10) == 10:
        board[row][col] = INITIAL_TILE * 2
    else:
        board[row][col] = INITIAL_TILE


def is_win_the_game():
    win = False
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if board[i][j] == 2048:
                win = True


def __get_empty_places_coordinates():
    coordinates = []
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if board[i][j] == 0:
                coordinates.append([i, j])
    return coordinates


def __has_empty_places():
    return len(__get_empty_places_coordinates()) != 0
