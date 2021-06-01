import pygame, sys

class Gracz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (400, 400))
        self.max_pkt_zycia = 1000
        self.biezace_pkt_zycia = 1000
        self.dlugosc_paska = 400
        self.wskaznik_zycia = self.max_pkt_zycia / self.dlugosc_paska

    def odejmowanie_pkt_zycia(self, liczba_pkt):
        if self.biezace_pkt_zycia > 0:
            self.biezace_pkt_zycia -= liczba_pkt
        else:
            self.biezace_pkt_zycia = 0

    def dodawanie_pkt_zycia(self, liczba_pkt):
        if self.biezace_pkt_zycia < self.max_pkt_zycia:
            self.biezace_pkt_zycia += liczba_pkt
        else:
            self.biezace_pkt_zycia = self.max_pkt_zycia

    def ksztalt_kolor(self):
        # zmieniający się pasek, kolor: szary (można zmienić), 25 - wysokość
        pygame.draw.rect(okno, (61,57,57), (10,10, self.biezace_pkt_zycia/self.wskaznik_zycia, 25))

        # pasek w tle, kolor: czarny, stała długość, 4 - szerokość ramki
        pygame.draw.rect(okno, (0,0,0), (10,10,self.dlugosc_paska,25),4)

    def update(self):
        self.ksztalt_kolor()

pygame.init()
okno = pygame.display.set_mode((900,600))
gracz = pygame.sprite.GroupSingle(Gracz())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # to trzeba będzie zmienić żeby to zależało od przeszkód
            if event.key == pygame.K_UP:
                # wciśnięcie strzałki w górę - dodawanie życia o 200 pkt
                gracz.sprite.dodawanie_pkt_zycia(200)
            if event.key == pygame.K_DOWN:
                # wciśnięcie strzałki w dół - odejmowanie życia o 200 pkt
                gracz.sprite.odejmowanie_pkt_zycia(200)

    okno.fill((255,255,255))
    gracz.draw(okno)
    gracz.update()
    pygame.display.update()

# wybaczcie niektóre angielskie nazwy, program bez nich czasem wariował


