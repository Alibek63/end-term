
import pygame
import random
import sys

# Инициализация Pygame
pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stock Market Simulator')

# Загрузка фонового изображения
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (width, height))

# Начальные настройки
font_large = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 28)
text_color = (230, 230, 250)
stock_colors = {'Apple': (255, 69, 0), 'Google': (65, 105, 225), 'Amazon': (34, 139, 34)}
stock_prices = {'Apple': 150, 'Google': 100, 'Amazon': 200}
positions = {'Apple': 150, 'Google': 250, 'Amazon': 350}
portfolio = {'Apple': 0, 'Google': 0, 'Amazon': 0}
balance = 1000
update_interval = 2000  # Замедление скорости изменения цен (в миллисекундах)

# Функция для отображения текста
def render_text(text, x, y, color=text_color, font=font_small):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Покупка и продажа акций
def buy_stock(stock_name):
    global balance, portfolio
    if balance >= stock_prices[stock_name]:
        balance -= stock_prices[stock_name]
        portfolio[stock_name] += 1

def sell_stock(stock_name):
    global balance, portfolio
    if portfolio[stock_name] > 0:
        balance += stock_prices[stock_name]
        portfolio[stock_name] -= 1

# Основной цикл программы
running = True
last_update = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: buy_stock('Apple')
            elif event.key == pygame.K_s: buy_stock('Google')
            elif event.key == pygame.K_d: buy_stock('Amazon')
            elif event.key == pygame.K_z: sell_stock('Apple')
            elif event.key == pygame.K_x: sell_stock('Google')
            elif event.key == pygame.K_c: sell_stock('Amazon')

    current_time = pygame.time.get_ticks()
    if current_time - last_update > update_interval:
        # Обновление цен акций
        stock_prices = {name: max(50, price + random.randint(-10, 10)) for name, price in stock_prices.items()}
        last_update = current_time

    # Отображение фонового изображения
    screen.blit(background_image, (0, 0))

    # Отображение цен акций и портфолио
    for index, (name, price) in enumerate(stock_prices.items()):
        render_text(f'{name}: ${price}', 50, positions[name], stock_colors[name], font_large)
        render_text(f'Owned: {portfolio[name]}', 250, positions[name], stock_colors[name])

    # Отображение баланса
    render_text(f'Balance: ${balance}', 50, 50, font=font_large)

    # Инструкции
    instructions = [
        'Press A to buy Apple stock',
        'Press S to buy Google stock',
        'Press D to buy Amazon stock',
        'Press Z to sell Apple stock',
        'Press X to sell Google stock',
        'Press C to sell Amazon stock'
    ]
    for i, instruction in enumerate(instructions):
        render_text(instruction, 550, 100 + i * 30, color=(224, 255, 255))

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
