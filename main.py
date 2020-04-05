import sys
sys.path.append(".")

import time
from source_package.main_classes.hero import Hero
from source_package.main_classes.dungeon import Dungeon
from source_package.main_classes.weapon import Weapon
from source_package.main_classes.spell import Spell
import pygame


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1000 / 2), (500 / 2))
    dis.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)
    pygame.quit()


map = Dungeon("level1.txt")
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip(w)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=200)
h.learn(s)
# print(map.map[0][1])
pygame.init()
white_hero = (255, 255, 255)

enemy_img = pygame.image.load('enemy.png')
hero_img = pygame.image.load("hero.jpg")
treasure_img=pygame.image.load("treasure.png")
# black_enemy = (0, 0, 0)
red_treasure = (255, 0, 0)
gray_wall = (138, 138, 92)
dis = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Dungeons And Pythons')


while len(map.spawn_locations) > 0:
    game_over = False
    map.set_obstacle_location()
    map.set_enemy_location()
    map.set_treasure_location()
    map.set_gateway_location()
    map.spawn(h)
    hero_x = map.hero.location[0]
    hero_y = map.hero.location[1]
    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.K_q:
                message_display("Quit")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    map.move_hero("left")

                elif event.key == pygame.K_RIGHT:
                    map.move_hero("right")

                elif event.key == pygame.K_UP:
                    map.move_hero("up")

                elif event.key == pygame.K_DOWN:
                    map.move_hero("DOWN")

                elif event.key == pygame.K_SPACE:
                    map.hero_attack(by="spell")

        hero_x = map.hero.location[0]
        hero_y = map.hero.location[1]
        dis.fill((0, 102, 0))
        if map.hero.location == map.gateway_location[0]:
            game_over = True
        if not map.hero.is_alive():
            message_display("GAME OVER")
        for wall in map.obstacle_localtions:
            pygame.draw.rect(dis, gray_wall, [wall[1], wall[0], 100, 100])

        for treasure in map.treasure_locations:
            # pygame.draw.rect(dis, red_treasure, [treasure[1], treasure[0], 100, 100])
            dis.blit(treasure_img,(treasure[1], treasure[0]))
        for enemy in map.enemy_locations:
            # pygame.draw.rect(dis, black_enemy, [enemy[1], enemy[0], 100, 100])
            dis.blit(enemy_img,(enemy[1],enemy[0]))
        pygame.draw.rect(dis, (139, 69, 19), [map.gateway_location[0][1], map.gateway_location[0][0], 100, 100])
        dis.blit(hero_img, (hero_y, hero_x))
        pygame.display.update()

message_display("GOOD GAME")
pygame.quit()
