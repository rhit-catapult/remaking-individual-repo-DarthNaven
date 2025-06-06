import pygame
import sys
import time
import Hero_module
import Cloud_module
def main():

    pygame.init()
    pygame.display.set_caption("New eeps")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    mike = Hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = Hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = Cloud_module.Cloud(screen, 300, 50, "heavy.jpg")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10
        screen.fill(pygame.Color("White"))
        cloud.draw()
        cloud.rain()
        cloud.rain()
        cloud.rain()
        cloud.rain()
        cloud.rain()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)
        mike.draw()
        alyssa.draw()
        pygame.display.update()
main()