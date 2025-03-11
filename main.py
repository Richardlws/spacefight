import pygame

WIDTH,HEIGHT = 900,600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE Fight Game!")

def main():
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
    pygame.quit()

if __name__ == "__main__":
    main()