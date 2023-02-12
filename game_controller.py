import random


# TODO: replace magic numbers with BOX_SIZE
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
    add_numberXXX()
    add_numberXXX()


# take your turn based on direction
def take_turn(direction):
    # TODO add number if possible
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if board[i][j] == 0 and __merge() == True:
                if direction == 'UP':
                    slide_up()
                elif direction == "DOWN":
                    slide_down()
                elif direction == "RIGHT":
                    slide_right()
                elif direction == "LEFT":
                    slide_left()
                if len(__get_empty_places_coordinates()) == 0:
                    return
                else:
                    add_numberXXX()
    # for i in range(BOX_SIZE):
    #     for j in range(BOX_SIZE):
    #         if board[i][j] == 0:
    #             add_numberXXX()
    #             return


def has_possible_moves():
    if __has_empty_places():
        return True

    for x in range(BOX_SIZE):
        for y in range(BOX_SIZE - 1):
            if board[x][y] == board[x][y + 1]:
                return True

    for y in range(BOX_SIZE):
        for x in range(BOX_SIZE-1):
            if board[x][y] == board[x + 1][y]:
                return True
    return False


def slide_right():
    row = []
    slided = []
    size = len(board)
    for i in range(size):
        for j in range(size - 1, -1, -1):
            if board[i][j] != 0:
                row.append(board[i][j])
        __merge(row, slided)

        for j in range(size - 1, -1, -1):
            if slided:
                board[i][j] = slided.pop(0)
            else:
                board[i][j] = 0
        row.clear()
        slided.clear()


def slide_down():
    column = []
    slided = []
    size = len(board)
    for j in range(size):
        for i in range(size - 1, -1, -1):
            if board[i][j] != 0:
                column.append(board[i][j])
        __merge(column, slided)

        for i in range(size - 1, -1, -1):
            if slided:
                board[i][j] = slided.pop(0)
            else:
                board[i][j] = 0
        column.clear()
        slided.clear()


def slide_up():
    column = []
    slided = []
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[j][i] != 0:
                column.append(board[j][i])
        __merge(column, slided)

        for j in range(size):
            if slided:
                board[j][i] = slided.pop(0)
            else:
                board[j][i] = 0
        column.clear()
        slided.clear()


def slide_left():
    row = []
    slided = []
    size = len(board)
    for j in range(size):
        for i in range(size):
            if board[j][i] != 0:
                row.append(board[j][i])
        __merge(row, slided)

        for i in range(size):
            if slided:
                board[j][i] = slided.pop(0)
            else:
                board[j][i] = 0
        row.clear()
        slided.clear()


def add_number(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, BOX_SIZE - 1)
        col = random.randint(0, BOX_SIZE - 1)
        if board[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        full = True
    return board, full


def add_numberXXX():
    coordinates = __get_empty_places_coordinates()
    index = random.randint(0, len(coordinates) - 1)
    target_coordinate = coordinates[index]
    row = target_coordinate[0]
    col = target_coordinate[1]

    if random.randint(1, 10) == 10:
        board[row][col] = INITIAL_TILE * 2
    else:
        board[row][col] = INITIAL_TILE
  

# def get_empty_coordinates():
#     empty_coordinates = []
#     for x in range(BOX_SIZE):
#         for y in range(BOX_SIZE):
#             if board[x][y] == 0:
#                 empty_coordinates.append((x, y))
#     return empty_coordinates


def __merge(given, slided):
    global score
    for i in range(len(given)):
        if i < len(given) - 1 and given[i] == given[i + 1]:
            merged_tile = given[i] * 2
            slided.append(merged_tile)
            given.pop(i + 1)
            given.append(0)
            score += merged_tile
            # new_pieces(board_values)
            # if slided[i] == 0 and slided[i + 1] != 0:
            #     new_pieces(board_values)
        else:
            slided.append(given[i])
            # if slided[i] == 0 and slided[i + 1] == 0:
            #     new_pieces(board_values)


def __get_empty_places_coordinates():
    coordinates = []
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if board[i][j] == 0:
                coordinates.append([i, j])
    return coordinates


def __has_empty_places():
    return len(__get_empty_places_coordinates()) == 0
