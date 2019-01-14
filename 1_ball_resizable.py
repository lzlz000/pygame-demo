import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
fps = 300
speed = [1,1]

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
print(pygame.display.Info())
pygame.display.set_caption("pygame-ball")
font = pygame.font.Font("Microsoft Yahei Mono.ttf",100)
ball = font.render("●", True, WHITE)
# ball = pygame.image.load("ball.png")
ballRect = ball.get_rect()
print(ballRect)
ball_interval = 8, 30
clock = pygame.time.Clock()
changeX = False
changeY = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if event.key == pygame.K_LEFT:
                speed[0] = 0 if speed[0]== 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0]> 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1]> 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = 0 if speed[1]== 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
    ballRect = ballRect.move(speed)
    if ballRect.left < -ball_interval[0] or ballRect.right > width+ball_interval[0]:
        if not changeX:
            speed[0] = -speed[0]
        changeX = True
    else:
        changeX = False
    if ballRect.top < -ball_interval[1] or ballRect.bottom > height+ball_interval[1]:
        if not changeY:
            speed[1] = -speed[1]
        changeY = True
    else:
        changeY = False

    # 刷新窗口
    screen.fill(BLACK)
    screen.blit(ball,ballRect)
    pygame.display.update()
    clock.tick(fps)

