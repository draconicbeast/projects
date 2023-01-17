import sys, pygame
pygame.init()

size = width, height = 1100, 1100
speed = [0, 0]
black = 180, 180, 180

screen = pygame.display.set_mode(size)

ball = pygame.image.load("/Users/brinkpax000/PycharmProjects/keyboard/test/test-resources/images.jpeg")
ballrect = ball.get_rect()
while True:
    ballrect = ballrect.move(speed)
    speed[0] = (pygame.mouse.get_pos()[0] - ballrect.left-(ballrect.right-ballrect.left)/2)
    if speed[0] == 0:
        speed[0] = 1
    else:
        print(pygame.mouse.get_pos()[0] + ballrect.left-(ballrect.right-ballrect.left)/2)
    speed[1] = (pygame.mouse.get_pos()[1] - ballrect.top-(ballrect.bottom-ballrect.top)/2)
    if pygame.mouse.get_pos()[1] != (ballrect.bottom - ballrect.top)/2 and speed[1] == 0:
        speed[1] = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()