import pygame
import button
import random

from  enemy_combat import enemy_scenario as es
from  enemy_combat import  enemy_counter_scenario as ecs


pygame.init()

#game screen window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#game title
pygame.display.set_caption("INFINITY BUGS")

#game font
font = pygame.font.SysFont("arialblack",40)
TEXT_COL = (255,255,255)

#game pause menu
#image path
resume_img = pygame.image.load("assets/button_resume.png").convert_alpha()
option_img = pygame.image.load("assets/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
video_img = pygame.image.load("assets/button_video.png").convert_alpha()
audio_img = pygame.image.load("assets/button_audio.png").convert_alpha()
keys_img = pygame.image.load("assets/button_keys.png").convert_alpha()
back_img = pygame.image.load("assets/button_back.png").convert_alpha()
#button create
resume_button = button.Button(300, 125, resume_img, 1)
option_button = button.Button(300, 250, option_img, 1)
quit_button = button.Button(300, 375, quit_img, 1)
video_button = button.Button(300, 75, video_img, 1)
audio_button = button.Button(300, 200, audio_img, 1)
keys_button = button.Button(300, 325, keys_img, 1)
back_button = button.Button(300, 450, back_img, 1)

#game varibles
game_paused = False
menu_state = "main"
prev_mouse_pos = pygame.mouse.get_pos()
delay_duration = 200
prev_time = pygame.time.get_ticks()
mouse_tracking = False

#game UI function
def write_text(text,font,text_col,x,y):
    line = font.render(text, True, text_col)
    screen.blit(line,(x,y))

# Main game loop
run = True
while run:
    #background color
    screen.fill("black")

    #game paused
    if game_paused:
        #check menu state
        if menu_state == "main":
            if resume_button.draw(screen):
                game_paused = False
            if option_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        #check options menu_state
        elif menu_state == "options":
            if video_button.draw(screen):
                print(random.choice(es))
            if audio_button.draw(screen):
                print(random.choice(ecs))
            if keys_button.draw(screen):
                print("Keys Settings")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        write_text("Mouse Tracking", font, TEXT_COL, 250, 100)
    # #game event check
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_paused = True
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # Start tracking mouse movement when mouse button is pressed
        #     mouse_tracking = True
        #     prev_time = pygame.time.get_ticks()
        # if event.type == pygame.MOUSEBUTTONUP:
        #     # Stop tracking mouse movement when mouse button is released
        #     mouse_tracking = False

    # if mouse_tracking:
    #     current_time = pygame.time.get_ticks()
    #     if current_time - prev_time >= delay_duration:
    #         mouse_position = pygame.mouse.get_pos()
    #         dx = mouse_position[0] - prev_mouse_pos[0]
    #         dy = mouse_position[1] - prev_mouse_pos[1]
    #         direction = ""
    #         if dy > 0:
    #             direction += "Down "
    #         elif dy < 0:
    #             direction += "Up "
    #         if dx > 0:
    #             direction += "Right "
    #         elif dx < 0:
    #             direction += "Left "
    #         if direction:
    #             print("Mouse direction:", direction)
    #         prev_mouse_pos = mouse_position
    #         prev_time = current_time
    pygame.display.update()
pygame.quit()
