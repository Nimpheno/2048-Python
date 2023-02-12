import pygame
import game_controller as game
import storage_manager
import view


game.init_game()
highest_score = storage_manager.read_top_score()

direction = ''
has_completed_game = False
run = True
elapsed_time = 0

# main game loop
while run:
    if not has_completed_game:
        elapsed_time = game.get_elapsed_time()

    view.draw_board(game.board, highest_score, game.score, elapsed_time)
    if game.is_win_the_game():
        view.draw_win()
        game.check_high_score_reached()
        has_completed_game = True

    if not game.has_possible_moves():
        view.draw_over()
        game.check_high_score_reached()
        has_completed_game = True

    if direction != '':
        game.take_turn(direction)
        direction = ''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            direction = 'QUIT'
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            if event.key == pygame.K_t:
                view.switch_mood()
            if event.key == pygame.K_n:
                game.init_game()
                has_completed_game = False

    pygame.display.flip()
pygame.quit()
