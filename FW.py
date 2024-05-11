from pygame import *

class Game(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(80,80))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Game_blocks1(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(700,30))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Game_blocks2(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(30,500))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Game_blocks3(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(300,30))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

    
class Move1(Game):
    def move1(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        

class Move2(Game):
    def move2(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed



window = display.set_mode((700,500))
display.set_caption("Вогонь і Вода")

bg = transform.scale(image.load("bg.png"),(700,500))
player1 = Move1("fireboy.png",50,400,4)
player2 = Move2("watergirl.png",50,305,4)
wall1= Game_blocks1("walls.jpg",0,472,5)
wall2= Game_blocks1("walls.jpg",0,0,5)
wall3= Game_blocks2("walls.jpg",0,0,5)
wall4= Game_blocks2("walls.jpg",670,0,5)
wall5= Game_blocks3("walls.jpg",0,375,5)

FPS = 60
clock = time.Clock()

game = True


#mixer.init()
#mixer.music.load("hghgh.mp3")
#mixer.music.play()
finish = False
a = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg,(0,0))
        player1.move1()
        player1.reset()
        player2.move2()
        player2.reset()
        wall1.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        wall5.reset()

    display.update()
    clock.tick(FPS)