import pygame

pygame.init()
ekran = pygame.display.set_mode((900,600))

# użyte kolory
szary_kolor = (61,57,57)
biały_kolor = (255,255,255)
czarny_kolor = (0,0,0)

pygame.display.set_caption("Kognigra")
ekran.fill(biały_kolor)

# wymiary ekranu
szerokosc = ekran.get_width()
wysokosc = ekran.get_height()

# użyte czcionki
czcionka = pygame.font.SysFont("Verdana", 20)
mala_czcionka = pygame.font.SysFont("Verdana", 15)

clock = pygame.time.Clock()

# do wpisywania imienia
wpisz_imie = ""
pole_imie = pygame.Rect(szerokosc*0.40,wysokosc*0.75,140,50)

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
