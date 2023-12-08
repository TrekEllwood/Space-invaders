import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, display_width, speed):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = position)
        self.speed = speed
        self.display_width = display_width
        self.shot_ready = True
        self.shoot_time = 0
        self.shoot_cooldown = 600

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < self.display_width:
            self.rect.x += self.speed

        if keys[pygame.K_SPACE] and self.shot_ready:
            self.shoot()
            self.shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.shot_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.shot_ready = True
        
    def shoot(self):
        pass

    def update(self):
        self.get_input()
        self.recharge()