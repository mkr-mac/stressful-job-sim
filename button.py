from image import StressImage

class StressButton(StressImage):
    def __init__(self, image, x, y, clickable = False, action = None):
        super().__init__(image, x, y, clickable, action)