import pygame
pygame.init() #must initial pygame.
window_width, window_height = 500, 480
win = pygame.display.set_mode((window_width, window_height)) #initializes a window with two parameter indicating the width and height
pygame.display.set_caption("Clement's Pygame tutorial 1")
#we gonna put a character on the screen to move

#Loading the images
walkRight = [pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R1.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R2.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R3.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R4.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R5.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R6.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R7.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R8.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R9.png')]
walkLeft = [pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L1.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L2.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L3.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L4.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L5.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L6.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L7.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L8.png'), pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L9.png')]
bg = pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/bg.jpg')
char = pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/standing.png')

#clock
clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/bullet.mp3')
hitSound = pygame.mixer.Sound('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/hit.mp3')


music = pygame.mixer.music.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/music.mp3')
pygame.mixer.music.play(-1)

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)#(x, y, width, height)
        #Pygame-Tutorials-master\Pygame-Tutorials-master\Game
    def draw(self, win):
        # filling the screen with a background.        
        # drawing the character which is an asset in this case.
        if self.walkCount + 1 >= 27:  # there's 9 sprites. 9 sprites gonna be present on screen for 3 frames.
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
                
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        
    def hit(self):
        if Shoitan.visible == True:
            self.isJump = False
            self.jumpCount = 10
            self.x = 60
            self.y = 410
            self.walkCount = 0
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('-5', True, (255, 0, 0))
            win.blit(text, (250 - (text.get_width()/2), 200))
            pygame.display.update()
            pause = 0
            while pause < 300:
                pygame.time.delay(10)
                pause += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#doing an enemy class.
class enemy(object):
    walkRight = [
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R1E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R2E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R3E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R4E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R5E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R6E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R7E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R8E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R9E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R10E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/R11E.png')
    ]
    walkLeft = [
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L1E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L2E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L3E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L4E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L5E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L6E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L7E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L8E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L9E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L10E.png'),
        pygame.image.load('Pygame-Tutorials-master/Pygame-Tutorials-master/Game/L11E.png')
    ]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.WalkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y+2, 31, 57)
        self.health = 10
        self.visible = True
        
    def draw(self, win):
        if self.visible:
        
            self.move()
            
            if self.WalkCount + 1 >= 33:
                self.WalkCount = 0
            if self.velocity > 0:
                win.blit(self.walkRight[self.WalkCount // 3], (self.x, self.y))
                self.WalkCount +=1
            else:
                win.blit(self.walkLeft[self.WalkCount//3], (self.x, self.y))
                self.WalkCount += 1
            self.hitbox = (self.x + 17, self.y+2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 129, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))

    pass
    
    def move(self):
    
        if self.velocity > 0:#moving right
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.WalkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.WalkCount = 0
        pass
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("Hit")

#drawing function
def redrawGameWindow():
    #filling the screen with a background.
    win.blit(bg, (0,0))
    text = font.render("Score: " + str(score), True, (0,0,0)) #parameters are (str, antialiasBOOL, color, backgroundCOLOR)
    win.blit(text, (340, 10))

    Raka.draw(win)
    Shoitan.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    #to make the character show up on the screen, there must be a refresh on the screen
    pygame.display.update()


Raka = player(300, 410, 64, 64)
Shoitan = enemy(100, 410, 64, 64, 450)
shootloop = 0
score = 0
font = pygame.font.SysFont("comicsons", 30, True) #this function basically a string that pops up. the parameters are (type of font, fontSIZE, BOLDboolean, ITALICboolean)
##MAIN LOOP
#loop to make the program going on and on
run = True
bullets = []
while run:
    clock.tick(27)
    if Shoitan.visible == True:
        if Raka.hitbox[1] < Shoitan.hitbox[1] + Shoitan.hitbox[3] and Raka.hitbox[1] + Raka.hitbox[3]> Shoitan.hitbox[1]:
            if Raka.hitbox[0] + Raka.hitbox[2] > Shoitan.hitbox[0] and Raka.hitbox[0] < Shoitan.hitbox[0] + Shoitan.hitbox[2]:
                Raka.hit()
                score -= 5
    
    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0
    #events are whatever the user does on the screen. clicking something or whatever. or mouse movement too.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:#checking for the bullet to be INSIDE the HITBOX!!
        if Shoitan.visible == True:
            if bullet.y - bullet.radius < Shoitan.hitbox[1] + Shoitan.hitbox[3] and bullet.y + bullet.radius > Shoitan.hitbox[1]:
                if bullet.x + bullet.radius > Shoitan.hitbox[0] and bullet.x - bullet.radius < Shoitan.hitbox[0] + Shoitan.hitbox[2]:
                    Shoitan.hit()
                    hitSound.play()
                    score += 1
                    bullets.remove(bullet)
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.remove(bullet)
    
    keys = pygame.key.get_pressed()#returns bool values of states of keys pressed. (useful when keys are pressed continuously/hold)
    
    if keys[pygame.K_SPACE] and shootloop == 0:
        bulletSound.play()
        if Raka.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 5:
            bullets.append(projectile(round(Raka.x + Raka.width //2), round(Raka.y + Raka.height//2), 6,(255,0,0), facing))
        shootloop = 1
    
    #move right add, mov left subtract, mov up subtract, mov down add.
    if keys[pygame.K_a] and Raka.x > Raka.velocity:#moving left
        Raka.x -= Raka.velocity
        Raka.left, Raka.right = True, False
        Raka.standing = False
    elif keys[pygame.K_d] and Raka.x < (window_width - Raka.width - Raka.velocity):#moving right
        Raka.x += Raka.velocity
        Raka.left, Raka.right = False, True
        Raka.standing = False
    else:
        Raka.standing = True
        Raka.walkCount = 0
    if not Raka.isJump:
        if keys[pygame.K_w]:
            Raka.isJump = True
            Raka.walkCount = 0
    else:
        if Raka.jumpCount >= -10:
            neg = 1
            if Raka.jumpCount < 0:
                neg = -1
            Raka.y -= (Raka.jumpCount ** 2) * 0.5 * neg
            Raka.jumpCount -= 1
        else:
            Raka.isJump = False
            Raka.jumpCount = 10
    
    
    redrawGameWindow()
    



pygame.quit() 