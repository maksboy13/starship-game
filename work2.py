import pygame
import random
import time

pygame.init()

# Инициализация экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Космопутешественник")

# Определение цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (80, 80 ,80)
DARK_GRAY = (40, 40, 40)
D_GR = (20, 20, 20)


#SCORE
score = 0

# SHIP COORDS

shx = 0

shy = 0

ship = pygame.rect


# creating stars
sc = 50
xs = [0] * sc
ys = [0] * sc

bc = 20
bx = [0] * bc
by = [0] * bc
for i in range(sc):
    xs[i] = random.randint(20, 780)
    ys[i] = random.randint(20, 580)

def create_stars():
    for i in range(sc):
        pygame.draw.circle(screen, WHITE, (xs[i], ys[i]), 2)

def create_barriers():
    for i in range(bc):
        bx[i] = random.randint(50, 750)
        by[i] = random.randint(50, 550)

def gen_bar():
    for i in range(bc):
        pygame.draw.circle(screen, GRAY, (bx[i], by[i]), 10)

# check for hit
def chkhit(ship):
    if ship.x < 0 or ship.x > 750 or ship.y < 0 or ship.y > 550:
        return True
    for i in range(bc):
        ast = pygame.draw.rect(screen, (0, 0, 0), (bx[i] - 10, by[i] - 10, 20, 20))
        pygame.draw.circle(screen, GRAY, (bx[i], by[i]), 10)
        if ship.colliderect(ast):
            return True

# Функция для создания кнопки
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.SysFont(None, 36)
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))


def pos(act):
    print()


# Функция для проверки, был ли клик на кнопке
def button_click(x, y, width, height, mouse_x, mouse_y):
    if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
        return True
    return False

def game_over():
    font = pygame.font.SysFont(None, 100)
    label = font.render("Game over", True, (255, 0, 0))
    screen.blit(label, (300 + (200 - label.get_width()) // 2, 250 + (50 - label.get_height()) // 2))


def draw_ship(x, y, score):

    font = pygame.font.SysFont(None, 36)
    label = font.render(f"score: {score}", True, WHITE)
    screen.blit(label, (300 + (200 - label.get_width()) // 2, 10 + (50 - label.get_height()) // 2))

    pygame.draw.polygon(screen, D_GR, [(x, y - 45), (x - 5, y - 25), (x + 5, y - 25)])
    pygame.draw.polygon(screen, D_GR, [(x - 45, y + 10), (x - 25, y + 5), (x - 25, y + 15)])
    pygame.draw.polygon(screen, D_GR, [(x + 45, y + 10), (x + 25, y + 5), (x + 25, y + 15)])
    ship = pygame.draw.rect(screen, DARK_GRAY, (x - 25, y - 25, 50, 50))
    pygame.draw.circle(screen, (255, 200, 0), (x, y), 15)

    if chkhit(ship) and score > 0:
        game_over()
        return False
    else:
        return True

def scene(rung):
    create_stars()
    if rung == False:
        score = 0
        draw_button(300, 250, 200, 50, BLUE, "Старт игры")
        create_barriers()
    elif rung:
        gen_bar()


# Главный цикл игры
running = True
rung = False
frame = False
go = False
keys = pygame.key.get_pressed()
while running:
    if not frame:
        temp = False
        frame = True
        screen.fill((0, 0, 0))
        scene(rung)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if rung == False:
                        if button_click(300, 250, 200, 50, mouse_x, mouse_y):
                            print("started")
                            rung = True
                            scene(rung)
                            pygame.display.update()
                    elif rung == True:
                        if go == True:
                            go = False
                            rung = False
                        else:
                            if not (shx == mouse_x and shy == mouse_y):
                                shx, shy = mouse_x, mouse_y
                                sco = True
                            if draw_ship(shx, shy, score):
                                if sco == True:
                                    score += 1
                                    sco = False
                            elif not draw_ship(shx, shy, score):
                                go = True
                        pygame.display.update()
                        time.sleep(1/10)
                elif event.type == pygame.KEYDOWN:
                    if go == True:
                        go = False
                        rung = False
                    else:
                        if event.key == pygame.K_w:
                            shy -= 20
                            if draw_ship(shx, shy, score):
                                    score += 1
                            elif not draw_ship(shx, shy, score):
                                go = True
                            pygame.display.update()
                            time.sleep(1 / 10)
                        if event.key == pygame.K_a:
                            shx -= 20
                            if draw_ship(shx, shy, score):
                                score += 1
                            elif not draw_ship(shx, shy, score):
                                go = True
                            pygame.display.update()
                            time.sleep(1 / 10)
                        if event.key == pygame.K_s:
                            shy += 20
                            if draw_ship(shx, shy, score):
                                score += 1
                            elif not draw_ship(shx, shy, score):
                                go = True
                            pygame.display.update()
                            time.sleep(1 / 10)
                        if event.key == pygame.K_d:
                            shx += 20
                            if draw_ship(shx, shy, score):
                                score += 1
                            elif not draw_ship(shx, shy, score):
                                go = True
                            pygame.display.update()
                            time.sleep(1 / 10)

        frame = False


pygame.quit()