# Librairie importer
import time
import keyboard

horloge = (13, 10, 25)
reveil = (13, 10, 28)

def alarme(reveil, horloge):
    if horloge == reveil:
        print("C'est l'heure de se réveiller !")

def format_heure(h, m, s):
    if h < 12:
        am_pm = "AM"
    else:
        am_pm = "PM"

    h = h % 12
    if h == 0:
        h = 12

    return f"{h:02d}:{m:02d}:{s:02d} {am_pm}"

def espace(keyboard_event):
    global en_pause
    if keyboard_event.event_type == keyboard.KEY_DOWN:
        en_pause = not en_pause

def affichage_heure(horloge):
    global en_pause
    en_pause = False
    keyboard.on_press_key('space', espace)

    format_choisi = input("Choisissez le format d'heure (12 ou 24) : ")
    print("Pour mettre l'horloge en pause veuillez appuyez sur la barre espace.")

    h, m, s = horloge
    while True:
        try:
            if en_pause:
                time.sleep(0.1)
                continue

            alarme(reveil, (h, m, s))

            if format_choisi == "12":
                heure = format_heure(h, m, s)
            elif format_choisi == "24":
                heure = f"{h:02d}:{m:02d}:{s:02d}"
            else: 
                print("Format non valide, utilisation du format 24h par défaut")
                heure = f"{h:02d}:{m:02d}:{s:02d}"

            print(heure, end="\r")
            s += 1

            if s == 60:
                s = 0
                m += 1
                if m == 60:
                    m = 0
                    h += 1
                    if h == 24:
                        h = 0

            time.sleep(1)
        except KeyboardInterrupt:
            break       

affichage_heure(horloge)