from pygame import*
from level import level

W,H = 1280,720
win = display.set_mode((W,H))
display.set_caption("Blockada")


bg = transform.scale(image.load("images/bgr.png"),(W,H))

class Settings(sprite.Sprite):
    def __init__(self, x,y,w,h,speed,img):
        super().__init__()
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img),(self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))
        
class Player(Settings):
    def I_r(self):
        keys = key.get_pressed()
        if keys [K_a]:
            self.rect.x -=self.speed
        if keys[K_d]:
            self.rect.x += self.speed
    def u_d(self):
        keys = key.get_pressed()
        if keys [K_w]:
            self.rect.y -=self.speed
        if keys[K_s]:
            self.rect.y += self.speed
            
class Camera():
    def __init__(self,camera_func, w,h):
        self.camera_func = camera_func
        self.state = Rect(0,0,w,h,)
        
    def apply(self,target):
        return target.rect.move(self.state.topleft)
    
    def update(self,target):
        self.state = self.camera_func(self.state, target.rect)
        

def camera_comfig(camera,target_rect):
    l,t,_,_= target_rect
    _,_,w,h = camera 
    l,t = - l + W/2, -t + H/2
    l = min(0,l)
    l= max (-(camera.width-W),l)
    t= max (-(camera.heigth-H),t)
    t= min(0,t)
    
    return Rect(l,t,w,h)




#TODO IMAGES
blackground = 'images/bgr.png'
img_coin = 'images/coin.png'
img_door = 'images/dorr.png'
img_key = 'images/key.png'
img_chest_open = 'imades/cst_open.png'
img_chesr_close = 'imades/cst_close.png'
img_cyborg = 'imades/cyborg.png'
img_stair = 'images/stair.png'
img_port = 'images/portal.png'
img_platform = 'images/platform.png'
img_nothing = 'images/nothing.png'
ing_power = 'images/mana.png'
img_hero = 'images/sprite1.png'





#TODO FONS

#TODO SOUNDS

player= Player(300,650,50,50,5,img_hero)
#TODO
blocks_r =[]
blocks_l =[]
coins = []
stairs =[] 
platform = []  
items = sprite.Group() 






win.blit(bg,(0,0))

x=y = 0 
for r in level:
    for c in  r:
        if c == r:
            r1 = Settings(x,y,40,40,0, img_nothing)
            r1.reset()
        if c == "l":
            r2 = Settings(x,y,40,40,0, img_nothing)
            r2.reset()
        if c == '/':
            r3 = Settings(x,y-40,40,180,0, img_stair)
            r3.reset()
        if c == '°':
            r4 = Settings(x,y,40,40,0, img_coin)
            r4.reset()
        if c == '-':
            r5 = Settings(x,y,40,40,0, img_platform)
            r5.reset()
        x+= 40
    y+=40
    x = 0
            


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    player.u_d()       
    player.I_r()       
    player.reset()
    time.delay(15)       
    display.update()
    