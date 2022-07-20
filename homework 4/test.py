from classes import Hero, Orc

my_hero = Hero("Heor", 100, "Theor")
my_orc = Orc("Roc", 100, 1.5)

print(my_hero)
print(my_orc.atack_enemy(10))

my_hero.take_damage(my_orc.atack_enemy(10))
print(my_hero.get_health())

my_hero.take_healing(200)
print(my_hero.get_health())
my_hero.take_damage(my_orc.atack_enemy(100))

print(f"Is my hero alive? {my_hero.is_alive()}")
