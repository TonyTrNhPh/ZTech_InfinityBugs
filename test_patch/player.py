import time
from time import sleep

import pygame
from button import Button as bt

class Player:
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size = size
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button_number = i * 3 + j + 1
                button = bt(self.x + j * self.size, self.y + i * self.size,(0,0,0), str(button_number))
                self.buttons.append(button)

    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface)

    def handle_event(self, key):
        if key == pygame.K_KP1:
            self.buttons[0].selected()
        elif key == pygame.K_KP2:
            self.buttons[1].selected()
        elif key == pygame.K_KP3:
            self.buttons[2].selected()
        elif key == pygame.K_KP4:
            self.buttons[3].selected()
        elif key == pygame.K_KP5:
            self.buttons[4].selected()
        elif key == pygame.K_KP6:
            self.buttons[5].selected()
        elif key == pygame.K_KP7:
            self.buttons[6].selected()
        elif key == pygame.K_KP8:
            self.buttons[7].selected()
        elif key == pygame.K_KP9:
            self.buttons[8].selected()

    def array_handle(self, array):
        for scene in array:
            for num in scene:
                self.buttons[num - 1].selected()
                pygame.display.flip()
                print(num)
                time.sleep(2)


        


