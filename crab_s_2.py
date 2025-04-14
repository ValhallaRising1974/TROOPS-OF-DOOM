
# crab_s_2.py

class CrabS2:
    def __init__(self):
        self.name = "Rune Crab"
        self.type = "Tank"
        self.hp = 500
        self.quantity = 2

    def absorb(self, damage):
        return max(0, damage - 50)  # absorbs 50 damage by default
