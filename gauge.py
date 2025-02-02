from image import StressImage

class StressGauge():
    def __init__(self, x, y):
        self.face = StressImage("gaugeface.png", x, y)
        self.needle = StressImage("gaugeneedle.png", x, y)
        self.front_face = StressImage("gaugefacefront.png", x, y)

        self.needle_pos = 0.0
        self.needle.rotate(-self.needle_pos * 1.8)

        self.clickable = False
    
    def set_needle_pos(self, newpos):
        self.needle_pos = newpos
        self.needle.rotate(-self.needle_pos * 1.8)

    def draw(self, DS, camera_offset_x=0):
        self.face.draw(DS, camera_offset_x)
        self.needle.draw(DS, camera_offset_x)
        self.front_face.draw(DS, camera_offset_x)
    
    def checkclick(self):
        return False
    
    def update(self):
        self.set_needle_pos(self.needle_pos + .01)

    def get_alarm_state(self):
        return self.needle_pos > 50
    
    def alarm(self):
        self.set_needle_pos(self.needle_pos + 10)