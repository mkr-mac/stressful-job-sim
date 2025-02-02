from image import StressImage

class StressAlarmLight(StressImage):
    def __init__(self, image, x, y, clickable = False, action = None):
        self.alarm_state = False
        self.light_on = False
        self.flash_timer_max = 10
        self.flash_timer = self.flash_timer_max
        super().__init__(image, x, y, clickable, action)

    def set_alarm_state(self, state):
        if state == False:
            self.change_pic("alarmlightoff.png")
        self.alarm_state = state

    def update_alarm_light(self):
        if self.alarm_state:
            if self.flash_timer <= 0:
                self.light_on = not self.light_on
                if self.light_on:
                    self.change_pic("alarmlighton.png")
                else:
                    self.change_pic("alarmlightoff.png")
                self.flash_timer = self.flash_timer_max
            else:
                self.flash_timer -= 1

        