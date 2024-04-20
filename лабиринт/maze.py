from pygame import *
win_width = 700
win_height = 900
window = display.set_mode((win_height, win_width))
display.set_caption('Maze')
background = transform.scale(image.load('686b4289a95d11ee9b33364a640f9019_upscaled.jpg'), (900, 800))

x1=100
y1=300
x2=500
t2=300

hero = transform.scale(image.load('hjify.png'), (100, 100))
cyborg = transform.scale(image.load('jangl.png'), (200, 200))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= -50:
            self.direction = 'right'
        if self.rect.x >= win_width - 80:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2,  color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3, ), (self.rect_x, self.rect_y, self.width, self.height))
    

player = Player('hjify.png', 5, win_height - 400, 5)
monster = Enemy('jangl.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 80, win_height - 250, 0)

w1 = Wall(154, 205, 50, 100, 0, 10, 620)
w2 = Wall(154, 205, 50, 200, 80, 10, 640)
w3 = Wall(154, 205, 50, 200, 80, 400, 20)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!!!!!!!!!!!', True, (225, 215, 0))
lose = font.render('TOU LOSEEE!!!!', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
       if e.type == QUIT:
           game = False

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        

        player.reset()
        monster.reset()
        final.reset()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()


    display.update()
    clock.tick(FPS)
