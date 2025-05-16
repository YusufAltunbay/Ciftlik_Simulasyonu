import pygame
import time
import sys
import random
import math

def random_direction():
    angle = random.uniform(0, 2 * math.pi)
    return math.cos(angle), math.sin(angle)

def move_animal(animal, area_rect, speed=1):
    # Hayvanın yönü yoksa başlat
    if "dir" not in animal:
        animal["dir"] = random_direction()
    dx, dy = animal["dir"]
    # Hareket et
    animal["rect"].x += int(dx * speed)
    animal["rect"].y += int(dy * speed)
    # Sınır kontrolü
    if not area_rect.contains(animal["rect"]):
        # Sınıra çarptıysa tamamen rastgele yeni bir yön ver
        animal["rect"].x -= int(dx * speed)
        animal["rect"].y -= int(dy * speed)
        animal["dir"] = random_direction()
    # Ara sıra yön değiştir 
    if random.random() < 0.03:
        animal["dir"] = random_direction()

# === Ayarlar ===
WIDTH, HEIGHT = 800, 700
TILE_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = 7, 6  
INFO_BAR_HEIGHT = 50  
INFO_BAR_RECT = pygame.Rect(0, 0, WIDTH, INFO_BAR_HEIGHT)  

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gelişmiş Çiftlik Oyunu")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# === Renkler ===
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (160, 82, 45)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WATER = (0, 191, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# === Tohum Türleri ===
TOHUM_TURLERI = {
    "buğday": {"büyüme_suresi": 5, "maliyet": 1, "satis_fiyati": 2},
    "mısır": {"büyüme_suresi": 7, "maliyet": 3, "satis_fiyati": 5},
    "havuç": {"büyüme_suresi": 10, "maliyet": 5, "satis_fiyati": 8},
    "pancar": {"büyüme_suresi": 20, "maliyet": 10, "satis_fiyati": 25},
    "çilek": {"büyüme_suresi": 12, "maliyet": 8, "satis_fiyati": 15},
    "ayçiçek": {"büyüme_suresi": 25, "maliyet": 10, "satis_fiyati": 30},
}

# Görselleri yükleme
WHEAT_SEEDS_IMG = pygame.image.load("Assets/Urunler/Wheat_Seeds.png")
WHEAT_STAGE_5_IMG = pygame.image.load("Assets/Urunler/Wheat_Stage_5.png")
CORN_SEEDS_IMG = pygame.image.load("Assets/Urunler/Corn_Seeds.png")
CORN_STAGE_6_IMG = pygame.image.load("Assets/Urunler/Corn_Stage_6.png")
CARROT_SEEDS_IMG = pygame.image.load("Assets/Urunler/Carrot_Seeds.png")
CARROT_STAGE_4_IMG = pygame.image.load("Assets/Urunler/Carrot_Stage_4.png")
BEET_SEEDS_IMG = pygame.image.load("Assets/Urunler/Beet_Seeds.png")
BEET_STAGE_5_IMG = pygame.image.load("Assets/Urunler/Beet_Stage_5.png")
STRAWBERRY_SEEDS_IMG = pygame.image.load("Assets/Urunler/Strawberry_Seeds.png")
STRAWBERRY_STAGE_6_IMG = pygame.image.load("Assets/Urunler/Strawberry_Stage_6.png")
SUNFLOWER_SEEDS_IMG = pygame.image.load("Assets/Urunler/Sunflower_Seeds.png")
SUNFLOWER_STAGE_6_IMG = pygame.image.load("Assets/Urunler/Sunflower_Stage_5.png")
FLOORING_IMG = pygame.image.load("Assets/Backgrounds/Flooring_50.png")
FLOORING_UNTILLED_IMG = pygame.image.load("Assets/Backgrounds/Flooring_62.png")  # Sürülmemiş tarla
FLOORING_TILLED_IMG = pygame.image.load("Assets/Backgrounds/Flooring_58.png")    # Sürülmüş tarla
BARN_IMG = pygame.image.load("Assets/Builds/144px-Deluxe_Barn.png")
COOP_IMG = pygame.image.load("Assets/Builds/144px-Coop.png")
COW_IMG = pygame.image.load("Assets/Sprites/White_Cow.png")
CHICKEN_IMG = pygame.image.load("Assets/Sprites/White_Chicken.png")
MILK_IMG = pygame.image.load("Assets/Urunler/Milk_TR.png")
EGG_IMG = pygame.image.load("Assets/Urunler/Egg.png")
CARROT_IMG= pygame.image.load("Assets/Urunler/Carrot.png")
STRAWBERRY_IMG= pygame.image.load("Assets/Urunler/Strawberry.png")
SUNFLOWER_IMG= pygame.image.load("Assets/Urunler/Sunflower.png")
WHEAT_IMG= pygame.image.load("Assets/Urunler/Wheat.png")
CORN_IMG= pygame.image.load("Assets/Urunler/Corn.png")
BEET_IMG= pygame.image.load("Assets/Urunler/Beet.png")
BAKKAL_IMG = pygame.image.load("Assets/Builds/bakkal.png")
AHIR_IC_IMG = pygame.image.load("Assets/Backgrounds/ahır_iç_son.png")
YOL_IMG = pygame.image.load("Assets/Backgrounds/yol.png")
AGAC_IMG = pygame.image.load("Assets/Sprites/ağac.png")
IMALATHANE_IMG = pygame.image.load("Assets/Builds/imalathane2.png")
pygame.mixer.init()
EKIN_TOPLAMA_SOUND = pygame.mixer.Sound("Assets/Sounds/ekin_toplama.wav")
CHICKEN_SOUND = pygame.mixer.Sound("Assets/Sounds/Chicken Sound Effect.mp3")
COW_SOUND = pygame.mixer.Sound("Assets/Sounds/İnek Sesi.ogg.opus")
SATINALIM_SOUND = pygame.mixer.Sound("Assets/Sounds/Satın Alım Satım.mp3")
CAR_IMG = pygame.image.load("Assets/Builds/Araba.png")
KORNA_SOUND = pygame.mixer.Sound("Assets/Sounds/Korna.mp3")

ADAM_SAG_SHEET = pygame.image.load("Assets/Sprites/adamsag.png")         # sağa bakan sprite sheet
ADAM_SOL_SHEET = pygame.image.load("Assets/Sprites/adamsol.png")         # sola bakan sprite sheet
ARKADAN_BAK_SHEET = pygame.image.load("Assets/Sprites/arkadanbak.png")   # yukarı bakan sprite sheet
ONDEN_BAKIS_SHEET = pygame.image.load("Assets/Sprites/öndenbakış.png")   # aşağı bakan sprite sheet

# Animasyon karelerini yükleyin
def load_animation_frames(sprite_sheet, frame_width, frame_height):

def load_frames(sheet, frame_width, frame_height):

def load_agac_frames(sheet, frame_width=64, frame_height=64):

class Player:
  def __init__(self, x, y):
    
        self.rect = pygame.Rect(x * TILE_SIZE + 100, y * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE)
        self.inventory = {
            "tohum_buğday": 5,
            "tohum_mısır": 5,
            "tohum_havuç": 5,
            "tohum_pancar": 5,
            "tohum_çilek": 5,
            "tohum_ayçiçek": 5,
            "buğday": 0,  
            "mısır": 0,
            "havuç": 0,
            "pancar": 0,
            "çilek": 0,
            "ayçiçek": 0,
            "süt": 0,  
            "yumurta": 0,  
            "ürün": 0,
            "para": 50
        }
        self.selected_seed = "buğday"  
        self.anim_frame = 0
        self.last_anim_update = 0
        self.direction = "down"  

    def move(self, dx, dy):
        new_rect = self.rect.move(dx * TILE_SIZE, dy * TILE_SIZE)

        if new_rect.left < 0 or new_rect.right > WIDTH or new_rect.top < 0 or new_rect.bottom > HEIGHT:
            return
        if INFO_BAR_RECT.colliderect(new_rect):
            return        
        def upper_part(rect, bottom_margin=30):
            return pygame.Rect(rect.x, rect.y, rect.width, rect.height - bottom_margin)

        if (
            upper_part(AHIR_RECT).colliderect(new_rect) or
            upper_part(KUMES_RECT).colliderect(new_rect) or
            upper_part(IMALATHANE_RECT).colliderect(new_rect) or
            upper_part(SATIS_RECT).colliderect(new_rect)
        ):
            return  

        self.rect = new_rect

        if dx > 0:
            self.direction = "right"
        elif dx < 0:
            self.direction = "left"
        elif dy > 0:
            self.direction = "down"
        elif dy < 0:
            self.direction = "up"

    def update_animation(self):
        now = pygame.time.get_ticks()
        
        if now - self.last_anim_update > 150:
            if self.direction == "right":
                frame_count = len(FRAMES_RIGHT)
            elif self.direction == "left":
                frame_count = len(FRAMES_LEFT)
            elif self.direction == "up":
                frame_count = len(FRAMES_UP)
            else:
                frame_count = len(FRAMES_DOWN)
            self.anim_frame = (self.anim_frame + 1) % frame_count
            self.last_anim_update = now

class Tile:
    def __init__(self):
        self.tilled = False  # Tarla sürülmüş mü?
        new_rect = self.rect.move(dx * TILE_SIZE, dy * TILE_SIZE)

        # Ekran sınırları içinde mi?
        if new_rect.left < 0 or new_rect.right > WIDTH or new_rect.top < 0 or new_rect.bottom > HEIGHT:
            return  # Ekran sınırlarını aşarsa hareket etme

        # Bilgi çubuğu alanına çarpmıyor mu?
        if INFO_BAR_RECT.colliderect(new_rect):
            return  # Bilgi çubuğuna çarptığında hareket etme

        # Binalarla çakışıyor mu?
        if not (new_rect.colliderect(AHIR_RECT) or
                new_rect.colliderect(KUMES_RECT) or
                new_rect.colliderect(IMALATHANE_RECT) or
                new_rect.colliderect(SATIS_RECT)):
            self.rect = new_rect

        if dx > 0:
            self.direction = "right"
        elif dx < 0:
            self.direction = "left"
        elif dy > 0:
            self.direction = "down"
        elif dy < 0:
            self.direction = "up"

    def update_animation(self):
        now = pygame.time.get_ticks()
        frames = GUY_DIRECTIONAL_FRAMES[self.direction]
        if now - self.last_anim_update > 150:
            self.anim_frame = (self.anim_frame + 1) % len(frames)
            self.last_anim_update = now

class Tile:
    def __init__(self):
        self.tilled = False  # Tarla sürülmüş mü?
        self.crop = None  # Ekili ürün
        self.planted_time = None  # Olgunlaşma süresinin başladığı zaman
        self.watered = False  # Sulanmış mı?

    def till(self):
        # Tarlayı sürme işlemi
        self.tilled = True

    def plant(self, tohum_turu):
        if self.tilled and self.crop is None:
            self.crop = tohum_turu
            self.watered = False  # Sulanmadığı için olgunlaşma başlamaz
            self.planted_time = None  # Olgunlaşma süresi başlamaz
            return True  # Ekim başarılı
        return False  # Ekim başarısız

    def water(self):
        if self.crop and not self.watered:
            self.watered = True
            self.planted_time = time.time()  # Sulandıktan sonra olgunlaşma süresi başlar
            return True  # Sulama başarılı
        return False  # Sulama başarısız

    def harvest(self):
        # Hasat işlemi
        if self.crop and self.watered:
            elapsed = time.time() - self.planted_time if self.planted_time else 0
            if elapsed >= TOHUM_TURLERI[self.crop]["büyüme_suresi"]:
                harvested_crop = self.crop  # Hasat edilen ürünü kaydet
                self.crop = None
                self.tilled = False
                self.planted_time = None
                self.watered = False
                return harvested_crop  # Hasat edilen ürünün adını döndür
        return None  # Hasat başarısız
# === Başlat ===
player = Player(0, 0)
farm_grid = [[Tile() for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Alan koordinatları (sadece çizim ve sınır için)
TARLA_RECT = pygame.Rect(100, 100, GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE)
AHIR_RECT = pygame.Rect(450, 100, 150, 120)  # Ahırın boyutları ve konumu genişletildi
KUMES_RECT = pygame.Rect(625, 100, 150, 120)  # Kümesin boyutları ve konumu genişletildi
IMALATHANE_RECT = pygame.Rect(325, 500, 230,120)
SATIS_RECT = pygame.Rect(625, 500, 150, 120)  # Satış alanı genişletildi

# === Etkileşim Alanları ===
AHIR_INTERACTION_AREA = pygame.Rect(AHIR_RECT.x - 20, AHIR_RECT.y - 20, AHIR_RECT.width + 40, AHIR_RECT.height + 40)
KUMES_INTERACTION_AREA = pygame.Rect(KUMES_RECT.x - 20, KUMES_RECT.y - 20, KUMES_RECT.width + 40,
                                     KUMES_RECT.height + 40)
IMALATHANE_INTERACTION_AREA = pygame.Rect(IMALATHANE_RECT.x - 20, IMALATHANE_RECT.y - 20, IMALATHANE_RECT.width + 40,
                                          IMALATHANE_RECT.height + 40)
SATIS_INTERACTION_AREA = pygame.Rect(SATIS_RECT.x - 20, SATIS_RECT.y - 20, SATIS_RECT.width + 40,
                                     SATIS_RECT.height + 40)


# Ahırdaki ineklerin durumları
cows = [
    {"rect": pygame.Rect(200, 150, 60, 60), "type": "cow", "milk": False, "fed_time": None},
    {"rect": pygame.Rect(400, 150, 60, 60), "type": "cow", "milk": False, "fed_time": None},
    {"rect": pygame.Rect(600, 150, 60, 60), "type": "cow", "milk": False, "fed_time": None},
    {"rect": pygame.Rect(200, 350, 60, 60), "type": "cow", "milk": False, "fed_time": None},
    {"rect": pygame.Rect(400, 350, 60, 60), "type": "cow", "milk": False, "fed_time": None},
    {"rect": pygame.Rect(600, 350, 60, 60), "type": "cow", "milk": False, "fed_time": None},
]

# Kümesdeki tavukların durumları
chickens = [
    {"rect": pygame.Rect(200, 150, 60, 60), "type": "chicken", "egg": False, "fed_time": None},
    {"rect": pygame.Rect(400, 150, 60, 60), "type": "chicken", "egg": False, "fed_time": None},
    {"rect": pygame.Rect(600, 150, 60, 60), "type": "chicken", "egg": False, "fed_time": None},
    {"rect": pygame.Rect(200, 350, 60, 60), "type": "chicken", "egg": False, "fed_time": None},
    {"rect": pygame.Rect(400, 350, 60, 60), "type": "chicken", "egg": False, "fed_time": None},
    {"rect": pygame.Rect(600, 350, 60, 60), "type": "chicken", "egg": False, "fed_time": None},
]

# İmalathane üretim durumu (global)
current_production = {
    "product": None,
    "start_time": None
}

def draw_buildings():
    screen.blit(pygame.transform.scale(BARN_IMG, (AHIR_RECT.width, AHIR_RECT.height)), (AHIR_RECT.x, AHIR_RECT.y))
    screen.blit(pygame.transform.scale(COOP_IMG, (KUMES_RECT.width, KUMES_RECT.height)), (KUMES_RECT.x, KUMES_RECT.y))
    screen.blit(pygame.transform.scale(IMALATHANE_IMG, (IMALATHANE_RECT.width, IMALATHANE_RECT.height)), (IMALATHANE_RECT.x, IMALATHANE_RECT.y))
    screen.blit(pygame.transform.scale(BAKKAL_IMG, (SATIS_RECT.width, SATIS_RECT.height)), (SATIS_RECT.x, SATIS_RECT.y))

def draw_farm():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(100 + x * TILE_SIZE, 100 + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            tile = farm_grid[y][x]
            
            if tile.tilled:
                screen.blit(pygame.transform.scale(FLOORING_TILLED_IMG, rect.size), rect.topleft)
            else:
                screen.blit(pygame.transform.scale(FLOORING_UNTILLED_IMG, rect.size), rect.topleft)

            if tile.crop:
                elapsed = time.time() - tile.planted_time if tile.planted_time else 0
                growth_time = TOHUM_TURLERI[tile.crop]["büyüme_suresi"]

                if elapsed < growth_time: 
                    if tile.crop == "buğday":
                        screen.blit(pygame.transform.scale(WHEAT_SEEDS_IMG, rect.size), rect.topleft)
                    elif tile.crop == "mısır":
                        screen.blit(pygame.transform.scale(CORN_SEEDS_IMG, rect.size), rect.topleft)
                    elif tile.crop == "havuç":
                        screen.blit(pygame.transform.scale(CARROT_SEEDS_IMG, rect.size), rect.topleft)
                    elif tile.crop == "pancar":
                        screen.blit(pygame.transform.scale(BEET_SEEDS_IMG, rect.size), rect.topleft)
                    elif tile.crop == "çilek":
                        screen.blit(pygame.transform.scale(STRAWBERRY_SEEDS_IMG, rect.size), rect.topleft)
                    elif tile.crop == "ayçiçek":
                        screen.blit(pygame.transform.scale(SUNFLOWER_SEEDS_IMG, rect.size), rect.topleft)

                    # Büyüme çubuğu
                    progress = min(elapsed / growth_time, 1)  
                    bar_width = TILE_SIZE - 10
                    bar_height = 5
                    bar_x = rect.x + 5
                    bar_y = rect.y + TILE_SIZE - 10
                    pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)  # Çerçeve
                    pygame.draw.rect(screen, GREEN, (bar_x, bar_y, int(bar_width * progress), bar_height))  # Dolan kısım
                else: 
                    if tile.crop == "buğday":
                        screen.blit(pygame.transform.scale(WHEAT_STAGE_5_IMG, rect.size), rect.topleft)
                    elif tile.crop == "mısır":
                        screen.blit(pygame.transform.scale(CORN_STAGE_6_IMG, rect.size), rect.topleft)
                    elif tile.crop == "havuç":
                        screen.blit(pygame.transform.scale(CARROT_STAGE_4_IMG, rect.size), rect.topleft)
                    elif tile.crop == "pancar":
                        screen.blit(pygame.transform.scale(BEET_STAGE_5_IMG, rect.size), rect.topleft)
                    elif tile.crop == "çilek":
                        screen.blit(pygame.transform.scale(STRAWBERRY_STAGE_6_IMG, rect.size), rect.topleft)
                    elif tile.crop == "ayçiçek":
                        screen.blit(pygame.transform.scale(SUNFLOWER_STAGE_6_IMG, rect.size), rect.topleft)

            
            if tile.watered:
                pygame.draw.rect(screen, WATER, rect, 3) 
            else:
                pygame.draw.rect(screen, BROWN, rect, 3)  


def get_tile_coords():

def check_interaction():

def update_cow_animation(cow, animation_frames, frame_delay):

print(COW_SPRITESHEET.get_size())  # Sprite sheet'in boyutlarını yazdır

def satış_arayüzü():

def kümes_arayuzu():
    global chickens
    kümes_rect = pygame.Rect(40, 40, WIDTH - 120, HEIGHT - 40)
    player_rect = pygame.Rect(100, 250, TILE_SIZE, TILE_SIZE)
    direction = "down"
    anim_frame = 0
    last_anim_update = 0

    KUMES_IC_IMG = pygame.image.load("Assets/Backgrounds/kümes_iç.png")

    for i, animal in enumerate(chickens):
        while True:
            animal["rect"].x = random.randint(50, WIDTH - 110)
            animal["rect"].y = random.randint(350, HEIGHT - 110)
            if not any(animal["rect"].colliderect(other["rect"]) for j, other in enumerate(chickens) if i != j):
                break
        animal["dir"] = random_direction()
        animal["anim_frame"] = random.randint(0, TAVUK_ANIM_LEN - 1)
        animal["last_anim_update"] = pygame.time.get_ticks()

    running = True
    while running:
        screen.blit(pygame.transform.scale(KUMES_IC_IMG, (WIDTH, HEIGHT)), (0, 0))

        for animal in chickens:
            if "dx" not in animal or "dy" not in animal:
                animal["dx"] = random.choice([-2, -1, 0, 1, 2])
                animal["dy"] = random.choice([-2, -1, 0, 1, 2])
            if random.randint(0, 100) < 8:
                animal["dx"] = random.choice([-2, -1, 0, 1, 2])
                animal["dy"] = random.choice([-2, -1, 0, 1, 2])

            new_rect = animal["rect"].move(animal["dx"]* 0.5, animal["dy"]* 0.5)

            if not kümes_rect.contains(new_rect):
                animal["dx"] = random.choice([-2, -1, 0, 1, 2])
                animal["dy"] = random.choice([-2, -1, 0, 1, 2])
            else:
                if not any(new_rect.colliderect(other["rect"]) for other in chickens if other != animal):
                    animal["rect"] = new_rect
            now = pygame.time.get_ticks()
            if now - animal["last_anim_update"] > 200:
                animal["anim_frame"] = (animal["anim_frame"] + 1) % TAVUK_ANIM_LEN
                animal["last_anim_update"] = now

            tavuk_img = pygame.transform.scale(TAVUK_FRAMES[animal["anim_frame"]], (30, 30))
            screen.blit(tavuk_img, animal["rect"].topleft)

            if animal["fed_time"] or animal["egg"]:
                elapsed_time = time.time() - animal["fed_time"] if animal["fed_time"] else 30
                progress = min(elapsed_time / 30, 1)
                bar_width = int(60 * progress)
                bar_rect = pygame.Rect(animal["rect"].x, animal["rect"].y - 10, 60, 5)
                pygame.draw.rect(screen, GRAY, bar_rect)
                pygame.draw.rect(screen, GREEN, (bar_rect.x, bar_rect.y, bar_width, bar_rect.height))
                if progress >= 1:
                    animal["egg"] = True
                    animal["fed_time"] = None

        now = pygame.time.get_ticks()
        if now - last_anim_update > 150:
            if direction == "right":
                frame_count = len(FRAMES_RIGHT)
            elif direction == "left":
                frame_count = len(FRAMES_LEFT)
            elif direction == "up":
                frame_count = len(FRAMES_UP)
            else:
                frame_count = len(FRAMES_DOWN)
            anim_frame = (anim_frame + 1) % frame_count
            last_anim_update = now

        if direction == "right":
            char_img = FRAMES_RIGHT[anim_frame]
        elif direction == "left":
            char_img = FRAMES_LEFT[anim_frame]
        elif direction == "up":
            char_img = FRAMES_UP[anim_frame]
        else:
            char_img = FRAMES_DOWN[anim_frame]

        screen.blit(pygame.transform.scale(char_img, (TILE_SIZE, TILE_SIZE)), player_rect.topleft)

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -TILE_SIZE; direction = "left"
        if keys[pygame.K_RIGHT]: dx = TILE_SIZE; direction = "right"
        if keys[pygame.K_UP]: dy = -TILE_SIZE; direction = "up"
        if keys[pygame.K_DOWN]: dy = TILE_SIZE; direction = "down"

        new_rect = player_rect.move(dx * 0.2, dy * 0.2)  
        if kümes_rect.contains(new_rect):
            collision = False
            for animal in chickens:
                if new_rect.colliderect(animal["rect"]):
                    collision = True
                    if keys[pygame.K_SPACE] and animal["egg"]:
                        animal["egg"] = False
                        player.inventory["yumurta"] += 1
                        CHICKEN_SOUND.play()
                        print("Yumurta toplandı!")
                    elif keys[pygame.K_b] and not animal["egg"] and not animal["fed_time"]:
                        if player.inventory.get("mısır", 0) > 0:
                            player.inventory["mısır"] -= 1
                            animal["fed_time"] = time.time()
                            CHICKEN_SOUND.play()
                            print("Tavuk beslendi!")
                        else:
                            print("Yeterli mısır yok!")
            if not collision:
                player_rect = new_rect
def ahir_arayuzu():
    global cows
    ahir_rect = pygame.Rect(40, 40, WIDTH - 120, HEIGHT - 40)
    player_rect = pygame.Rect(100, 180, TILE_SIZE, TILE_SIZE)
    direction = "down"
    anim_frame = 0
    last_anim_update = 0

    for i, animal in enumerate(cows):
        while True:
            animal["rect"].x = random.randint(50, WIDTH - 110)
            animal["rect"].y = random.randint(350, HEIGHT - 110)
            if not any(animal["rect"].colliderect(other["rect"]) for j, other in enumerate(cows) if i != j):
                break
        animal["dir"] = random_direction()

    running = True
    while running:
        screen.blit(pygame.transform.scale(AHIR_IC_IMG, (WIDTH, HEIGHT)), (0, 0))

        for animal in cows:
            if "dx" not in animal or "dy" not in animal:
                animal["dx"] = random.choice([-2, -1, 0, 1, 2])
                animal["dy"] = random.choice([-2, -1, 0, 1, 2])
            if random.randint(0, 100) < 8:
                animal["dx"] = random.choice([-2, -1, 0, 1, 2])
                animal["dy"] = random.choice([-2, -1, 0, 1, 2])

            new_rect = animal["rect"].move(animal["dx"] * 0.5, animal["dy"] * 0.5)
            if not ahir_rect.contains(new_rect):
                animal["dx"] = random.choice([-2, -1, 0, 1, 2])
                animal["dy"] = random.choice([-2, -1, 0, 1, 2])
            else:
                if not any(new_rect.colliderect(other["rect"]) for other in cows if other != animal):
                    animal["rect"] = new_rect

            inek_img = pygame.transform.scale(COW_IMG, (60, 60))
            screen.blit(inek_img, animal["rect"].topleft)

            if animal["fed_time"] or animal["milk"]:
                elapsed_time = time.time() - animal["fed_time"] if animal["fed_time"] else 60
                progress = min(elapsed_time / 60, 1)
                bar_width = int(60 * progress)
                bar_rect = pygame.Rect(animal["rect"].x, animal["rect"].y - 10, 60, 5)
                pygame.draw.rect(screen, GRAY, bar_rect)
                pygame.draw.rect(screen, GREEN, (bar_rect.x, bar_rect.y, bar_width, bar_rect.height))
                if progress >= 1:
                    animal["milk"] = True
                    animal["fed_time"] = None

        now = pygame.time.get_ticks()
        if now - last_anim_update > 150:
            if direction == "right":
                frame_count = len(FRAMES_RIGHT)
            elif direction == "left":
                frame_count = len(FRAMES_LEFT)
            elif direction == "up":
                frame_count = len(FRAMES_UP)
            else:
                frame_count = len(FRAMES_DOWN)
            anim_frame = (anim_frame + 1) % frame_count
            last_anim_update = now

        if direction == "right":
            char_img = FRAMES_RIGHT[anim_frame]
        elif direction == "left":
            char_img = FRAMES_LEFT[anim_frame]
        elif direction == "up":
            char_img = FRAMES_UP[anim_frame]
        else:
            char_img = FRAMES_DOWN[anim_frame]

        screen.blit(pygame.transform.scale(char_img, (TILE_SIZE, TILE_SIZE)), player_rect.topleft)

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -TILE_SIZE; direction = "left"
        if keys[pygame.K_RIGHT]: dx = TILE_SIZE; direction = "right"
        if keys[pygame.K_UP]: dy = -TILE_SIZE; direction = "up"
        if keys[pygame.K_DOWN]: dy = TILE_SIZE; direction = "down"

        new_rect = player_rect.move(dx * 0.2, dy * 0.2) 
        if ahir_rect.contains(new_rect):
            collision = False
            for animal in cows:
                if new_rect.colliderect(animal["rect"]):
                    collision = True
                    if keys[pygame.K_SPACE] and animal["milk"]:
                        animal["milk"] = False
                        player.inventory["süt"] += 1
                        COW_SOUND.play()
                        print("Süt toplandı!")
                    elif keys[pygame.K_b] and not animal["milk"] and not animal["fed_time"]:
                        if player.inventory.get("buğday", 0) > 0:
                            player.inventory["buğday"] -= 1
                            animal["fed_time"] = time.time()
                            COW_SOUND.play()
                            print("İnek beslendi!")
                        else:
                            print("Yeterli buğday yok!")
            if not collision:
                player_rect = new_rect

# İmalathane ürünleri ve gereksinimleri
products = [
    {"name": "Yoğurt", "requirements": {"süt": 2}, "time": 180, "price": 75},
    {"name": "Peynir", "requirements": {"süt": 5}, "time": 300, "price": 150},
    {"name": "Un", "requirements": {"buğday": 5}, "time": 20, "price": 20},
    {"name": "Ayçiçek Yağı", "requirements": {"ayçiçek": 4}, "time": 120, "price": 200},
    {"name": "Şeker", "requirements": {"pancar": 3}, "time": 45, "price": 100},
    {"name": "Pasta", "requirements": {"çilek": 5, "un": 2, "şeker": 2, "yağ": 1, "yumurta": 1, "süt": 2}, "time": 240, "price": 1000},
    {"name": "Kurabiye", "requirements": {"un": 2, "süt": 1, "şeker": 1, "yumurta": 1}, "time": 120, "price": 250},
    {"name": "Dondurma", "requirements": {"süt": 2, "şeker": 1, "çilek": 2}, "time": 60, "price": 200},
    {"name": "Ayran", "requirements": {"yoğurt": 1}, "time": 30, "price": 120},
]

def imalathane_arayuzu():
    global current_production
    running = True
    margin = 20 
    spacing = 10  
    cols = 2  
    row_height = 100  
    col_width = (WIDTH - 2 * margin - (cols - 1) * spacing) // cols 

    product_images = {
        "Yoğurt": pygame.image.load("Assets/Urunler/Mayonnaise.png"),
        "Peynir": pygame.image.load("Assets/Urunler/Cheese.png"),
        "Un": pygame.image.load("Assets/Urunler/flour.jpg"),
        "Ayçiçek Yağı": pygame.image.load("Assets/Urunler/Oil.png"),
        "Şeker": pygame.image.load("Assets/Urunler/Sugar.png"),
        "Pasta": pygame.image.load("Assets/Urunler/Pink_Cake.png"),
        "Kurabiye": pygame.image.load("Assets/Urunler/Cookie.png"),
        "Dondurma": pygame.image.load("Assets/Urunler/Ice_cream.png"),
        "Ayran": pygame.image.load("Assets/Urunler/ayran.webp"),
    }

    requirement_images = {
        "süt": MILK_IMG,
        "yumurta": EGG_IMG,
        "buğday": WHEAT_IMG,
        "mısır": CORN_IMG,
        "havuç": CARROT_IMG,
        "pancar": BEET_IMG,
        "çilek": STRAWBERRY_IMG,
        "ayçiçek": SUNFLOWER_IMG,
        "un": pygame.image.load("Assets/Urunler/flour.jpg"),
        "şeker": pygame.image.load("Assets/Urunler/Sugar.png"),
        "yağ": pygame.image.load("Assets/Urunler/Oil.png"),
        "yoğurt": pygame.image.load("Assets/Urunler/Mayonnaise.png"),
    }

    while running:
        screen.fill(GRAY)

        
        screen.blit(font.render("İMALATHANE", True, WHITE), (WIDTH // 2 - 50, 20))

        for i, product in enumerate(products):
            row = i // cols  
            col = i % cols  

            
            x = margin + col * (col_width + spacing)
            y = margin + 50 + row * (row_height + spacing)

            
            product_rect = pygame.Rect(x, y, col_width, row_height)
            pygame.draw.rect(screen, WHITE, product_rect)
            pygame.draw.rect(screen, BLACK, product_rect, 2)

         
            if product["name"] in product_images:
                product_image = pygame.transform.scale(product_images[product["name"]], (row_height - 20, row_height - 20))
                screen.blit(product_image, (product_rect.x + 10, product_rect.y + 10))

            
            req_x = product_rect.x + row_height + 20
            req_y = product_rect.y + 10
            for item, amount in product["requirements"].items():
                if item in requirement_images:
                    req_image = pygame.transform.scale(requirement_images[item], (30, 30))
                    screen.blit(req_image, (req_x, req_y))
                    amount_text = font.render(str(amount), True, BLACK)
                    screen.blit(amount_text, (req_x + 20, req_y + 20))
                    req_x += 40

           
            time_text = font.render(f"Üretim Süresi: {product['time']} sn", True, BLACK)
            screen.blit(time_text, (product_rect.x + row_height, product_rect.y + 50))

            if (
                current_production["product"] is not None
                and current_production["product"]["name"] == product["name"]
            ):
                elapsed_time = time.time() - current_production["start_time"]
                total_time = product["time"]
                progress = min(elapsed_time / total_time, 1)
                bar_width = col_width - 20
                bar_height = 15
                bar_x = product_rect.x + 10
                bar_y = product_rect.y + row_height - bar_height - 10
                pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
                pygame.draw.rect(screen, GREEN, (bar_x, bar_y, int(bar_width * progress), bar_height))
                percent_text = font.render(f"%{int(progress*100)}", True, BLACK)
                screen.blit(percent_text, (bar_x + bar_width + 8, bar_y))

       
        if current_production["product"]:
            product = current_production["product"]
            elapsed_time = time.time() - current_production["start_time"]
            total_time = product["time"]
            if elapsed_time >= total_time:
             
                product_name = product["name"].lower()
                player.inventory[product_name] = player.inventory.get(product_name, 0) + 1
                print(f"{product['name']} üretildi!")
                current_production["product"] = None
                current_production["start_time"] = None

      
        exit_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 50, 100, 40)
        pygame.draw.rect(screen, RED, exit_button)
        screen.blit(font.render("Çıkış", True, WHITE), (exit_button.x + 20, exit_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                  
                    if exit_button.collidepoint(mouse_x, mouse_y):
                        return
                    
                    for i, product in enumerate(products):
                        row = i // cols
                        col = i % cols
                        x = margin + col * (col_width + spacing)
                        y = margin + 50 + row * (row_height + spacing)
                        product_rect = pygame.Rect(x, y, col_width, row_height)
                        if product_rect.collidepoint(mouse_x, mouse_y):
                            if current_production["product"] is None:
                                if all(player.inventory.get(item, 0) >= amount for item, amount in product["requirements"].items()):
                                    current_production["product"] = product
                                    current_production["start_time"] = time.time()
                                    for item, amount in product["requirements"].items():
                                        player.inventory[item] -= amount
                                    print(f"{product['name']} üretimi başladı!")
                                else:
                                    print(f"{product['name']} için yeterli malzeme yok!")
                            else:
                                print(f"{current_production['product']['name']} üretimi devam ediyor!")


def envanter_arayuzu():
    running = True
    slot_width = 80  
    slot_height = 80  
    slot_margin = 10  
    rows = 4  
    cols = 9  
    inventory_start_x = (WIDTH - (cols * slot_width + (cols - 1) * slot_margin)) // 2
    inventory_start_y = (HEIGHT - (rows * slot_height + (rows - 1) * slot_margin)) // 2

 
    product_images = {
        "tohum_buğday": WHEAT_SEEDS_IMG,
        "tohum_mısır": CORN_SEEDS_IMG,
        "tohum_havuç": CARROT_SEEDS_IMG,
        "tohum_pancar": BEET_SEEDS_IMG,
        "tohum_çilek": STRAWBERRY_SEEDS_IMG,
        "tohum_ayçiçek": SUNFLOWER_SEEDS_IMG,
        "buğday": WHEAT_IMG,
        "mısır": CORN_IMG,
        "havuç": CARROT_IMG,
        "pancar": BEET_IMG,
        "çilek": STRAWBERRY_IMG,
        "ayçiçek": SUNFLOWER_IMG,
        "süt": MILK_IMG,
        "yumurta": EGG_IMG,
        "yoğurt": pygame.image.load("Assets/Urunler/Mayonnaise.png"),
        "peynir": pygame.image.load("Assets/Urunler/Cheese.png"),
        "un": pygame.image.load("Assets/Urunler/flour.jpg"),
        "ayçiçek yağı": pygame.image.load("Assets/Urunler/Oil.png"),
        "şeker": pygame.image.load("Assets/Urunler/Sugar.png"),
        "pasta": pygame.image.load("Assets/Urunler/Pink_Cake.png"),
        "kurabiye": pygame.image.load("Assets/Urunler/Cookie.png"),
        "dondurma": pygame.image.load("Assets/Urunler/Ice_cream.png"),
        "ayran": pygame.image.load("Assets/Urunler/ayran.webp"),
    }

    while running:
        screen.fill(GRAY)

      
        screen.blit(font.render("ENVANTER", True, WHITE), (WIDTH // 2 - 50, 50))

        
        x = inventory_start_x
        y = inventory_start_y
        for i, (item, amount) in enumerate(player.inventory.items()):
            if i >= rows * cols:
                break  

            
            slot_rect = pygame.Rect(x, y, slot_width, slot_height)
            pygame.draw.rect(screen, WHITE, slot_rect)
            pygame.draw.rect(screen, BLACK, slot_rect, 2)

           
            if item in product_images:
                image = pygame.transform.scale(product_images[item], (slot_width - 10, slot_height - 10))
                screen.blit(image, (x + 5, y + 5))

            
            if amount > 0:
                text = font.render(str(amount), True, BLACK)
                screen.blit(text, (x + slot_width - 20, y + slot_height - 20))

           
            x += slot_width + slot_margin
            if (i + 1) % cols == 0:  
                x = inventory_start_x
                y += slot_height + slot_margin

   
        exit_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 80, 100, 40)
        pygame.draw.rect(screen, RED, exit_button)
        screen.blit(font.render("Çıkış", True, WHITE), (exit_button.x + 20, exit_button.y + 10))

        pygame.display.flip()

     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if exit_button.collidepoint(mouse_x, mouse_y):
                    running = False

def ana_menu():

# === Ana Döngü ===
selected_seed = "buğday"  # Varsayılan seçili tohum

ana_menu()



pygame.mixer.music.load("Oyun Müziği.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  # Oyun boyunca döngüde çalsın


running = True
while running:
    # Haritayı doldur
    for y in range(0, HEIGHT, TILE_SIZE):
        for x in range(0, WIDTH, TILE_SIZE):
            if 600 <= y < 700:
                screen.blit(pygame.transform.scale(YOL_IMG, (TILE_SIZE, TILE_SIZE)), (x, y))
            else:
                screen.blit(pygame.transform.scale(FLOORING_IMG, (TILE_SIZE, TILE_SIZE)), (x, y))
    # Bilgi çubuğunu çiz
    pygame.draw.rect(screen, GRAY, INFO_BAR_RECT)

    # Para miktarını sağ köşede göster
    para_text = font.render(f"Para: {player.inventory.get('para', 0)}$", True, WHITE)
    screen.blit(para_text, (WIDTH - para_text.get_width() - 10, 10))

    # Seçili ürünün simgesini orta kısımda göster ve miktarını yaz
    selected_seed = player.selected_seed
    if selected_seed:
        seed_image = {
            "buğday": WHEAT_SEEDS_IMG,
            "mısır": CORN_SEEDS_IMG,
            "havuç": CARROT_SEEDS_IMG,
            "pancar": BEET_SEEDS_IMG,
            "çilek": STRAWBERRY_SEEDS_IMG,
            "ayçiçek": SUNFLOWER_SEEDS_IMG,
        }.get(selected_seed)

        if seed_image:
            scaled_seed_image = pygame.transform.scale(seed_image, (30, 30))  # Görseli küçült
            screen.blit(scaled_seed_image, (WIDTH // 2 - 15, 10))  # Orta kısma yerleştir

            # Seçili ürün miktarını yaz
            seed_count = player.inventory.get(f"tohum_{selected_seed}", 0)
            count_text = font.render(str(seed_count), True, WHITE)
            screen.blit(count_text, (WIDTH // 2 + 10, 10))  # Simgenin sağ üst köşesine yaz

            draw_buildings()
    draw_farm()

    # 3 animasyonlu ağaç çizimi (sol kenardan imalathaneye kadar)
    agac_y = 540
    agac_width = 64
    agac_height = 64
    agac_aralik = (IMALATHANE_RECT.x - 20 - agac_width * 3) // 4
    # Animasyon karesi (her ağaç için farklı faz)
    agac_anim_frame = (pygame.time.get_ticks() // 200) % AGAC_ANIM_LEN

    for i in range(3):
        agac_x = agac_aralik + i * (agac_width + agac_aralik)
        frame_idx = (agac_anim_frame + i) % AGAC_ANIM_LEN  # Her ağaç farklı fazda olsun
        frame = pygame.transform.scale(AGAC_FRAMES[frame_idx], (agac_width, agac_height))
        screen.blit(frame, (agac_x, agac_y))

    # y 100 ve 540 arasına x=20'de 3 eşit aralıklı animasyonlu ağaç
    agac_x_dikey = 25
    agac_y1 = 100
    agac_y2 = 480
    agac_height_dikey = 64
    agac_width_dikey = 64
    agac_count = 3
    agac_aralik_dikey = (agac_y2 - agac_y1 - agac_height_dikey * agac_count) // (agac_count - 1)
    agac_anim_frame_dikey = (pygame.time.get_ticks() // 200) % AGAC_ANIM_LEN

    for i in range(agac_count):
        agac_y = agac_y1 + i * (agac_height_dikey + agac_aralik_dikey)
        frame_idx = (agac_anim_frame_dikey + i) % AGAC_ANIM_LEN
        frame = pygame.transform.scale(AGAC_FRAMES[frame_idx], (agac_width_dikey, agac_height_dikey))
        screen.blit(frame, (agac_x_dikey, agac_y))

    # Karakteri çiz
    if player.direction == "right":
        char_img = FRAMES_RIGHT[player.anim_frame]
    elif player.direction == "left":
        char_img = FRAMES_LEFT[player.anim_frame]
    elif player.direction == "up":
        char_img = FRAMES_UP[player.anim_frame]
    else:  # down
        char_img = FRAMES_DOWN[player.anim_frame]

    screen.blit(pygame.transform.scale(char_img, (TILE_SIZE, TILE_SIZE)), player.rect.topleft)

    # İmalathane üretim kontrolü (arayüz dışında da çalışsın)
    if current_production["product"]:
        product = current_production["product"]
        elapsed_time = time.time() - current_production["start_time"]
        if elapsed_time >= product["time"]:
            product_name = product["name"].lower()
            player.inventory[product_name] = player.inventory.get(product_name, 0) + 1
            print(f"{product['name']} üretildi!")
            current_production["product"] = None
            current_production["start_time"] = None

    pygame.display.flip()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Ahır etkileşimi
            if player.rect.colliderect(AHIR_INTERACTION_AREA) and event.key == pygame.K_RETURN:
                ahir_arayuzu()  # Ahır arayüzüne geçiş

            # Kümes etkileşimi
            if player.rect.colliderect(KUMES_INTERACTION_AREA) and event.key == pygame.K_RETURN:
                kümes_arayuzu()  # Kümes arayüzüne geçiş

            # İmalathane etkileşimi
            if player.rect.colliderect(IMALATHANE_INTERACTION_AREA) and event.key == pygame.K_RETURN:
                imalathane_arayuzu()  # İmalathane arayüzüne geçiş

            # Satış alanı etkileşimi
            if player.rect.colliderect(SATIS_INTERACTION_AREA) and event.key == pygame.K_RETURN:
                satış_arayüzü()  # Satış arayüzüne geçiş

            # Envanter arayüzü
            if event.key == pygame.K_c:  # Tuş değiştirildi
                envanter_arayuzu()

            # Seviye görevleri arayüzü
            if event.key == pygame.K_i:
                seviye_gorevleri_arayuzu()

    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT]: dx = -1
    if keys[pygame.K_RIGHT]: dx = 1
    if keys[pygame.K_UP]: dy = -1
    if keys[pygame.K_DOWN]: dy = 1
    if dx != 0 or dy != 0:
        player.move(dx, dy)
        player.update_animation()
    else:
        player.anim_frame = 0

    # Tohum türünü değiştirmek için tuşlar
    if keys[pygame.K_1]: player.selected_seed = "buğday"
    if keys[pygame.K_2]: player.selected_seed = "mısır"
    if keys[pygame.K_3]: player.selected_seed = "havuç"
    if keys[pygame.K_4]: player.selected_seed = "pancar"
    if keys[pygame.K_5]: player.selected_seed = "çilek"
    if keys[pygame.K_6]: player.selected_seed = "ayçiçek"

    # === Tarla İşlemleri ===
    if keys[pygame.K_t]:  # Tarlayı sür
        gx, gy = get_tile_coords()
        if gx is not None and gy is not None:
            farm_grid[gy][gx].till()
            print(f"Tarlanın ({gx}, {gy}) koordinatındaki alan sürüldü.")

    if keys[pygame.K_e]:  # Tohum ek
        gx, gy = get_tile_coords()
        if gx is not None and gy is not None:
            selected_seed = player.selected_seed
            # Tohum envanterde var mı ve tarla ekime uygun mu?
            if player.inventory[f"tohum_{selected_seed}"] > 0 and farm_grid[gy][gx].plant(selected_seed):
                player.inventory[f"tohum_{selected_seed}"] -= 1  # Tohumu envanterden düş
                EKIN_TOPLAMA_SOUND.play()  # SESİ ÇAL
                print(f"{selected_seed.capitalize()} ekildi!")
            else:
                print("Ekim başarısız! Yeterli tohum yok veya tarla sürülmemiş.")

    if keys[pygame.K_h]:  # Hasat yap
        gx, gy = get_tile_coords()
        if gx is not None and gy is not None:
            harvested_crop = farm_grid[gy][gx].harvest()  # Hasat edilen ürünü al
            if harvested_crop:  # Eğer bir ürün hasat edildiyse
                player.inventory[harvested_crop] += 1  # Ürünü envantere ekle
                EKIN_TOPLAMA_SOUND.play()  # SESİ ÇAL
                print(f"{harvested_crop} hasat edildi!")
            else:
                print("Hasat başarısız! Ürün henüz olgunlaşmamış veya sulanmamış.")

    if keys[pygame.K_s]:  # Sulama yap
        gx, gy = get_tile_coords()
        if gx is not None and gy is not None:
            if farm_grid[gy][gx].water():
                print(f"Tarlanın ({gx}, {gy}) koordinatındaki ürün sulandı ve olgunlaşma süresi başladı.")
            else:
                print("Sulama başarısız! Ekili bir ürün yok veya zaten sulanmış.")
pygame.quit()

