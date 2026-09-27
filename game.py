import pygame
import random
import sys

# Pygame инициализациялоо
pygame.init()

# Экрандын өлчөмдөрү (телефон үчүн портреттик формат)
WIDTH, HEIGHT = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anime Arena")

# Түстөр
BLACK = (20, 20, 30)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
GOLD = (255, 215, 0)

clock = pygame.time.Clock()

# Каарман (Герой)
player_x = WIDTH // 2 - 50
player_y = HEIGHT - 200
player_size = 80
player_speed = 10

# Душман
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_size = 80
enemy_speed = 7

score = 0
font = pygame.font.Font(None, 60)

# Оюндун негизги цикли
running = True
while running:
    screen.fill(BLACK)
    
    # Окуяларды текшерүү (Башкаруу)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Телефон экранына тийүү же баскычтар аркылуу башкаруу
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed

    # Экрандан чыгып кетүүдөн сактоо
    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Душмандын кыймылы
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1

    # Кагылышууну текшерүү (Коллизия)
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        score = 0  # Упай күйөт
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)

    # Объекттерди тартуу
    # Каарман (Көк түстө)
    pygame.draw.rect(screen, BLUE, player_rect, border_radius=15)
    
    # Душман (Кызыл түстө)
    pygame.draw.rect(screen, RED, enemy_rect, border_radius=15)

    # Упайды көрсөтүү
    score_text = font.render(f"Score: {score}", True, GOLD)
    screen.blit(score_text, (30, 30))

    pygame.display.flip()
    clock.tick(60)
