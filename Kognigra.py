import pygame
import pygame as pg
import sys, random

pg.init()

szerokosc = 900
wysokosc = 600
ekran = pg.display.set_mode((900,600))

# użyte kolory
szary_kolor = (61,57,57)
biały_kolor = (255,255,255)
czarny_kolor = (0,0,0)

# ikonka
ikonka = pg.image.load("assets\grad_cap_icon.jpg")
pg.display.set_icon(ikonka)

pg.display.set_caption("Kognigra")
ekran.fill(biały_kolor)

# użyte czcionki
czcionka = pg.font.SysFont("Verdana", 20)
mala_czcionka = pg.font.SysFont("Verdana", 15)

clock = pg.time.Clock()

# do wpisywania imienia
wpisz_imie = ""
pole_imie = pg.Rect(szerokosc*0.40,wysokosc*0.75,140,50)

postac = pg.image.load("assets\postac_początek.png")
bieganie = [pg.image.load("assets\postac_początek.png"), pg.image.load("assets\postac_bieg1.png"), pg.image.load("assets\postac_bieg2.png")]
unikanie = [pg.image.load("assets\postac_schylenie1.png"), pg.image.load("assets\postac_schylenie2.png")]
skakanie = pg.image.load("assets\postac_skok.png")

przeszkoda_meto = [pg.image.load("assets\przeszkoda_mail.png")]

przeszkoda_atom = [pg.image.load("assets\przeszkoda_atom.png")]

tlo = pg.image.load("assets\podłoga.png")

pg.mixer.music.load('backround.mp3')

dzwiek_skoku = pg.mixer.Sound("jumpsound.wav")

uderzenie = pg.mixer.Sound("ouch.mp3")

przedmioty = ["Kolokwium", "Dzień rektorski", "Brak internetu"]


