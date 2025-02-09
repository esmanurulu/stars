import random
import pygame

pygame.init()

X=600
Y=600

screen = pygame.display.set_mode((X, Y))  # window
pygame.display.set_caption("✧stars✧") 

W = (255, 255, 255)

star_img = pygame.image.load("star.png")
star_img = pygame.transform.scale(star_img, (30, 30)) 

class Stars:
    def __init__(self):
        self.size = Y
        self.speed = random.uniform(1, 3)
        self.x = random.randint(50, X - 50)
        self.y = Y - random.randint(20, 100)

    def draw(self):
        screen.blit(star_img, (star.x, star.y))
        
    def movement(self):
        self.y += self.speed
        if self.y > self.size:
            self.y = -10
            self.x = random.randint(50, X - 30)



starss = [Stars() for _ in range(15)]


run = True
clock = pygame.time.Clock()
while run:
    screen.fill(W)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for star in starss:
        star.movement()
        star.draw()

    pygame.display.flip()
    clock.tick(60)



pygame.quit()

