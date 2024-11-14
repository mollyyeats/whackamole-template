import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x = 3
        mole_y = 3
        running = True
        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
        def draw_grid():
            for i in range(1, 17):
                pygame.draw.line(screen, (0, 0, 0), (0, i * 32), (640, i * 32))
            for i in range(1, 21):
                pygame.draw.line(screen, (0, 0, 0), (i * 32, 0), (i * 32, 512))


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mouse_x//32 == mole_x // 32 and mouse_y//32 == mole_y // 32:
                        mole_x = random.randrange(0, 20) *32 +3
                        mole_y = random.randrange(0, 16) *32 +3
            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
