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

# obrazek
postac = pygame.image.load("assets\postac_początek.png")

# ikonka
icon = pygame.image.load("grad_cap_icon.jpg")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

while True:
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


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()

            elif event.key == pygame.K_RETURN:
                # po wcisnięciu enter, gra się rozpoczyna
                akcja_start()


        pygame.display.flip()
        clock.tick(60)