import pygame
import game_controller
import storage_manager

pygame.init()

WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

# game variable initialize
# board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''


def draw_over():
    pygame.draw.rect(screen, 'black', [50, 50, 300, 100], 0, 10)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (130, 65))
    screen.blit(game_over_text2, (70, 105))

# def haveNoMoreMoves(board):
#     haveMove = False
#     column = []
#     slided = []
#     size = len(board)
#     for j in range(size - 1):
#         for i in range(size - 1):
#             if board[j][i] != 0:
#                 column.append(board[j][i])
#         merge(column, slided)
#
#         for i in range(size):
#             if slided:
#                 board[j][i] = slided.pop(0)
#             else:
#                 board[j][i] = 0
#         for i in range(size - 1):
#             if slided[i] == 0 and slided[i + 1] != 0:
#                 haveMove = True
#             else:
#                 haveMove = False
#         column.clear()
#         slided.clear()
#
#     return haveMove
#
#     # for j in range(len(given) - 1):
#     #     if slided[j] == 0 and slided[j+1] != 0:
#     #         new_pieces(board_values)
#
#     given.clear()
#     # sizeOfTiles = len(tiles)
#     # merged_tiles = []
#     # for i in range(sizeOfTiles):
#     #     if i < sizeOfTiles - 1 and tiles[i] == tiles[i+1]:
#     #         merged_tiles = tiles[i] * 2
#     #
#     #         tiles[i] *= 2
#     #         tiles[i+1] = tiles[i+2]
#     #         tiles[i+2] = 0
#     #         i += 1
#     #
#     #     return tiles
#     # # tiles[i] *= 2
#     # # tiles[i + 1] = tiles [i+2]


# spawn in new pieces randomly when turns start


# draw background for the board
def draw_board(high_score):
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)
    score_text = font.render(f'Score: {game_controller.score}', True, 'black')
    ticks = pygame.time.get_ticks()
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    stop_watch = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
    stopwatch_text = font.render(f'Stopwatch: {stop_watch}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    screen.blit(score_text, (10, 410))
    screen.blit(stopwatch_text, (10, 460))
    screen.blit(high_score_text, (10, 430))
    pass


def draw_pieces(board):
    for i in range(game_controller.BOX_SIZE):
        for j in range(game_controller.BOX_SIZE):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)


# main game loop

# storage_manager.store_high_score(50)
# storage_manager.store_high_score(23)
# storage_manager.store_high_score(58)
# storage_manager.store_high_score(24)
# storage_manager.store_high_score(152)
# storage_manager.store_high_score(84)
# storage_manager.store_high_score(250)
# storage_manager.store_high_score(530)
# storage_manager.store_high_score(540)
# # storage_manager.store_high_score(45)
# storage_manager.store_high_score(2048)
# storage_manager.store_high_score(1024)

game_controller.init_game()
highest_score = storage_manager.read_top_score()

run = True
while run:
    # timer.tick(fps)
    screen.fill('gray')
    draw_board(highest_score)
    draw_pieces(game_controller.board)
    if not game_controller.has_possible_moves():
        storage_manager.store_high_score(game_controller.score)
        draw_over()
        # TODO: draw GAVE OVER

    # if spawn_new or init_count < 2:
    #     game_controller.add_number(board_values)
    #     spawn_new = False
    #     init_count += 1
    if direction != '':
        game_controller.take_turn(direction)
        direction = ''
        spawn_new = True

    # if game_over:
    # draw_over()
    # if high_score > init_high:
    #     file = open('high_score.txt', 'w')
    #     file.write(f'{high_score}')
    #     file.close()
    #     init_high = high_score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            direction = 'QUIT'
            run = False
        if event.type == pygame.KEYUP:
            storage_manager.store_high_score(game_controller.score)
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

    pygame.display.flip()
pygame.quit()
