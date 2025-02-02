class KeyHandler():

    def __init__(self):
        self.key_states = {
            "left": False,
            "right": False,
        }

    def handle_input(self, event):

        if event.type == pygame.KEYDOWN:        
            # Get key presses
            if event.key == K_LEFT:
                self.key_states["left"] = True
            if event.key == K_RIGHT: 
                self.key_states["right"] = True
        elif event.type == pygame.KEYUP:
            # Get key presses
            if event.key == K_LEFT:
                self.key_states["left"] = False
            if event.key == K_RIGHT: 
                self.key_states["right"] = False

    def get_key_states(self):    
        return self.key_states