import os
import sys

plansza = {
    "top_l" : " ", "top_m" : " ", "top_r" : " ",
    "mid_l" : " ", "mid_m" : " ", "mid_r" : " ",
    "bot_l" : " ", "bot_m" : " ", "bot_r" : " "
}

dostepne_ruchy = ["top_l","top_m","top_r","mid_l","mid_m","mid_r","bot_l","bot_m","bot_r"]

def wypisz(dict):
    print(dict["top_l"]+" | "+dict["top_m"]+"| "+dict["top_r"])
    print("--+--+--")
    print(dict["mid_l"]+" | "+dict["mid_m"]+"| "+dict["mid_r"])
    print("--+--+--")
    print(dict["bot_l"]+" | "+dict["bot_m"]+"| "+dict["bot_r"])

def sprawdz_dwojki(do_sprawdzenia,plansza,znak):    #do szukania dwójek gracza i naszych
    # i = 0
    # while(i<3):
    #     if(plansza[do_sprawdzenia[i]] == znak):
    #         licznik += 1
    #         del do_sprawdzenia[i]
    #     if(licznik == 2):
    #         return do_sprawdzenia[0]
    #     i += 1
    # if(licznik<2):
    #     return 0

    # for i in do_sprawdzenia:
    #     if(plansza[i] == znak):
    #         licznik += 1
    #         do_sprawdzenia.remove(i)
    # if(licznik == 2):
    #     return do_sprawdzenia[0]
    # else:
    #     return 0
    # licznik = 0
    # for i in do_sprawdzenia:
    #     if(plansza[do_sprawdzenia[0]] == znak):
    #         licznik += 1
    #         del do_sprawdzenia[0]
    # if(licznik == 2):
    #     if(plansza[do_sprawdzenia[0]] == " "):
    #         return do_sprawdzenia[0]
    #     else:
    #         return 0
    # else:
    #     return 0
    licznik = 0
    for i in do_sprawdzenia:
        if(plansza[i] == znak):
            licznik += 1
        else:
            ostatni = i
    if(licznik == 2):
        if(plansza[ostatni] == " "):
            return ostatni
        else:
            return 0
    else:
        return 0

