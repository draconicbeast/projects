import sys, pygame
import os
pygame.init()
def createitemlist():
    res = []
    item_list = ["Air", "Brick", "Continent", "Dust", "Earth", "Earthquake","Energy","Eruption", "Fire", "Geyser", "Granite", "Gunpowder", "Heat", "Land", "Lava", "Mist", "Mud", "Obsidian", "Pond", "Pressure", "Puddle", "Smoke", "Steam", "Stone", "Time", "Volcano", "Water", "Wind"]
    for i in range

        for path in os.listdir("https://littlealchemy2.com/static/icons/" + ):
            res.append(path)
            print(res)
    for i in range(len(item_list)):
        item_list[i]
    res.sort()
    print(res)
    d = {item_list[0]: pygame.image.load(res[0])}
    for i in range(1, len(item_list)-1):
        d.update({item_list[i]: pygame.image.load(res[i])})
    print(d["Air"])
    return(d)



item_list = ["Air", "Brick", "Continent", "Dust", "Earth", "Earthquake","Energy","Eruption", "Fire", "Geyser", "Granite", "Gunpowder", "Heat", "Land", "Lava", "Mist", "Mud", "Obsidian", "Pond", "Pressure", "Puddle", "Smoke", "Steam", "Stone", "Time", "Volcano", "Water", "Wind"]
d = createitemlist()
size = width, height = 1100, 1100
speed = [0, 0]
black = 180, 180, 180

screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    pygame.display.flip()
    screen.blit(d[item_list[0]], (110,110))


