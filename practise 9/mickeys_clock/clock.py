import pygame
import os
import datetime 

class Clock:
    def __init__(self):
        current_dir = os.path.dirname(__file__)

        self.face = pygame.image.load(
            os.path.join(current_dir, 'images', 'mainclock.png')
        )

        self.minute_arrow = pygame.image.load(
            os.path.join(current_dir, 'images', 'rightarm.png')
        )

        self.second_arrow = pygame.image.load(
            os.path.join(current_dir, 'images', 'leftarm.png')
        )

    def draw(self, screen):
        my_time = datetime.datetime.now()
        minuteINT = int(my_time.strftime("%M"))
        secondINT = int(my_time.strftime("%S"))

        angleMINUTE = minuteINT * -6 - 25
        angleSECOND = secondINT * -6

        minute = pygame.transform.rotate(self.minute_arrow, angleMINUTE)
        second = pygame.transform.rotate(self.second_arrow, angleSECOND)

        screen.blit(self.face, (-300, -200))

        screen.blit(second, (400 - second.get_width() // 2, 340 - second.get_height() // 2))
        screen.blit(minute, (400 - minute.get_width() // 2, 340 - minute.get_height() // 2))