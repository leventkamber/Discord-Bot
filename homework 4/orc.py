class Orc:
    def __init__(self, name, health, berserk_factor):
        self.name = name
        self.health = health
        self.berserk_factor = berserk_factor
        self.max_health = health

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def get_health(self):
        return self.health

    def take_damage(self, points):
        if points > self.get_health():
            self.health = 0

        else:
            self.get_health() - points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif self.is_alive():
            return True

        if self.get_health() + healing_points > self.max_health():
            self.health = self.max_health
        else:
            self.health += healing_points

    def atack_enemy(self, attack_points):
        return self.berserk_factor * attack_points
