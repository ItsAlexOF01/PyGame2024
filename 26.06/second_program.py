# coding: utf8
import pygame
import random
count=0
x_user=int (input())
y_user=int (input())
enemy_new=True


# задааем размер окна, создаем окно размера size
size = [400, 400]
window = pygame.display.set_mode(size)
# задаем имя - в кавычках, т.к. текст - это строка
pygame.display.set_caption('My second file')

screen = pygame.Surface(size)

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))


def Intersect(s1_x, s2_x, s1_y, s2_y):
    if ((s1_x>s2_x-40) and (s1_x<s2_x+40) and (s1_y>s2_y-40) and (s1_y<s2_y+40)):
        return 1
    else:
        return 0

# создание персонажей
# герой

# переменные-"переключатели" движения для героя
hero = Sprite(200, 200, 'img1.png')
hero.right = True
hero.up = True
# враг
enemy = Sprite(200, 10, 'img2.png')
# переменные-"переключатели" движения для врага
enemy.right = True
enemy.up = False


bad_screen = False
count = 0
running = True

enemy_new = True

runnig=True
pygame.key.set_repeat(1,1)
while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running  = False
    if e.type==pygame.KEYDOWN:
        if e.key==pygame.K_LEFT:
            hero.x-=1
        if e.key==pygame.K_RIGHT:
            hero.x+=1
        if e.key==pygame.K_UP:
            hero.y-=1
        if e.key==pygame.K_DOWN:
            hero.y+=1
        

    # задайте фоновый цвет
    screen.fill([23, 198, 93])

    # движение персонажей - аналогично тому,
    # что делали с квадратом, но теперь по вертикали
    '''
    if hero.up == True:
        hero.y -= 10
        if hero.y < 0:
            hero.up = False
    else:
        hero.y += 10
        if hero.y > 360:
            hero.up = True
    '''
    if enemy_new==True:
        enemy.x = random.randint(0, 400)
        #enemy.y = random.radint(0, 400)
        enemy.y = 0
        high = random.randint(0, 200)
        count += 1
        enemy_new = False
        enemy.up = False
        
    
    if enemy.up == True:
        enemy.y -= 10
        if enemy.y < 0:
            enemy.up = False
            enemy_new = True
    else:
        enemy.y += 10
        if enemy.y > high:
            enemy.up = True
            


    # столкновение персонажей
    if Intersect(hero.x, enemy.x, hero.y, enemy.y):
        hero.up = False
        enemy.up = True
        print('/n Game Over')
        print('Score', count)
        break

    # отображение персонажей
    hero.render()
    enemy.render()
    

    # отображение окна
    window.blit(screen, [0, 0])
    pygame.display.flip()
    pygame.time.delay(50)


pygame.quit()