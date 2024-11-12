import pygame
import random
import math

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        for i in range(32, 640, 32):
            pygame.draw.line(screen, "black", (i, 0), (i, 512))
        for i in range(32, 512, 32):
            pygame.draw.line(screen, "black", (0, i), (640, i))
        newpos = (0, 0)
        screen.blit(mole_image, mole_image.get_rect(topleft=newpos))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if math.isclose(newpos[0]+16, event.pos[0], abs_tol=16) and math.isclose(newpos[1]+16, event.pos[1], abs_tol=16):
                        newpos = (random.randrange(0, 640, 32), random.randrange(0, 512, 32))
                        screen.fill("light green")
                        for i in range(32, 640, 32):
                            pygame.draw.line(screen, "black", (i, 0), (i, 512))
                        for i in range(32, 512, 32):
                            pygame.draw.line(screen, "black", (0, i), (640, i))
                        screen.blit(mole_image, mole_image.get_rect(topleft=newpos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
