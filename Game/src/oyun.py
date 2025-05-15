import pygame
import time
import sys
import random
import math

def random_direction():

def move_animal(animal, area_rect, speed=1):

# === Ayarlar ===
WIDTH, HEIGHT = 800, 700
TILE_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = 7, 6  # Tarla alanı (5x6)
INFO_BAR_HEIGHT = 50  # Üstteki bilgi çubuğunun yüksekliği
INFO_BAR_RECT = pygame.Rect(0, 0, WIDTH, INFO_BAR_HEIGHT)  # Bilgi çubuğu alanı

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

  def update_animation(self):

class Tile:
  def __init__(self):

  def till(self):

  def plant(self, tohum_turu):

  def water(self):

  def harvest(self):

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

def get_tile_coords():

def check_interaction():

def update_cow_animation(cow, animation_frames, frame_delay):

print(COW_SPRITESHEET.get_size())  # Sprite sheet'in boyutlarını yazdır

def satış_arayüzü():

def kümes_arayuzu():

def ahir_arayuzu():

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

def envanter_arayuzu():

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