class Student():
    pos_x = 70
    pos_y = 320
    pos_y_unik = 405
    skok_v = 8

    def __init__(self):
        self.bieg_img = bieganie
        self.unik_img = unikanie
        self.skok_img = skakanie

        self.student_bieg = True
        self.student_unik = False
        self.student_skok = False

        self.kroki = 0
        self.skok_predkosc = self.skok_v
        self.image = self.bieg_img[0]
        self.student_rect = self.image.get_rect()
        self.student_rect.x = self.pos_x
        self.student_rect.y = self.pos_y

    def update(self, userInput):
        if self.student_bieg:
            self.bieg()
        if self.student_unik:
            self.unik()
        if self.student_skok:
            self.skok()

        if userInput[pg.K_DOWN] and not self.student_skok:
            self.student_unik = True
            self.student_bieg = False
            self.student_skok = False
        elif not (userInput[pg.K_DOWN] or userInput[pg.K_UP]):
            self.student_bieg = True
            self.student_unik = False
            self.student_skok = False
        elif userInput[pg.K_UP] and not self.student_skok:
            self.student_skok = True
            self.student_bieg = False
            self.student_unik = False

        if self.kroki >= 10:
            self.kroki = 0

    def bieg(self):
        self.student_bieg = True
        self.student_unik = False
        self.student_skok = False
        self.image = self.bieg_img[self.kroki // 5]
        self.student_rect = self.image.get_rect()
        self.student_rect.x = self.pos_x
        self.student_rect.y = self.pos_y
        self.kroki += 1

    def unik(self):
        self.student_bieg = False
        self.student_unik = True
        self.student_skok = False
        self.image = self.unik_img[self.kroki // 5]
        self.student_rect = self.image.get_rect()
        self.student_rect.x = self.pos_x
        self.student_rect.y = self.pos_y_unik
        self.kroki += 1

    def skok(self):
        self.image = self.skok_img
        if self.student_skok:
            pg.mixer.Sound.play(dzwiek_skoku)
            self.student_rect.y -= self.skok_v * 2
            self.skok_predkosc -= 0.8
        if self.skok_predkosc < - self.skok_v:
            self.student_skok = False
            self.skok_predkosc = self.skok_v


    def draw(self, ekran):
        ekran.blit(self.image, (self.student_rect.x, self.student_rect.y))



class Przeszkoda():
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = szerokosc

    def update(self):
        self.rect.x -= szybkosc_gry
        if self.rect.x < -self.rect.width:
            przeszkody.pop()

    def draw(self, ekran):
        ekran.blit(self.image[self.type], self.rect)


class Programowanie(Przeszkoda):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 390


class Metodologia(Przeszkoda):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 290
        self.indeks = 0

    def draw(self, ekran):
        if self.indeks >= 9:
            self.indeks = 0
        ekran.blit(self.image[self.indeks//10], self.rect)
        self.indeks += 1

class pasekHP(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40,40))
        self.image.fill((122, 125, 128))
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
        pg.draw.rect(ekran, (61,57,57), (10,10, self.biezace_pkt_zycia/self.wskaznik_zycia, 25))

        # pasek w tle, kolor: czarny, stała długość, 4 - szerokość ramki
        pg.draw.rect(ekran, (0,0,0), (10,10,self.dlugosc_paska,25),4)

    def update(self):
        self.ksztalt_kolor()

hp = pg.sprite.GroupSingle(pasekHP())

class Inwentarz():
    def __init__(self):
        self.inwentarz = []
        self.kolos = self.przedmioty[0]
        self.wolne = self.przedmioty[1]
        # self.internet = self.przedmioty[2]

    def Kolokwium(self):
        self.inwentarz.append(self.kolos)
        


    def



#     def stworzprzedmiot(self):
#         przedmiot = range(0, 9)
#         if przedmiot [8] != "pelny":
#             przedmiot[1] = ("Książka")
#             przedmiot[2] = ("Kolokwium")
#             przedmiot[3] = ("Oceny")
#             przedmiot[4] = ("Punkty")
#             przedmiot[5] = ("Dzień rektorski")
#             return przedmiot
#         else:
#             return przedmiot
#
#     def stworzInwentarz(self):
#         inw = range(0, 9)
#         inw[10] = ("zrobione")
#         if inw[10] != ("zrobione"):
#             for i in range (0, 9):
#                 inw[i] = 0
#         return inw
#
#     def magazynInwentarza(self, przedmiot):
#         inw = stworzInwentarz()
#         for i in range (0, 9):
#             if inw[i] == 0:
#                 inw[i] = przedmiot
#                 break
#                 return inw
#
#     def sprawdzenieInwentarza(self, przedmiot):
#         przedmiot2 = przedmiot
#         inw = stworzInwentarz()
#         for i in range(0, 9):
#             if przedmiot2 == inw[i]:
#                 return "yes"




def akcja_start():
    global szybkosc_gry, pos_x_tlo, pos_y_tlo, punkty, przeszkody
    run = True
    zegar = pg.time.Clock()
    czas_gry = pg.time.get_ticks()
    gracz = Student()
    # inwent = Inwentarz()
    przeszkody = []
    punkty = 0
    pg.mixer.music.play()


    szybkosc_gry = 20

    pos_x_tlo = 0
    pos_y_tlo = 0

    smierc = 0


    def wynik():
        global punkty, szybkosc_gry
        punkty += 1
        if punkty % 100 == 0:
            szybkosc_gry += 1

        napis = czcionka.render("Wynik:" + str(punkty), True, (0, 0, 0))
        napisRect = napis.get_rect()
        napisRect.center = (800, 30)
        ekran.blit(napis, napisRect)

    while run:

        czas = (pygame.time.get_ticks()-czas_gry) / 1000
        if czas > 60:
            koniec(smierc)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # to trzeba będzie zmienić żeby to zależało od przeszkód
                if event.key == pygame.K_RIGHT:
                    # wciśnięcie strzałki w górę - dodawanie życia o 200 pkt
                    hp.sprite.dodawanie_pkt_zycia(20)

        ekran.fill((122, 125, 128))
        ekran.blit(tlo, (pos_x_tlo, pos_y_tlo))
        ekran.blit(tlo, (szerokosc+pos_x_tlo, pos_y_tlo))
        if pos_x_tlo <= -szerokosc:
            ekran.blit(tlo, (szerokosc+pos_x_tlo, pos_y_tlo))
            pos_x_tlo = 0
        pos_x_tlo -= szybkosc_gry
        # inwent.draw(ekran)

        klikanie = pg.key.get_pressed()

        gracz.draw(ekran)
        gracz.update(klikanie)

        if len(przeszkody) == 0:
            if random.randint(0, 1) == 0:
                przeszkody.append(Programowanie(przeszkoda_atom))
            elif random.randint(0, 1) == 1:
                przeszkody.append(Metodologia(przeszkoda_meto))

        for przeszkoda in przeszkody:
            przeszkoda.draw(ekran)
            przeszkoda.update()
            if gracz.student_rect.colliderect(przeszkoda.rect):
                pg.mixer.Sound.play(uderzenie)
                smierc += 1
                hp.sprite.odejmowanie_pkt_zycia(20)
                if hp.sprite.biezace_pkt_zycia == 0:
                    koniec(smierc = 7)


        wynik()
        hp.draw(ekran)
        hp.update()

        zegar.tick(30)
        pg.display.update()

def koniec(smierc):
    global punkty
    run = True
    pg.mixer.music.stop()

    while run:
        if smierc >= 7:
            naglowek = czcionka.render("Nie tym razem :((", False, czarny_kolor)
            ekran.blit(naglowek, (0.38 * szerokosc, 0.10 * wysokosc))

            ekran.blit(postac, (375, 120))

            tekst_koniec1 = "Niestety czeka Cię poprawka :("
            koniec1 = mala_czcionka.render(tekst_koniec1, False, czarny_kolor)
            ekran.blit(koniec1, (0.35 * szerokosc, 0.53 * wysokosc))

            tekst_koniec2 = "Jeśli chcesz zagrać jeszcze raz i powtórzyć rok, wciśnij ENTER"
            koniec2 = mala_czcionka.render(tekst_koniec2, False, czarny_kolor)
            ekran.blit(koniec2, (0.25 * szerokosc, 0.65 * wysokosc))

            tekst_koniec3 = "Jeśli chcesz zakończyć studiowanie na dziś, wciśnij SPACJĘ"
            koniec3 = mala_czcionka.render(tekst_koniec3, False, czarny_kolor)
            ekran.blit(koniec3, (0.25 * szerokosc, 0.70 * wysokosc))

            pg.display.flip()



        elif smierc < 7:
            naglowek = czcionka.render("Udało się! :D", False, czarny_kolor)
            ekran.blit(naglowek, (0.41 * szerokosc, 0.10 * wysokosc))

            ekran.blit(postac, (375, 120))

            tekst_koniec1 = "Gratulacje!"
            koniec1 = mala_czcionka.render(tekst_koniec1, False, czarny_kolor)
            ekran.blit(koniec1, (0.43 * szerokosc, 0.53 * wysokosc))

            tekst_koniec2 = "Udało Ci się zdać sesję i zaliczyć wszystkie przedmioty!"
            koniec2 = mala_czcionka.render(tekst_koniec2, False, czarny_kolor)
            ekran.blit(koniec2, (0.25 * szerokosc, 0.60 * wysokosc))

            tekst_koniec3 = "Teraz w końcu czas na wakacje :)"
            koniec3 = mala_czcionka.render(tekst_koniec3, False, czarny_kolor)
            ekran.blit(koniec3, (0.35 * szerokosc, 0.65 * wysokosc))

            tekst_koniec4 = "Do zobaczenia w przyszłym roku!"
            koniec4 = mala_czcionka.render(tekst_koniec4, False, czarny_kolor)
            ekran.blit(koniec4, (0.35 * szerokosc, 0.70 * wysokosc))

            tekst_koniec2 = "Jeśli chcesz zagrać jeszcze raz, wciśnij ENTER"
            koniec2 = mala_czcionka.render(tekst_koniec2, False, czarny_kolor)
            ekran.blit(koniec2, (0.25 * szerokosc, 0.80 * wysokosc))

            tekst_koniec5 = "Jeśli chcesz zakończyć studiowanie na dziś, wciśnij SPACJĘ"
            koniec5 = mala_czcionka.render(tekst_koniec5, False, czarny_kolor)
            ekran.blit(koniec5, (0.25 * szerokosc, 0.85 * wysokosc))

            pg.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()

                elif event.key == pygame.K_RETURN:
                    # po wcisnięciu enter, gra się rozpoczyna
                    akcja_start()

            clock.tick(30)


while True:
    # każda linijka musiała być osobno, bo funkcja w pygame nie rozumie \n
    naglowek = czcionka.render("Drogi Kognistudencie!", False, czarny_kolor)
    ekran.blit(naglowek, (0.35*szerokosc, 0))

    tekst_wstep1 = "Zaczynamy kolejny semestr kognitywistyki."
    wstep1 = mala_czcionka.render(tekst_wstep1, False, czarny_kolor)
    ekran.blit(wstep1, (0.15*szerokosc, 0.10*wysokosc))

    tekst_wstep2 = "Twoim zadaniem będzie zaliczenie wszystkich przedmiotów i zdanie sesji jak najlepiej."
    wstep2 = mala_czcionka.render(tekst_wstep2, False, czarny_kolor)
    ekran.blit(wstep2, (0.15 * szerokosc, 0.15 * wysokosc))

    tekst_wstep3 = "Jednak uważaj! Na drodze czyhają jednak liczne przeszkody!"
    wstep3 = mala_czcionka.render(tekst_wstep3, False, czarny_kolor)
    ekran.blit(wstep3, (0.15 * szerokosc, 0.20 * wysokosc))

    tekst_wstep5 = "Nie pozwól, aby projekty z programowania i zadania z metodologii Cię pokonały!"
    wstep5 = mala_czcionka.render(tekst_wstep5, False, czarny_kolor)
    ekran.blit(wstep5, (0.15 * szerokosc, 0.25 * wysokosc))

    tekst_wstep4 = "Aby stoczyć z nimi walkę, poruszaj się strzałkami góra/dół."
    wstep4 = mala_czcionka.render(tekst_wstep4, False, czarny_kolor)
    ekran.blit(wstep4, (0.15 * szerokosc, 0.30 * wysokosc))

    tekst_narzedzia1 = "Masz do dyspozycji kilka narzędzi, które możesz wykorzystać w trakcie gry:"
    narzedzia1 = mala_czcionka.render(tekst_narzedzia1, False, czarny_kolor)
    ekran.blit(narzedzia1, (0.15 * szerokosc, 0.35 * wysokosc))

    tekst_narzedzia2 = "- kolokwium na 5 - pozwala na jedno przejście sesji bez żadnych strat"
    narzedzia2 = mala_czcionka.render(tekst_narzedzia2, False, czarny_kolor)
    ekran.blit(narzedzia2, (0.15 * szerokosc, 0.40 * wysokosc))

    tekst_narzedzia3 = "- dzień rektorski - doładuje Twój pasek życia do 100%!"
    narzedzia3 = mala_czcionka.render(tekst_narzedzia3, False, czarny_kolor)
    ekran.blit(narzedzia3, (0.15 * szerokosc, 0.45 * wysokosc))

    tekst_narzedzia4 = "- brak internetu - na chwilę znikają wszystkie przeszkody"
    narzedzia4 = mala_czcionka.render(tekst_narzedzia4, False, czarny_kolor)
    ekran.blit(narzedzia4, (0.15 * szerokosc, 0.50 * wysokosc))

    polecenie1 = czcionka.render("Aby zalogować się do MS Teams i rozpocząć grę,", False, czarny_kolor)
    ekran.blit(polecenie1, (0.25 * szerokosc, 0.60*wysokosc))
    polecenie2 = czcionka.render("wpisz swoje imię, a następnie wciśnij Enter:", False, czarny_kolor)
    ekran.blit(polecenie2, (0.25 * szerokosc, 0.65*wysokosc))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                wpisz_imie = wpisz_imie[:-1]
            elif event.key == pygame.K_RETURN:
                # po wcisnięciu enter, gra się rozpoczyna
                akcja_start()
            else:
                wpisz_imie += event.unicode

        # tworzenie pola do wpisania imienia
        pygame.draw.rect(ekran, szary_kolor, pole_imie)
        imie_czcionka = mala_czcionka.render(wpisz_imie, True, biały_kolor)
        ekran.blit(imie_czcionka, (pole_imie.x + 15, pole_imie.y + 10))
        pygame.display.flip()
        clock.tick(60)
