import random

class EventDirector():
    def __init__(self):
        self.pace = 2000
        self.stress = 0.0
        self.job_security = 0
        self.energy = 1000
        self.difficulty = 1

    def update(self, scene):
        active_stressors = 0
        for obj in scene:
            if obj.get_alarm_state():
                active_stressors += 1
            if (self.difficulty > random.random()*self.pace):
                obj.alarm()
        
        self.stress += active_stressors*self.difficulty

        if self.stress > 1000:
            self.die()

        if self.stress > 0:
            self.stress -= 1

        if self.stress < 0:
            self.stress = 0

        self.difficulty += .0005
        self.energy += -self.stress

    def die(self):
        print (f"You ded. Your score:{(self.difficulty*1000)}")