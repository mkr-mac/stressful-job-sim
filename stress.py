 # Example file showing a basic pygame "game loop"
import pygame, sys
from keyhandler import KeyHandler
import scene

def quit():
  pygame.quit()
  sys.exit()

#Screen size constants
SCREENWIDTH = 1280
SCREENHEIGHT = 720
FULLSCREEN = False

#Start Pygame
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
FPS = 60.0
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
  DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
  DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption('Stressfull Job Sim')

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    camera_offset_x = 0
    
    kh = KeyHandler()

    current_scene = scene.desk

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            kh.handle_input(event)

    for obj in current_scene:
      if obj.clickable and obj.checkclick(mousex, mousey, camera_offset_x):
        action = obj.action


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        

        # foreach object in the game
        #

        # flip() the display to put your work on screen
        pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

pygame.quit()


if (__name__ == "__main__"):
    main()