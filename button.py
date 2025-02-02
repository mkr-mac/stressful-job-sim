from image import StressImage
from alarmlight import StressAlarmLight as AL

class StressButton(StressImage):
    def __init__(self, image, x, y, clickable = False, action = None):
        self.alarm_state = False
        super().__init__(image, x, y, clickable, action)

        self.alarm_light = AL("alarmlightoff.png", x + 25, y - 50)

    def get_alarm_state(self):
        return self.alarm_state
    
    def alarm(self):
        self.alarm_state = True
        self.alarm_light.set_alarm_state(True)

    def clear_alarm(self):
        self.alarm_state = False
        self.alarm_light.set_alarm_state(False)
    
    def draw(self, DS, camera_offset_x=0):
        super().draw(DS, camera_offset_x)
        self.alarm_light.update_alarm_light()
        self.alarm_light.draw(DS, camera_offset_x)

