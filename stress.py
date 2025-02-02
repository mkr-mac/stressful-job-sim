 # Example file showing a basic pygame "game loop"
import pygame, sys
from keyhandler import KeyHandler
import scene
import button

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

    #Start Pygame
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    FPS = 60.0
    fpsClock  = pygame.time.Clock()

    camera_offset_x = 0
    
    kh = KeyHandler()

    current_scene = scene.desk()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            kh.handle_input(event)


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        mouse_state = kh.get_mouse_state()
        for obj in current_scene:
            if obj.clickable and obj.checkclick(mouse_state["pos"][0], mouse_state["pos"][1], camera_offset_x) and mouse_state["framelmb"] == True:
                obj.action()
                if type(obj) is button.StressButton:
                    obj.change_pic("buttondown.png")
                mouse_state["framelmb"] = False
            elif obj.clickable and not obj.checkclick(mouse_state["pos"][0], mouse_state["pos"][1], camera_offset_x) or mouse_state["lmb"] == False:
                if type(obj) is button.StressButton:
                    obj.change_pic("buttonup.png")

            obj.draw(DS, camera_offset_x)

        key_states = kh.get_key_states()
        # Hande camera movement
        if key_states["right"]:
            camera_offset_x += 1
        if key_states["left"]:
            camera_offset_x -= 1
            
        # RENDER YOUR GAME HERE
        

        # foreach object in the game
        #

        # flip() the display to put your work on screen

        pygame.display.update()
        fpsClock.tick(FPS)
    
    pygame.quit()


if (__name__ == "__main__"):
    main()