def calculateMove(plansza,wybor,enemy,dostepne_ruchy):
    #tutaj oblicz następny ruch i zwróc go w formacie takim jak określenia na planszy
    #najpierw sprawdzamy czy gracz gdzieś nie ma już dwójki
    #jeśli ma to ją blokujemy
    #sprawdzamy czy my gdzieś mamy dwójkę, a jeśli tak to ją dopełniamy
    #jeśli jej nie mamy to sprawdzamy czy środek jest zajęty
    #jeśli nie jest zajęty to go zajmujemy
    #jeśli jest zajęty to szukamy rogu który jest na przecięciu rzędów jak najmniej zajętych przez przeciwnika
    #w przeciwnym wypadku szukamy bocznych środków w rzędach(kolumnach gdzie już coś mamy)
    #w przeciwnym wypadku zajmujemy którykolwiek boczny środek

    #albo inaczej
    #najpierw sprawdzamy czy gracz gdzieś nie ma już dwójki
    #jeśli ma to ją blokujemy
    #sprawdzamy czy my gdzieś mamy dwójkę, a jeśli tak to ją dopełniamy i wygrywamy
    #jeśli jej nie mamy to sprawdzamy czy środek jest zajęty
    #jeśli nie jest zajęty to go zajmujemy
    #jeśli środek jest zajęty to dopiero teraz zaczyna się zabawa
    #jeśli środek jest zajęty przez nas to szukamy pustych rogów i zajmujemy taki gdzie mamy jak najwięcej możliwości wygranej
    #jeśli środek jest zajęty przez przeciwnika to przechodzimy przez 6 innych możliwości wygranej(ale nie mamy dwójki)
    a = sprawdz_dwojki(["top_l","top_m","top_r"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["mid_l","mid_m","mid_r"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["bot_l","bot_m","bot_r"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_l","mid_l","bot_l"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_m","mid_m","bot_m"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_r","mid_r","bot_r"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_l","mid_m","bot_r"],plansza,enemy)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_r","mid_m","bot_l"],plansza,enemy)
    if(a != 0):
        return a

    a = sprawdz_dwojki(["top_l","top_m","top_r"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["mid_l","mid_m","mid_r"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["bot_l","bot_m","bot_r"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_l","mid_l","bot_l"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_m","mid_m","bot_m"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_r","mid_r","bot_r"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_l","mid_m","bot_r"],plansza,wybor)
    if(a != 0):
        return a
    a = sprawdz_dwojki(["top_r","mid_m","bot_l"],plansza,wybor)
    if(a != 0):
        return a


    if(plansza["mid_m"] == " "):
        return "mid_m"
    else:
        if(plansza["mid_m"] == enemy):#my zajęliśmy środek
            if(plansza["top_l"] == " "):
                if(plansza["bot_r"] == " "):
                    a = 0
                    b = 0
                    a += (plansza["top_m"] == wybor) + (plansza["top_r"] == wybor) + (plansza["mid_l"] == wybor) + (plansza["bot_l"]==wybor)
                    b += (plansza["bot_m"] == wybor) + (plansza["bot_l"] == wybor) + (plansza["mid_r"] == wybor) + (plansza["top_r"]==wybor)
                    if(a <= b):
                        return "top_l"
                    else:
                        return "bot_r"
                else:
                    return dostepne_ruchy[0]
            elif(plansza["top_r"] == " "):
                if(plansza["bot_l"] == " "):
                    a = 0
                    b = 0
                    a += (plansza["top_m"] == wybor) + (plansza["top_l"] == wybor) + (plansza["mid_r"] == wybor) + (plansza["bot_r"]==wybor)
                    b += (plansza["bot_m"] == wybor) + (plansza["bot_r"] == wybor) + (plansza["mid_l"] == wybor) + (plansza["top_l"]==wybor)
                    if(a <= b):
                        return "top_r"
                    else:
                        return "bot_l"
                else:
                    return dostepne_ruchy[0]
            else:
                return dostepne_ruchy[0]
        else:#gracz zajął środek
            return dostepne_ruchy[0]


def isWin(dict):
    #tutaj sprawdź czy osiągnięte zostało zwycięstwo, zmień flagę zwycięstwa i zwróc kto wygrał
    if(dict["top_l"] == 'x' and dict["top_m"] == 'x' and dict["top_r"] == 'x'):
        return [True,'x']
    if(dict["mid_l"] == 'x' and dict["mid_m"] == 'x' and dict["mid_r"] == 'x'):
        return [True,'x']
    if(dict["bot_l"] == 'x' and dict["bot_m"] == 'x' and dict["bot_r"] == 'x'):
        return [True,'x']
    if(dict["top_l"] == 'x' and dict["mid_l"] == 'x' and dict["bot_l"] == 'x'):
        return [True,'x']
    if(dict["top_m"] == 'x' and dict["mid_m"] == 'x' and dict["bot_m"] == 'x'):
        return [True,'x']
    if(dict["top_r"] == 'x' and dict["mid_r"] == 'x' and dict["bot_r"] == 'x'):
        return [True,'x']
    if(dict["top_l"] == 'x' and dict["mid_m"] == 'x' and dict["bot_r"] == 'x'):
        return [True,'x']
    if(dict["top_r"] == 'x' and dict["mid_m"] == 'x' and dict["bot_l"] == 'x'):
        return [True,'x']
    
    if(dict["top_l"] == 'o' and dict["top_m"] == 'o' and dict["top_r"] == 'o'):
        return [True,'o']
    if(dict["mid_l"] == 'o' and dict["mid_m"] == 'o' and dict["mid_r"] == 'o'):
        return [True,'o']
    if(dict["bot_l"] == 'o' and dict["bot_m"] == 'o' and dict["bot_r"] == 'o'):
        return [True,'o']
    if(dict["top_l"] == 'o' and dict["mid_l"] == 'o' and dict["bot_l"] == 'o'):
        return [True,'o']
    if(dict["top_m"] == 'o' and dict["mid_m"] == 'o' and dict["bot_m"] == 'o'):
        return [True,'o']
    if(dict["top_r"] == 'o' and dict["mid_r"] == 'o' and dict["bot_r"] == 'o'):
        return [True,'o']
    if(dict["top_l"] == 'o' and dict["mid_m"] == 'o' and dict["bot_r"] == 'o'):
        return [True,'o']
    if(dict["top_r"] == 'o' and dict["mid_m"] == 'o' and dict["bot_l"] == 'o'):
        return [True,'o']
    
    return [False,'remis']


os.system("cls")
print("Witaj w grze kółko i krzyżyk!".center(41,'*'))

def gra():
    global plansza
    plansza = {
        "top_l" : " ", "top_m" : " ", "top_r" : " ",
        "mid_l" : " ", "mid_m" : " ", "mid_r" : " ",
        "bot_l" : " ", "bot_m" : " ", "bot_r" : " "
    }
    global dostepne_ruchy
    dostepne_ruchy = ["top_l","top_m","top_r","mid_l","mid_m","mid_r","bot_l","bot_m","bot_r"]
    while(True):
        print("wpisz o jeśli chcesz grać kółkiem lub x jeśli krzyżykiem lub wpisz spację żeby zakończyć")
        wybor = str(input())
        if(wybor == 'o'):
            enemy = 'x'
            break
        elif(wybor == 'x'):
            enemy = 'o'
            break
        elif(wybor == ' '):
            sys.exit()
        else:
            os.system("cls")
            print("Złe dane")

    wypisz(plansza)

    while(dostepne_ruchy):
        print("Podaj ruch w dobrym formacie: ")
        ruch = str(input())
        if(ruch in dostepne_ruchy):
            plansza[ruch] = wybor
            dostepne_ruchy.remove(ruch)
            os.system("cls")
            wypisz(plansza)
            input()
            flaga_win,zwyc = isWin(plansza)
            if(flaga_win == False and dostepne_ruchy):
                a = calculateMove(plansza,wybor,enemy,dostepne_ruchy)
                plansza[a] = enemy
                dostepne_ruchy.remove(a)
                os.system("cls")
                wypisz(plansza)
                flaga_win,zwyc = isWin(plansza)
                if(flaga_win == True):
                    break
            else:
                break
        else:
            print("ten ruch już wykonano")
    print("zwycięzca: " + zwyc)
    input()
    os.system("cls")
while(True):
    gra()

