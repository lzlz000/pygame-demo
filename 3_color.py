import pygame,sys


class Status:
    def __init__(self):
        self.active = True

    def change(self, status):
        self.active = status

pygame.init()
# flag参数指定显示方式 pygame.RESIZABLE 可调节大小 pygame.NOFRAME 无边框 pygame.FULLSCREEN 全屏
print(pygame.display.Info())
pygame.display.set_mode((600,400))
print(pygame.display.Info())

pygame.display.set_caption("pygame-哈哈哈")  # set_caption里设置icon在部分操作系统不支持
flower = pygame.image.load("flower.png")  # 设置icon
pygame.display.set_icon(flower)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    if pygame.display.get_active():  # 窗口没有被最小化
        print("active")
    else:
        print("icon")
    pygame.display.update()



