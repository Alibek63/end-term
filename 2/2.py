import pygame
import random
import sys

# Инициализация Pygame
pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stock Market Simulator')
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (width, height))
font_large = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 28)
text_color = (230, 230, 250)
balance = 1000
update_interval = 2000

# Класс для акций
class Stock:
    def __init__(self, name, color, price, position):
        self.name = name
        self.color = color
        self.price = price
        self.position = position
        self.quantity = 0  # количество акций в портфеле

    def buy(self):
        global balance
        if balance >= self.price:
            balance -= self.price
            self.quantity += 1

    def sell(self):
        global balance
        if self.quantity > 0:
            balance += self.price
            self.quantity -= 1

    def update_price(self):
        self.price = max(50, self.price + random.randint(-10, 10))

    def render(self):
        render_text(f'{self.name}: ${self.price}', 50, self.position, self.color, font_large)
        render_text(f'Owned: {self.quantity}', 250, self.position, self.color)

# Функция для отрисовки текста
def render_text(text, x, y, color=text_color, font=font_small):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Создание объектов акций
stocks = {
    'Apple': Stock('Apple', (255, 69, 0), 150, 150),
    'Google': Stock('Google', (65, 105, 225), 100, 250),
    'Amazon': Stock('Amazon', (34, 139, 34), 200, 350)
}

# Основной цикл программы
running = True
last_update = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: stocks['Apple'].buy()
            elif event.key == pygame.K_s: stocks['Google'].buy()
            elif event.key == pygame.K_d: stocks['Amazon'].buy()
            elif event.key == pygame.K_z: stocks['Apple'].sell()
            elif event.key == pygame.K_x: stocks['Google'].sell()
            elif event.key == pygame.K_c: stocks['Amazon'].sell()

    current_time = pygame.time.get_ticks()
    if current_time - last_update > update_interval:
        for stock in stocks.values():
            stock.update_price()
        last_update = current_time

    screen.blit(background_image, (0, 0))

    for stock in stocks.values():
        stock.render()

    render_text(f'Balance: ${balance}', 50, 50, font=font_large)

    # Отрисовка инструкций
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

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
