class Hero:
    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
        self.max_health = health

    def __str__(self) -> str:
        return self.name + " the " + self.nickname

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


h1 = Hero("Name", 100, "Nickname")
