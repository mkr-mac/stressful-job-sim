class KeyHandler():

    def __init__(self):
        self.key_states = {
            "left": False,
            "right": False,
        }

    def get_key_states(self):

        self.key_states = {
            "left": False,
            "right": False,
        }

        # Get key presses
        if event.key == K_LEFT:
            self.key_states["left"] = True
        if event.key == K_RIGHT: 
            self.key_states["right"] = True

        return self.key_states