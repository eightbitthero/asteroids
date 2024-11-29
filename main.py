# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *   
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)    
        screen.fill("black")

        for i in asteroids:
            if player.collide(i):
                print ("Game over!")
                return
            for bullet in shots:
                if i.collide(bullet):
                    i.split()
                    bullet.kill()

        for i in drawable:
            i.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60)/1000
        

        

if __name__ == "__main__":
    main()
