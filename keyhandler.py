import pygame

class KeyHandler():

    def __init__(self):
        self.key_states = {
            "left": False,
            "right": False,
        }
        self.mouse_state = {
            "lmb": False,
            "framelmb": False,
            "pos": pygame.mouse.get_pos()
        }

    def handle_input(self, event):

        # handle key events
        if event.type == pygame.KEYDOWN:        
            # Get key presses
            if event.key == pygame.K_LEFT:
                self.key_states["left"] = True
            if event.key == pygame.K_RIGHT: 
                self.key_states["right"] = True
        elif event.type == pygame.KEYUP:
            # Get key unpresses
            if event.key == pygame.K_LEFT:
                self.key_states["left"] = False
            if event.key == pygame.K_RIGHT: 
                self.key_states["right"] = False
        
        # handle mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # setting frame lmb to true for one frame for singe fire
            if self.mouse_state["lmb"] == False:
                self.mouse_state["framelmb"] = True

            self.mouse_state["lmb"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse_state["lmb"] = False
        self.mouse_state["pos"] = pygame.mouse.get_pos()

    def get_key_states(self):    
        return self.key_states

    def get_mouse_state(self):
        return self.mouse_state