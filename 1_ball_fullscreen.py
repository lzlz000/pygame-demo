import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
fps = 300
speed = [1,1]

pygame.init()
info = pygame.display.Info()
size = width, height = info.current_w, info.current_h
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("pygame-ball")
font = pygame.font.Font("Microsoft Yahei Mono.ttf",100)
ball = font.render("●", True, WHITE)
# ball = pygame.image.load("ball.png")
ballRect = ball.get_rect()
print(ballRect)
ball_interval = 8, 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
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
        speed[0] = -speed[0]
    if ballRect.top < -ball_interval[1] or ballRect.bottom > height+ball_interval[1]:
        speed[1] = -speed[1]

    # 刷新窗口
    screen.fill(BLACK)
    screen.blit(ball,ballRect)
    pygame.display.update()
    clock.tick(fps)

