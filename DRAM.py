from tkinter import *
from turtle import *
from tkinter.messagebox import *
import random
import time
COLORS = ['gray', 'midnight blue', 'navy', 'royal blue',  'blue',
    'sky blue','cyan', 'dark green', 
    'dark sea green',  'spring green', 'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'dark khaki', 'yellow', 'gold', 'dark goldenrod','saddle brown','orange', 'dark orange',
    'coral','tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pale violet red', 'medium violet red', 'violet red',
    'dark violet', 'blue violet', 'purple', 'medium purple', 'LavenderBlush2','LavenderBlush4']
obrisaniSviGumbi = True
pravokutnici = []
gumbi = []
zauzetaMjesta=[]
gumbiZaBrisanje=[]
mjestaZaGumbe = []
poljePreslagivanja=[]
poljePraznih =  []
brojac = 0
br = 0
brojSlobodnih = 40

def brisanjeMemorije(polje):
    k = -1
    kProcitan = False
    global pravokutnici
    global canvas
    global br
    global zauzetaMjesta
    global mjestaZaGumbe
    global brojSlobodnih
    global obrisaniSviGumbi
    redniBroj = polje[0]
    kolikoMjesta = polje[2]
    isPreslagivanje = polje[3]
    redniBrGumba = polje[4]
    i = 0
    for i in range(len(zauzetaMjesta)):
        if zauzetaMjesta[i] == redniBroj:
            if (not kProcitan):
                k = i
                kProcitan = True
            canvas.itemconfig(pravokutnici[i], fill = "White")
            zauzetaMjesta[i] = -1
            brojSlobodnih += 1
            
    if (not obrisaniSviGumbi) and isPreslagivanje != -1:
        obrisaniSviGumbi = True
        for i in range(0,len(gumbiZaBrisanje)):
            if gumbiZaBrisanje[i] != 0:
                gumbiZaBrisanje[i].destroy()
                gumbiZaBrisanje[i] = 0
            mjestaZaGumbe[i] = 0
    
    elif isPreslagivanje == -1: 
        br -= 1
        COLORS.append(polje[1])
        if k != -1:
            gumbiZaBrisanje[k].destroy()
            gumbiZaBrisanje[k] = 0
            mjestaZaGumbe[redniBrGumba] = 0
            poljePreslagivanja[k] = -1
    return
    
def preslagivanje():
    i = 0
    redniBroj = 0
    global br
    global canvas
    global brojac
    global gumbiZaBrisanje
    global glavniProzor
    global COLORS
    global pravokutnici
    global canvas
    global mjestaZaGumbe
    global brojSlobodnih
    global obrisaniSviGumbi

    obrisaniSviGumbi = False
    for i in range(len(poljePreslagivanja)):
        if poljePreslagivanja[i] != -1:
            redniBroj = zauzetaMjesta[poljePreslagivanja[i]]
            color = canvas.gettags(pravokutnici[i])[0] + canvas.gettags(pravokutnici[i])[1]
            koliko = zauzetaMjesta.count(zauzetaMjesta[poljePreslagivanja[i]])
            brisanjeMemorije([redniBroj, color, koliko, poljePreslagivanja[i], 0])
            poljePreslagivanja[i] = -1
            zauzimanjeMemorijePilikomPreslagivanja([koliko - 1, color])
            
            
def trazenjeNajmanjeg(kolikoMjesta):
    global brojac
    global zauzetaMjesta
    i = 0
    k = 0
    pomakUPolju = 0
    counter = 0
    poljeBrojaRupa=[]
    poljeIndeksa=[]
    for k in range(0, 40):
        poljeBrojaRupa.append(0)
        poljeIndeksa.append(0)
    minBrRupa = 100
    while i < 40:
        for j in range(i, 40):
            if zauzetaMjesta[j] == -1:
                counter += 1
            else:
                break
        if counter > 0 :
            poljeBrojaRupa[pomakUPolju] = counter
            poljeIndeksa[pomakUPolju] = i
            if poljeBrojaRupa[pomakUPolju] < minBrRupa and poljeBrojaRupa[pomakUPolju] >= kolikoMjesta:
                minBrRupa = poljeBrojaRupa[pomakUPolju]
            pomakUPolju += 1
        i = i + counter + 1
        counter = 0
        
    for k in range(0, len(poljeBrojaRupa)):
        if poljeBrojaRupa[k] == minBrRupa:
            break;
    if minBrRupa != 100:
        return poljeIndeksa[k]
    else:
        return -1

