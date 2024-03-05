import pygame
from pygame.examples.setmodescale import flag

import button
import os
pygame.init()

#game screen window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("INFINITY BUGS")

#game font
font = pygame.font.SysFont("arialblack",40)
TEXT_COL = (255,255,255)
def write_text(text,font,text_col,x,y):
    line = font.render(text, True, text_col)
    screen.blit(line,(x,y))

#game buttons
resume_img = pygame.image.load("assets/button_resume.png").convert_alpha()
option_img = pygame.image.load("assets/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
video_img = pygame.image.load("assets/button_video.png").convert_alpha()
audio_img = pygame.image.load("assets/button_audio.png").convert_alpha()
keys_img = pygame.image.load("assets/button_keys.png").convert_alpha()
back_img = pygame.image.load("assets/button_back.png").convert_alpha()


resume_button = button.Button(300,125, resume_img,1)
option_button = button.Button(300,250, option_img,1)
quit_button = button.Button(300,375, quit_img,1)
video_button = button.Button(300,75, video_img,1)
audio_button = button.Button(300,200, audio_img,1)
keys_button = button.Button(300,325, keys_img,1)
back_button = button.Button(300,450, back_img,1)
#game varibles
game_paused = False
menu_state = "main"
prev_mouse_pos = pygame.mouse.get_pos()

#game start
run = True
while run:
    #backround color
    screen.fill("black")

    #game paused
    if game_paused == True:
        #check menu state
        if menu_state == "main":
            if resume_button.draw(screen):
                game_paused = False
            if option_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        #check options menu_state
        if menu_state == "options":
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Keys Settings")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        write_text("Mouse tracking",font,TEXT_COL,250, 100)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_paused = True
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Start tracking mouse movement when mouse button is pressed
            mouse_tracking = True
            print("Pressed")
            flag =1
        if event.type == pygame.MOUSEBUTTONUP:
            # Stop tracking mouse movement when mouse button is released
            mouse_tracking = False
            print("Unpressed")
            flag = 0
        if flag == 1:
            if event.type == pygame.MOUSEMOTION and mouse_tracking:
                mouse_position = pygame.mouse.get_pos()
                dx= mouse_position[0] - prev_mouse_pos[0]
                dy= mouse_position[1] - prev_mouse_pos[1]

                direction = ""
                if dy > 0:
                    direction += "Xuống "
                elif dy < 0:
                    direction += "Lên "
                if dx > 0:
                    direction += "Phải "
                elif dx < 0:
                    direction += "Trái "

                # Print the direction of movement
                if direction:
                    print("Mouse direction:", direction)

                # Update the previous mouse position
                prev_mouse_pos = event.pos

    pygame.display.update()

pygame.quit()