class Player():
    def __init__(self):
        self.stress = 0.0
        self.job_security = 0
        self.energy = 1000
        self.difficulty = 1

    def update(self):
        if stress > 1000:
            self.die()

        if self.stress > 0:
            stress -= 1

        if self.stress < 0:
            self.stress = 0

        self.difficulty += .0005
        self.energy += -self.stress


    def increase_stress(self, active_stressors):
        self.stress += active_stressors*self.difficulty

    def die(self):
        print (f"You ded. Your score:{(self.difficulty*1000)}")