def zauzimanjeMemorijePilikomPreslagivanja(polje):
    kolikoMjesta = polje[0]
    preodredenaBoja = polje[1]
    
    i = 0
    j = 0
    k = 0
    zauzeo = False
    global br
    global canvas
    global brojac
    global gumbiZaBrisanje
    global glavniProzor
    global COLORS
    global pravokutnici
    global canvas
    global mjestaZaGumbe
    global brojSlobodnih
    for i in range(len(zauzetaMjesta) - kolikoMjesta):
        slobodno = True
        j = 0
        for j in range(kolikoMjesta + 1):
            if zauzetaMjesta[i+j] != -1:
                slobodno = False
                break
        if slobodno:
            zauzeo = True
            poljePreslagivanja[i] = i
            if preodredenaBoja == "":
                boja = COLORS[random.randint(0, len(COLORS)-br - 1)]
                COLORS.remove(boja)
                br += 1
            else:
                boja = preodredenaBoja
            brojSlobodnih = brojSlobodnih -(kolikoMjesta + 1)
            for k in range(len(mjestaZaGumbe)):
                if mjestaZaGumbe[k] == 0:
                    break
            if k > 17:
                showerror("Dogodila se pogreska", "Nažalost na prozoru više nema mjesta tako da cu vas zamoliti da oslobodite blokove ili krenete ispocetka! Hvala")
                break;
            if k>11:
                gumbiZaBrisanje[i] = Button(glavniProzor, text=" ",bg = boja, height = 1, fg="Black", font=("Arial",20,"bold"),borderwidth=0,command=lambda arg = [brojac, boja, kolikoMjesta, -1, k]: brisanjeMemorije(arg))
                gumbiZaBrisanje[i].place(x = 600 + (k-12)*60, y=470)
                mjestaZaGumbe[k] = 1
            elif k>5:
                gumbiZaBrisanje[i] = Button(glavniProzor, text=" ",bg = boja, height = 1, fg="Black", font=("Arial",20,"bold"),borderwidth=0,command=lambda arg = [brojac, boja, kolikoMjesta, -1, k]: brisanjeMemorije(arg))
                gumbiZaBrisanje[i].place(x = 600 + (k-6)*60, y=400)
                mjestaZaGumbe[k] = 1
            else:
                
                gumbiZaBrisanje[i] = Button(glavniProzor, text=" ",bg = boja, height = 1, fg="Black", font=("Arial",20,"bold"),borderwidth=0,command=lambda arg = [brojac, boja, kolikoMjesta, -1, k]: brisanjeMemorije(arg))
                gumbiZaBrisanje[i].place(x = 600 + k*60, y=330)
                mjestaZaGumbe[k] = 1
            k = 0
            for k in range(kolikoMjesta + 1):
                zauzetaMjesta[i + k] = brojac
                canvas.itemconfig(pravokutnici[i+k], fill = boja, tags=(boja, ""))
            brojac += 1
            return
    if (not zauzeo) and brojSlobodnih >= kolikoMjesta + 1:
        preslagivanje()
        zauzimanjeMemorije([kolikoMjesta, ""])
        slobodno = True
    if slobodno == False:
        showerror("Dogodila se pogreska", "Nazalost tolika kolicina memorije ne moze se trenutno rezervirati!")
    
        
def zauzimanjeMemorije(polje):
    kolikoMjesta = polje[0]
    preodredenaBoja = polje[1]
    i = 0
    
    j = 0
    k = 0
    zauzeo = False
    
    global br
    global canvas
    global brojac
    global gumbiZaBrisanje
    global glavniProzor
    global COLORS
    global pravokutnici
    global canvas
    global mjestaZaGumbe
    global brojSlobodnih
    i = trazenjeNajmanjeg(kolikoMjesta + 1)
    slobodno = False
    k = 0
    for k in range(len(mjestaZaGumbe)):
            if mjestaZaGumbe[k] == 0:
                break
    if i != -1 :
        slobodno = True
        zauzeo = True
        poljePreslagivanja[i] = i
        if preodredenaBoja == "" and k < 18:
            boja = COLORS[random.randint(0, len(COLORS)-br - 1)]
            COLORS.remove(boja)
            br += 1
        else:
            boja = preodredenaBoja
        
        if k > 17:
            showerror("Dogodila se pogreska", "Nažalost na prozoru više nema mjesta tako da cu vas zamoliti da oslobodite blokove ili krenete ispocetka! Hvala")
            return
        if k>11:
            gumbiZaBrisanje[i] = Button(glavniProzor, text=" ",bg = boja, height = 1, fg="Black", font=("Arial",20,"bold"),borderwidth=0,command=lambda arg = [brojac, boja, kolikoMjesta, -1, k]: brisanjeMemorije(arg))
            gumbiZaBrisanje[i].place(x = 600 + (k-12)*60, y=470)
            mjestaZaGumbe[k] = 1
        elif k>5:
            gumbiZaBrisanje[i] = Button(glavniProzor, text=" ",bg = boja, height = 1, fg="Black", font=("Arial",20,"bold"),borderwidth=0,command=lambda arg = [brojac, boja, kolikoMjesta, -1, k]: brisanjeMemorije(arg))
            gumbiZaBrisanje[i].place(x = 600 + (k-6)*60, y=400)
            mjestaZaGumbe[k] = 1
        else:
            gumbiZaBrisanje[i] = Button(glavniProzor, text=" ",bg = boja, height = 1, fg="Black", font=("Arial",20,"bold"),borderwidth=0,command=lambda arg = [brojac, boja, kolikoMjesta, -1, k]: brisanjeMemorije(arg))
            gumbiZaBrisanje[i].place(x = 600 + k*60, y=330)
            mjestaZaGumbe[k] = 1
        k = 0
        for k in range(kolikoMjesta + 1):
            zauzetaMjesta[i + k] = brojac
            canvas.itemconfig(pravokutnici[i+k], fill = boja, tags=(boja, ""))
            brojSlobodnih -= 1
        brojac += 1
        return
    if (not zauzeo) and brojSlobodnih >= kolikoMjesta + 1 and k < 18:
        preslagivanje()
        zauzimanjeMemorije([kolikoMjesta, ""])
        slobodno = True
        return
    if slobodno == False:
        showerror("Dogodila se pogreska", "Nazalost tolika kolicina memorije ne moze se trenutno rezervirati!")

