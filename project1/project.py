import pygame as pyg
import sys
import random
import time
pyg.init()
pyg.display.set_caption("GGS")
size = width, height = 1000, 1000
black = 180, 180, 180
rock_sel = 0
paper_sel = 0
scissors_sel = 0
screen = pyg.display.set_mode(size)
Lose = pyg.image.load("/Users/brinkpax000/PycharmProjects/keyboard/project1/project-resources/Lose.png")
Win = pyg.image.load("/Users/brinkpax000/PycharmProjects/keyboard/project1/project-resources/Win.png")
Tie = pyg.image.load("/Users/brinkpax000/PycharmProjects/keyboard/project1/project-resources/Tie.png")
rock = pyg.image.load("/Users/brinkpax000/PycharmProjects/keyboard/project1/project-resources/rock.png")
rockrect = rock.get_rect()
paper = pyg.image.load("/Users/brinkpax000/PycharmProjects/keyboard/project1/project-resources/paper.png")
paperrect = paper.get_rect()
scissors = pyg.image.load("/Users/brinkpax000/PycharmProjects/keyboard/project1/project-resources/scissors.png")
scissorsrect = scissors.get_rect()
group = [rock, paper, scissors]
choice_rand = 0
clicked = 0
while True:
    rockrect.move(100, 100)
    paperrect.move(425,100)
    scissorsrect.move(700, 100)
    for event in pyg.event.get():
        if event.type == pyg.QUIT: sys.exit()
        if pyg.mouse.get_pressed()[0] and pyg.mouse.get_pos()[0] > rockrect.left + 100 and pyg.mouse.get_pos()[0] < rockrect.right + 100 and pyg.mouse.get_pos()[1] > rockrect.top + 100 and pyg.mouse.get_pos()[1] < rockrect.bottom + 100 and clicked == 0:
            rock_sel = 1
            paper_sel = 0
            scissors_sel = 0
            choice_rand = random.randint(0, 2)
            clicked = 1
        if pyg.mouse.get_pressed()[0] and pyg.mouse.get_pos()[0] > paperrect.left + 425 and pyg.mouse.get_pos()[0] < paperrect.right + 425 and pyg.mouse.get_pos()[1] > paperrect.top + 100 and pyg.mouse.get_pos()[1] < paperrect.bottom + 100 and clicked == 0:
            paper_sel = 1
            rock_sel = 0
            scissors_sel = 0
            choice_rand = random.randint(0, 2)
            clicked = 1
        if pyg.mouse.get_pressed()[0] and pyg.mouse.get_pos()[0] > paperrect.left + 700 and pyg.mouse.get_pos()[0] < paperrect.right + 700 and pyg.mouse.get_pos()[1] > paperrect.top + 100 and pyg.mouse.get_pos()[1] < paperrect.bottom + 100 and clicked == 0:
            scissors_sel = 1
            rock_sel = 0
            paper_sel = 0
            choice_rand = random.randint(0, 2)
            clicked = 1
    screen.fill(black)
    screen.blit(rock, (100,100))
    if rock_sel == 1:
        screen.blit(rock, (200, 600))
        screen.blit(group[choice_rand], (600, 600))
        if choice_rand == 1:
            screen.blit(Lose, (250, 800))
        if choice_rand == 2:
            screen.blit(Win, (250, 800))
        if choice_rand == 0:
            screen.blit(Tie, (250, 800))
    screen.blit(paper, (425,100))
    if paper_sel == 1:
        screen.blit(paper, (200, 600))
        screen.blit(group[choice_rand], (600, 600))
        if choice_rand == 2:
            screen.blit(Lose, (250, 800))
        if choice_rand == 0:
            screen.blit(Win, (250, 800))
        if choice_rand == 1:
            screen.blit(Tie, (250, 800))
    screen.blit(scissors, (700,100))
    if scissors_sel == 1:
        screen.blit(scissors, (200, 600))
        screen.blit(group[choice_rand], (600, 600))
        if choice_rand == 0:
            screen.blit(Lose, (250, 800))
        if choice_rand == 1:
            screen.blit(Win, (250, 800))
        if choice_rand == 2:
            screen.blit(Tie, (250, 800))
    if clicked == 1:
        clicked = 0
    pyg.display.flip()
    print(rock)