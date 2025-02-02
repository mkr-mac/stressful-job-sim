from image import StressImage

class StressButton(StressImage):
    def __init__(self, image, x, y, clickable = False, action = None):
        self.alarm_state = False
        super().__init__(image, x, y, clickable, action)

    def get_alarm_state(self):
        return self.alarm_state
    
    def alarm(self):
        self.alarm = True

    def clear_alarm(self):
        self.alarm = False
        