def inicijalizacija():
    global pravokutnici
    global mjestaZaGumbe
    global poljePraznih

    for i in range(40):
        mjestaZaGumbe.append(0)
        poljePraznih.append(0)
    for i in range(40):
        zauzetaMjesta.append(-1)
    for i in range(40):
        poljePreslagivanja.append(-1)
    for i in range(40):
        gumbiZaBrisanje.append(0)

def stvaranjeProzora():
    global glavniProzor
    global gumbi
    naslov = Label(glavniProzor, text="Dinamicko rasporedivanje memorije", bg="White",font=("Arial", 30, "bold"))
    naslov.place(x=500, y=40, anchor="center")
    gumbNaslov = Label(glavniProzor, text="Izaberite broj blokova:", bg="White",font=("Arial", 20, "bold"))
    gumbNaslov.place(x=750, y = 125, anchor="center")
    brojevi = [0,1,2,3,4,5,6,7,8,9,10]
    for i in range(10):
        broj = Label(glavniProzor, text=str(i + 1), bg="White",font=("Arial", 10, "bold"))
        broj.place(x=15, y=140 + i*40, anchor="center")
    for i in range(10):
        broj = Label(glavniProzor, text=str(i + 11), bg="White",font=("Arial", 10, "bold"))
        broj.place(x=135, y=140 + i*40, anchor="center")
    for i in range(10):
        broj = Label(glavniProzor, text=str(i + 21), bg="White",font=("Arial", 10, "bold"))
        broj.place(x=255, y=140 + i*40, anchor="center")
    for i in range(10):
        broj = Label(glavniProzor, text=str(i + 31), bg="White",font=("Arial", 10, "bold"))
        broj.place(x=375, y=140 + i*40, anchor="center")
        
    for i in range(5):
        gumbi = gumbi + [Button(glavniProzor, text=str(i+1),bg="white", fg="Black", font=("Arial",30,"bold"),borderwidth=0,command=lambda arg=[brojevi[i], ""]: zauzimanjeMemorije(arg))]
        gumbi[i].place(x=600 + i * 60,y=150)
        
    for i in range(5):
        gumbi = gumbi + [Button(glavniProzor, text=str(i+6),bg="white", fg="Black", font=("Arial",30,"bold"),borderwidth=0,command=lambda arg=[brojevi[i+5], ""]: zauzimanjeMemorije(arg))]
        gumbi[i + 5].place(x=600 + i * 60,y=210)
    
    naslovZaUnistavanje = Label(glavniProzor, text="Otpustite blok pritiskom na njega:", bg="White",font=("Arial", 18, "bold"))
    naslovZaUnistavanje.place(x=755, y=310, anchor="center")

def main():
    global glavniProzor
    glavniProzor = Tk()
    glavniProzor.title("Dinamicko rasporedivanje memorije")
    glavniProzor.config(bg="white")
    glavniProzor.resizable(False, False)
    glavniProzor.geometry("1000x600")

    global canvas
    canvas = Canvas(glavniProzor, width = 1000, height = 600, borderwidth = 0, bg="White")
    canvas.grid()
    stvaranjeProzora()
    inicijalizacija()
    
    global pravokutnici
    for i in range(10):
        pravokutnik = canvas.create_rectangle(25, 120 + 40 * i, 100, 160 + 40 * i, fill = "white", outline = "black")
        pravokutnici = pravokutnici + [pravokutnik]
    for i in range(10):
        pravokutnik = canvas.create_rectangle(145, 120 + 40 * i, 220, 160 + 40 * i, fill = "white", outline = "black")
        pravokutnici = pravokutnici + [pravokutnik]
    for i in range(10):
        pravokutnik = canvas.create_rectangle(265, 120 + 40 * i, 340, 160 + 40 * i, fill = "white", outline = "black")
        pravokutnici = pravokutnici + [pravokutnik]
    for i in range(10):
        pravokutnik = canvas.create_rectangle(385, 120 + 40 * i, 460, 160 + 40 * i, fill = "white", outline = "black")
        pravokutnici = pravokutnici + [pravokutnik]

main()




