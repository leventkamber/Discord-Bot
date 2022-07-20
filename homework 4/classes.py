class Entity:
    def __init__(self, name, health):
        self._name = name
        self._health = health
        self._max_health = health

    def is_alive(self):
        if self._health <= 0:
            return False
        else:
            return True

    def get_health(self):
        return self._health

    def take_damage(self, points):
        if points > self.get_health():
            self._health = 0

        else:
            self._health -= points

    def take_healing(self, healing_points):
        if self.get_health() + healing_points > self._max_health:
            self._health = self._max_health
        else:
            self._health += healing_points

        if not self.is_alive():
            return False
        elif self.is_alive():
            return True


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.__nickname = nickname

    def __repr__(self):
        return f'{self._name} the {self.__nickname}'


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.__berserk_factor = berserk_factor

    def atack_enemy(self, attack_points):
        return self.__berserk_factor * attack_points
