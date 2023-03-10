import pygame
import view_settings as settings

pygame.init()
screen = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
pygame.display.set_caption('2048')
FONT = pygame.font.Font('freesansbold.ttf', 24)
colors = settings.DAY_MOOD_COLORS


def switch_mood():
    global colors
    colors = settings.NIGHT_MOOD_COLORS if colors == settings.DAY_MOOD_COLORS else settings.DAY_MOOD_COLORS


def draw_board(board, high_score, current_score, elapsed_time):
    screen.fill(settings.BG_FILL_COLOR)
    pygame.draw.rect(screen, colors['BG'], [0, 0, 400, 400], 0, 10)
    score_text = FONT.render(f'Score: {current_score}', True, 'black')
    stopwatch_text = FONT.render(f'Stopwatch: {elapsed_time}', True, 'black')
    high_score_text = FONT.render(f'High Score: {high_score}', True, 'black')
    day_and_dark_mood_text = "Press T for dark/day mood"
    day_and_dark_mood = FONT.render(f'{day_and_dark_mood_text}', True, 'black')
    new_game_text = "Press N for new game"
    new_game = FONT.render(f'{new_game_text}', True, 'black')
    screen.blit(score_text, (10, 410))
    screen.blit(stopwatch_text, (10, 483))
    screen.blit(high_score_text, (10, 445))
    screen.blit(new_game, (10, 520))
    screen.blit(day_and_dark_mood, (10, 558))
    __draw_pieces(board)


def draw_win():
    __draw_final_text("YOU WON!")


def draw_over():
    __draw_final_text("GAME OVER!")


def __draw_final_text(text):
    pygame.draw.rect(screen, 'black', [30, 50, 360, 90], 0, 10)
    final_text = FONT.render(text, True, 'white')
    final_text2 = FONT.render('Press N to start a new game', True, 'white')
    screen.blit(final_text, (135, 65))
    screen.blit(final_text2, (50, 105))


def __draw_pieces(board):
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            value = board[i][j]
            if value > 8:
                value_color = colors['LIGHT_TEXT']
            else:
                value_color = colors['DARK_TEXT']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['OTHER']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)
