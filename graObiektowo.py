import pygame, sys, os, cmath, random, time
from pygame.locals import *
#from proba import *

#STALE
liczbaTur =9
#tura = 1
menuKolorow =[]
liczbaKolorow = 4
listaKolorow = []
listaKolorowPoNajechaniu =[]
listaKulek = []
listaKombinacji =[]
listaPozycjiKulek =[]



class Kulka():
    def __init__(self, pozX, pozY, kolor1, kolor2, promien, ):
        self.pozX = pozX
        self.pozY = pozY
        self.kolor = kolor1
        self.kolor1 = kolor1
        self.kolor2 = kolor2
        self.promien = promien
        self.klikniete = False
        listaKulek.append(self)

    def wypisz(self):
        # print(self.pozX,self.pozY,self.kolor,self.promien)
        pygame.draw.circle(window, self.kolor, (self.pozX, self.pozY), self.promien)
        pygame.display.update()

    def klikniecie(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if cmath.sqrt(((self.pozX - mouseX) ** 2) + ((self.pozY - mouseY) ** 2)).real <= self.promien:
            #print("klik2")
            kulkaSzyfru = Kulka(listaPozycjiKulek[len(listaKombinacji)][0],listaPozycjiKulek[len(listaKombinacji)][1], self.kolor1, self.kolor1, 20)
            kulkaSzyfru.wypisz()
            listaKombinacji.append(kulkaSzyfru)
            self.klikniete=True


    def najechanie(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if cmath.sqrt(((self.pozX - mouseX) ** 2) + ((self.pozY - mouseY) ** 2)).real <= self.promien:
            #print("najechanie")
            self.kolor = self.kolor2
            self.wypisz()
        else:
            self.kolor = self.kolor1
            self.wypisz()


class Kolor():
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


    def wartosc(self):
        return self.red, self.green, self.blue


class Szyfr():
    def __init__(self):
        self.szyfr = []
        self.czyWygrane =False

    def losuj(self):
        for i in range(liczbaKolorow):
            self.szyfr.append(random.choice(listaKolorow))
        #print(self.szyfr)
    def sprawdz(self,kombinacja,tura,czyZrwacac=False):
        kolory = self.sprawdzKolory(kombinacja)
        pozycje = self.sprawdzPozycje(kombinacja)
        self.wyswietlPodpowiedzi(kolory, pozycje,tura)
        self.wygrana(pozycje)
        if(czyZrwacac):
            return kolory,pozycje

    def spr(self,kombinacja):
        liczbaTrafionychKolorow = 0
        liczbaTrafionychPozycji = 0
        pomSzyfr = list(self.szyfr)
        indeks = 0
        for i in kombinacja:
            if i in pomSzyfr:
                pomSzyfr.remove(i)
                # print(pomSzyfr)
                # print(szyfr)
                liczbaTrafionychKolorow = liczbaTrafionychKolorow + 1
            if kombinacja[indeks] == self.szyfr[indeks]:
                liczbaTrafionychPozycji = liczbaTrafionychPozycji + 1
            indeks = indeks + 1
        print("Trafiles kolorow: ", liczbaTrafionychKolorow)
        print("Trafiłeś pozycji: ", liczbaTrafionychPozycji)
        kombinacja.clear()
    def sprawdzKolory(self,kombinacja):
        kombinacja1 = list(self.szyfr)
        liczbaTrafionychKolorow =0
        for i in kombinacja:
            if i in kombinacja1:
                kombinacja1.remove(i)
                liczbaTrafionychKolorow = liczbaTrafionychKolorow+1
        print(liczbaTrafionychKolorow)
        return liczbaTrafionychKolorow
    def sprawdzPozycje(self,kombinacja):
        liczbaTrafionychPozycji =0
        indeks=0
        #print("szyfr === ",self.szyfr)
        #print("kom === ",kombinacja)
        for i in kombinacja:
            if i == self.szyfr[indeks]:
                liczbaTrafionychPozycji = liczbaTrafionychPozycji+1
            #print("index == ", indeks)
            indeks +=1
        print(liczbaTrafionychPozycji)
        return(liczbaTrafionychPozycji)

    def wyswietlPodpowiedzi(self,liczbaTrafionychKolorow,liczbaTrafionychPozycji ,tura):
        liczbaTrafionychKolorow = liczbaTrafionychKolorow - liczbaTrafionychPozycji
        print(listaPozycjiKulek[(tura-1)*4])
        x=listaPozycjiKulek[(tura-1)*4][0]-80
        y=listaPozycjiKulek[(tura-1)*4][1]-10

        for i in range(4):
            if liczbaTrafionychKolorow >0:
                kulkaPom = Kulka(x,y,blue.wartosc(),blue.wartosc(),10)
                liczbaTrafionychKolorow-=1
            elif liczbaTrafionychPozycji >0:
                kulkaPom = Kulka(x, y, red.wartosc(), red.wartosc(), 10)
                liczbaTrafionychPozycji-=1
            else:
                kulkaPom = Kulka(x, y, white.wartosc(), white.wartosc(), 10)
            kulkaPom.wypisz()
            x+=25
            if(i==1):
                x=listaPozycjiKulek[(tura-1)*4][0]-80
                y=y+25

    def wygrana(self,liczbaTrafoinychPozycji):
        if liczbaTrafoinychPozycji == liczbaKolorow :
            print("WYGRALES")
            self.pokazSzyfr()
            self.czyWygrane = True
    def pokazSzyfr(self):
        y=520
        pygame.draw.line(window, red.wartosc(), (70, y), (280, y), 4)
        pygame.draw.line(window, red.wartosc(), (70, y), (70, y + 62), 4)
        pygame.draw.line(window, red.wartosc(), (280, y), (280, y + 62), 4)
        y += 60
        pygame.draw.line(window, red.wartosc(), (70, y), (280, y), 4)
        x=100
        for i in self.szyfr:
            szyfrKulka = Kulka(x,550,i,i,20)
            szyfrKulka.wypisz()
            x+=50
    def podajSzyfr(self):
        licznik =0
        while(licznik <=liczbaKolorow):
            for i in listaKulek:
                i.klikniecie()
                if i.klikniete:
                    i.klikniete=False
                    licznik+=1
        self.szyfr = list(listaKombinacji)
        self.pokazSzyfr()


class AI():
    def __init__(self):
        self.kombinacja =[]
        self.pozostaleKolory = list(listaKolorow)
        self.dostepneKombinacje = []
        self.aktualneKombinacje =[]
        self.uzyteKombinacje =[]
        self.kolory=0
        self.pozycje=0
    def podajKombinacje(self):

        czyJest=True
        while(czyJest==True):
            self.kombinacja.clear()
            self.kombinacja.append(random.choice(self.dostepneKombinacje))
            # self.kombinacja = list(self.kombinacja)
            self.kombinacja = [self.kombinacja[0][0], self.kombinacja[0][1], self.kombinacja[0][2],self.kombinacja[0][3]]
            if(self.kombinacja not in self.uzyteKombinacje):
                self.uzyteKombinacje.append(self.kombinacja)
                czyJest=False
        print ("aaa",self.kombinacja)
    def pierwszaKombinacja(self):
        self.kombinacja.append(red.wartosc())
        self.kombinacja.append(red.wartosc())
        self.kombinacja.append(blue.wartosc())
        self.kombinacja.append(blue.wartosc())
        self.uzyteKombinacje.append(self.kombinacja)
        print("tuuu===",self.kombinacja)
    def wszystkieKombinacje(self):
        self.dostepneKombinacje.clear()
        print("pozostalekolory4:", self.pozostaleKolory)
        for jeden in self.pozostaleKolory:
            for dwa in self.pozostaleKolory:
                for trzy in self.pozostaleKolory:
                    for cztery in self.pozostaleKolory:
                        self.dostepneKombinacje.append((jeden,dwa,trzy,cztery))
        print(self.dostepneKombinacje)
        print("a",self.dostepneKombinacje[0][0])
    def eliminuj(self,kolory):
        self.kombinacja = list(self.kombinacja)
        print("pozostale kolory === ",self.pozostaleKolory)
        print("kombinacja === ",self.kombinacja)
        print("1",self.pozostaleKolory[0])
        print("11",self.kombinacja[0])
        if (kolory == 0):
            for i in range(liczbaKolorow):
                #print("tu",self.kombinacja[i],i)#błąd
                if(self.kombinacja[i] in self.pozostaleKolory):
                    print("tak")
                    self.pozostaleKolory.remove(self.kombinacja[i])

                #print("błąd")
            print("pozostalekolory3:",self.pozostaleKolory)
            self.wszystkieKombinacje()
            self.aktualneKombinacje = list(self.dostepneKombinacje)
        elif (kolory == 1):
            pom = []
            czyJest = False
            for i in self.dostepneKombinacje:
                czyJest = False
                for kol in self.kombinacja:
                    if kol in i:
                        czyJest = True
                if (czyJest):

                    pom.append(i)

                    #print("blad")
            self.aktualneKombinacje=list(pom)
            print(pom)
        elif(kolory == 2):
            for kom in self.dostepneKombinacje:
                kombinacjaPom = list(kom)
                for wybranaKulka in self.kombinacja:
                    if(wybranaKulka in kombinacjaPom):
                        kombinacjaPom.remove(wybranaKulka)
                if(len(kombinacjaPom) <=2):
                    self.aktualneKombinacje.append(kom)
                kombinacjaPom.clear()
            print("2")
        elif(kolory == 3):
            for kom in self.dostepneKombinacje:
                kombinacjaPom = list(kom)
                for wybranaKulka in self.kombinacja:
                    if(wybranaKulka in kombinacjaPom):
                        kombinacjaPom.remove(wybranaKulka)
                if(len(kombinacjaPom) <=1):
                    #print("komdla 3 :",kombinacjaPom)
                    #print("komdla 3[0] :", kombinacjaPom[0])
                    #if(kombinacjaPom[0] not in kom):
                    self.aktualneKombinacje.append(kom)
                #elif(len(kombinacjaPom)==0):
                #    self.aktualneKombinacje.append(kom)
                kombinacjaPom.clear()
            print("3")
            print("aktkom:\n",self.aktualneKombinacje)
        elif(kolory == 4):
            for kom in self.dostepneKombinacje:
                kombinacjaPom = list(kom)
                for wybranaKulka in self.kombinacja:
                    if(wybranaKulka in kombinacjaPom):
                        kombinacjaPom.remove(wybranaKulka)
                if(len(kombinacjaPom) ==0):
                    self.aktualneKombinacje.append(kom)

                kombinacjaPom.clear()
            print("4")
        self.dostepneKombinacje = list(self.aktualneKombinacje);
        self.aktualneKombinacje.clear()


black = Kolor(0, 0, 0)
red = Kolor(200, 0, 0)
green = Kolor(0, 200, 0)
blue = Kolor(0, 0, 200)
white = Kolor(255, 255, 255)
gray = Kolor(128, 128, 128)
yellow = Kolor(255, 255, 0)
brown = Kolor(150, 75, 0)
ocean = Kolor(30, 235, 230)
purple = Kolor(184, 3, 255)
listaKolorow.append(red.wartosc())
listaKolorow.append(green.wartosc())
listaKolorow.append(blue.wartosc())
listaKolorow.append(white.wartosc())
listaKolorow.append(gray.wartosc())
listaKolorow.append(yellow.wartosc())
listaKolorow.append(brown.wartosc())
listaKolorow.append(ocean.wartosc())
listaKolorow.append(purple.wartosc())
#bright_black = Kolor(50,50,50)
bright_red = Kolor(255,0,0)
bright_green = Kolor(0,255,0)
bright_blue = Kolor(50,50,255)
bright_white = Kolor(235, 235, 235)
bright_gray= Kolor(170,170,170)
bright_yellow = Kolor(255,255,100)
bright_brown = Kolor(200,125,30)
bright_ocean = Kolor(90,255,255)
bright_purple = Kolor(200,20,255)
listaKolorowPoNajechaniu.append(bright_red.wartosc())
listaKolorowPoNajechaniu.append(bright_green.wartosc())
listaKolorowPoNajechaniu.append(bright_blue.wartosc())
listaKolorowPoNajechaniu.append(bright_white.wartosc())
listaKolorowPoNajechaniu.append(bright_gray.wartosc())
listaKolorowPoNajechaniu.append(bright_yellow.wartosc())
listaKolorowPoNajechaniu.append(bright_brown.wartosc())
listaKolorowPoNajechaniu.append(bright_ocean.wartosc())
listaKolorowPoNajechaniu.append(bright_purple.wartosc())

def dodajKoloryDoMenu():
    #dodaj kolory do menu
    pozX=325
    pozY=400
    i=0

    for i in range(9):
        kulka=Kulka(pozX, pozY, listaKolorow[i], listaKolorowPoNajechaniu[i],20)
        kulka.wypisz()
        menuKolorow.append(kulka)
        pozY = pozY +50
        if(i==2):
            pozY=400
            pozX=375
        if (i == 5):
            pozY = 400
            pozX = 425

def input(events):
    rozmiar = len(listaKombinacji)
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == pygame.locals.MOUSEBUTTONDOWN:
            for i in menuKolorow:
                i.klikniecie()
                if i.klikniete:
                    i.klikniete=False
                    #print("zmien pozycje")
        elif event.type == pygame.locals.MOUSEMOTION:
            for i in menuKolorow:
                i.najechanie()

def dodajKulkiDoPlanszy():
    #wspołrzędne aktualnej kulki
    pozXKulki = 100
    pozYKulki = 50
    for i in range (36):
        listaPozycjiKulek.append((pozXKulki,pozYKulki))
        pozXKulki = pozXKulki  +50
        if i%4 ==3:
            pozYKulki = pozYKulki +55
            pozXKulki=100
# działaj aż do przerwania




szyfr = Szyfr()


def gameLoop():
    tura =1
    while tura<=liczbaTur:

        input(pygame.event.get())
        if (szyfr.czyWygrane):
            tura =10
        pygame.display.update()
        if(len(listaKombinacji)==4 * tura):
            kombinacja =[]
            kombinacja.append(listaKombinacji[len(listaKombinacji) - 4].kolor1)
            kombinacja.append(listaKombinacji[len(listaKombinacji) - 3].kolor1)
            kombinacja.append(listaKombinacji[len(listaKombinacji) - 2].kolor1)
            kombinacja.append(listaKombinacji[len(listaKombinacji) - 1].kolor1)
            print(kombinacja)
            szyfr.sprawdz(kombinacja,tura)
            tura+=1
    szyfr.pokazSzyfr()
def gameLoopCP():
    dodajTekst("Podaj swój szyfr", 130, 50, 20)
    ai=AI()
    # input(pygame.event.get())
    licznik = 0
    while (licznik < liczbaKolorow):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                for i in menuKolorow:
                    i.klikniecie()
                    if i.klikniete:
                        i.klikniete = False
                        licznik += 1
                        window.fill((0, 0, 108))
                        pygame.display.update()
                        # print("zmien pozycje")
            elif event.type == pygame.locals.MOUSEMOTION:
                for i in menuKolorow:
                    i.najechanie()
    szyfr.szyfr.append(listaKombinacji[0].kolor1)
    szyfr.szyfr.append(listaKombinacji[1].kolor1)
    szyfr.szyfr.append(listaKombinacji[2].kolor1)
    szyfr.szyfr.append(listaKombinacji[3].kolor1)
    szyfr.pokazSzyfr()
    listaKombinacji.clear()
    pygame.display.update()
    dodajLinie()
    tura = 1
    ai.wszystkieKombinacje()
    ai.pierwszaKombinacja()
    indeks =0
    while tura <= liczbaTur:
        #print("start ------")

        input(pygame.event.get())
        pygame.display.update()

        #ai.podajKombinacje()
        print("ai.kom===== ",ai.kombinacja)
        for i in ai.kombinacja:
            kulkaSzyfru = Kulka(listaPozycjiKulek[indeks][0], listaPozycjiKulek[indeks][1],i, i, 20)
            kulkaSzyfru.wypisz()
            indeks+=1
        ai.kolory, ai.pozycje = szyfr.sprawdz(ai.kombinacja, tura,czyZrwacac=True)
        ai.eliminuj(ai.kolory)
        szyfr.sprawdz(ai.kombinacja, tura)
        if (szyfr.czyWygrane):
            tura =10
        else:
            ai.podajKombinacje()
            #print(ai.kolory, ai.pozycje)
            tura += 1
            time.sleep(3)
        #print("stop ------")
    szyfr.pokazSzyfr()
    #time.sleep(20)
def gameLoopPP():
    dodajTekst("Podaj swój szyfr", 130, 50, 20)
    licznik = 0
    while (licznik < liczbaKolorow):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                for i in menuKolorow:
                    i.klikniecie()
                    if i.klikniete:
                        i.klikniete = False
                        licznik += 1
                        window.fill((0, 0, 108))
                        pygame.display.update()
                        # print("zmien pozycje")
            elif event.type == pygame.locals.MOUSEMOTION:
                for i in menuKolorow:
                    i.najechanie()
    szyfr.szyfr.append(listaKombinacji[0].kolor1)
    szyfr.szyfr.append(listaKombinacji[1].kolor1)
    szyfr.szyfr.append(listaKombinacji[2].kolor1)
    szyfr.szyfr.append(listaKombinacji[3].kolor1)
    #szyfr.pokazSzyfr()
    listaKombinacji.clear()
    pygame.display.update()
    dodajLinie()
    gameLoop()
def klik(x,y,dlX,dlY):
    mouse = pygame.mouse.get_pos()
    if (mouse[0] >= x and mouse[0] <= x + dlX and mouse[1] >= y and mouse[1] <=y + dlY):
        return 1
    else:
        return 0
def dodajTekst(tekst,cenX,cenY,wielkosc =13,kolor=black.wartosc()):
    czcionka = pygame.font.Font('freesansbold.ttf', wielkosc)
    TextSurf = czcionka.render(tekst, True, kolor)
    TextRect = TextSurf.get_rect()
    TextRect.center = (cenX, cenY)
    window.blit(TextSurf, TextRect)
    pygame.display.update()
def instrukcja():
    window.fill((0, 0, 108))
    pygame.display.update()
    dodajTekst("INSTRUKCJA",130,50,20)
    dodajTekst("Gra Master Mind polega na odgadywaniu szyfru złożonego z kolorowych kulek.          ",279,100)
    dodajTekst("Każda gra składa się z 9 tur(prób) w których gracz podaje swoją kombinację.         ",265,150)
    dodajTekst("Kolorowe kulki w szyfsze mogą się powtarzać.                                        ",236,200)
    dodajTekst("Po podaniu swojej kombinacji komputer sprawdza poprawność szyfru.                   ",271,250)
    dodajTekst("Jeśli jakiś kolor z podajen kombinacji jest w szyfrze to wyświetli niebieską,       ",259,300)
    dodajTekst("jeśli jest na swojej pozycji wyświetli czerwoną kulkę, w innym razie białą.         ",259,350)
    dodajTekst("Gracz do odgadnięcia szyfru korzysta z wyświetlanych podpowiedzi.                   ",264,400)
    dodajTekst("Do wyboru gracz ma 9 różnych kolorów                                                ",230,450)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
def dodajLinie():
    pygame.draw.line(window,black.wartosc(),(70,30),(70,520),4)
    y=79
    for i in range(liczbaTur):
        pygame.draw.line(window, black.wartosc(), (10, y), (280, y), 3)
        y+=55

def menu():
    window.fill(white.wartosc())
    pygame.draw.rect(window, green.wartosc(), (175, 100, 150, 50))  #PLAYER vs COMPUTER
    pygame.draw.rect(window, green.wartosc(), (175, 200, 150, 50))  #COMPUTER vs PLAYER
    pygame.draw.rect(window, green.wartosc(), (175, 300, 150, 50))  # PLAYER vs PLAYER
    pygame.draw.rect(window, green.wartosc(), (175, 400, 150, 50))  # INSTRUCTION
    pygame.draw.rect(window, green.wartosc(), (175, 500, 150, 50))  # EXIT

    dodajTekst("PLAYER vs COMPUTER", 250, 125)
    dodajTekst("COMPUTER vs PLAYER", 250, 225)
    dodajTekst("PLAYER vs PLAYER",   250, 325)
    dodajTekst("INSTRUCTION",        250, 425)
    dodajTekst("EXIT",               250, 525)
    pygame.display.flip()
    szyfr.szyfr.clear()
    szyfr.czyWygrane=False
    listaKombinacji.clear()
    liczbaTur=0
    koniec = 0
    kontynuowac =0
    while koniec != 1:
        # input(pygame.event.get())
        # ind =
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == 5:
                if (klik(150, 100, 150, 50)):
                    koniec = 1
                    rodzajGry = "PC"
                elif (klik(150, 200, 150, 50)):
                    koniec = 1
                    rodzajGry = "CP"
                elif (klik(150, 300, 150, 50)):
                    koniec = 1
                    rodzajGry = "PP"
                elif (klik(150, 400, 150, 50)):
                    koniec = 1
                    rodzajGry = "I"
                elif (klik(150, 500, 150, 50)):
                    koniec = 1
                    rodzajGry = "E"
    if (rodzajGry == "PC"):
        window.fill((0, 0, 108))
        pygame.display.update()
        szyfr.losuj()
        print(szyfr.szyfr)
        dodajLinie()
        gameLoop()
        kontynuowac=0
    elif (rodzajGry == "CP"):
        window.fill((0, 0, 108))
        pygame.display.update()

        gameLoopCP()
        print("CP")
        kontynuowac = 0
    elif (rodzajGry == "PP"):
        window.fill((0, 0, 108))
        pygame.display.update()

        gameLoopPP()
        print("PP")
        kontynuowac = 0
    elif (rodzajGry == "I"):
        print("I")
        instrukcja()
        kontynuowac = 1
    elif (rodzajGry == "E"):
        print("E")
        kontynuowac = 2
    if(kontynuowac ==0):
        if (szyfr.czyWygrane):
            tekst = "WYGRANA"
        else:
            tekst = "PRZEGRANA"
        running = True

        while running:
            dodajTekst(tekst, 200, 500, 50,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
        menu()
    elif(kontynuowac ==1):
        menu()

pygame.init()
# utworzenie okna
window = pygame.display.set_mode((510, 600))
dodajKoloryDoMenu()
dodajKulkiDoPlanszy()

szyfr.losuj()

print(listaKolorow)
#print(szyfr.szyfr)

menu()