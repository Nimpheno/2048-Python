import pygame
import game_controller
import storage_manager
import view


direction = ''
stored_high_score = False

game_controller.init_game()
highest_score = storage_manager.read_top_score()

run = True
# main game loop
while run:
    view.draw_board(game_controller.board, highest_score, game_controller.score)
    if not game_controller.has_possible_moves():
        view.draw_over()
        if not stored_high_score:
            storage_manager.store_high_score(game_controller.score)
            stored_high_score = True


    if direction != '':
        game_controller.take_turn(direction)
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
            if event.key == pygame.K_n:
                game_controller.init_game()
                stored_high_score = False

    pygame.display.flip()
