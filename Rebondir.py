from tkinter import *
import random
import time

class Balle:
    def __init__(self, canvas, raquette, egg, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.egg = egg
        self.id = canvas.create_oval(10, 10, 25, 25, fill=couleur)
        self.canvas.move(self.id, 245, 100)
        departs = [-3, -2, -1, 1, 2, 3]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        self.hauteur_canevas = self.canvas.winfo_height() #pour mesurer la hauteur du canvas
        self.largeur_canevas = self.canvas.winfo_width()  #pour mesurer la largeur du canvas
        self.touche_bas = False
        self.score = 0
        self.score_str = str(self.score)

    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                self.score = self.score + 1
                return True
        return False

    def heurter_easter_egg(self, pos):
        pos_easter_egg = self.canvas.coords(self.egg.id)
        if pos[2] >= pos_easter_egg[0] and pos[0] <= pos_easter_egg[2] and egg.heurter_egg == True :
            if pos[3] >= pos_easter_egg[1] and pos[3] <= pos_easter_egg[3] :
                if self.score >= 1000:
                    self.score = self.score + 111111111111111111111111111111111
                else:
                    self.score = self.score +3
                return True
        return False
    
    

    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)#prise de mouvement par les variables x et y
        self.pos = self.canvas.coords(self.id)#prend les cordonées de la balle 
        if self.pos[1] <= 0 : #condition pour changé la direction de la balle si elle atteint le haut de l'écrant
            if egg.heurter_egg == True:
                if self.score >= 1000:
                    self.y = 30
                else :
                    self.y = 20
            else:
                self.y = 4
        if self.pos[3] >= self.hauteur_canevas:#condition pour terminé la partie si la balle touche le bas de l'écrant
            self.touche_bas = True
        if self.heurter_raquette(self.pos) == True:
            self.y = -7
        if self.heurter_easter_egg(self.pos) == True:
            if self.score >= 1000:
                self.y = -30
            else :
                self.y = -20
        if self.pos[0] <= 0:  #condition pour changé la direction de la balle si elle touche la gauche de l'écrant
            if egg.heurter_egg == True:
                if self.score >= 1000:
                    self.x = 30
                else :
                    self.x = 20
            else:
                self.x = 3
        if self.pos[2] >= self.largeur_canevas: #condition pour changé la direction de la balle si elle touche la droite de l'écrant 
            if egg.heurter_egg == True:
                if self.score >= 1000:
                    self.x = -30
                else :
                    self.x = -20
            else:
                self.x = -3

            
class Raquette:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=couleur)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.largeur_canevas = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.vers_gauche) #mise en place du input utilisateur
        self.canvas.bind_all('<KeyPress-Right>', self.vers_droite)#mise en place du input utilisateur
        self.canvas.bind_all('<Button-1>', self.clique_sourit)
        self.canvas.bind_all('<KeyPress-k>', self.restart)
        self.canvas.bind_all('<KeyPress-e>', self.easter_egg_fonc)
        self.inp_sourit = False
        self.restart_var = False
        self.easter_egg_var = False


    def vers_gauche(self, evt):
        self.x = -3

    def vers_droite(self, evt):
        self.x = 3

    def clique_sourit(self, evt):
        self.inp_sourit = True

    def restart(self, evt):
        self.restart_var = True

    def easter_egg_fonc(self, evt):
        self.easter_egg_var = True
        
        
        
    def dessiner(self):
        self.canvas.move(self.id, self.x, 0)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0] <= 0 :
            self.x = 0
        elif self.pos[2] >= self.largeur_canevas:
            self.x = 0
            
class easter_egg:
    
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10000, 10, fill=couleur)
        self.canvas.move(self.id, 0, 150)
        self.canvas.itemconfig(self.id, stat='hidden')
        self.heurter_egg = False

    def dessiner(self):
        self.canvas.itemconfig(self.id, stat='normal')
        self.heurter_egg = True
        

    


tk = Tk()
tk.title("Rebondir")
tk.resizable(0, 0) #resizable est utilisé pour empèché l'agrandissement manuel de l'utilisateur de la fenêtre 
tk.wm_attributes("-topmost", 1) #Cette ligne sert a placé la fenetre a l'avant plan 
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0) #argument bd et higlightthickness sur 0 pour empèché l'apparition de bordur
canvas.pack()
tk.update()


raquette = Raquette(canvas, 'blue')
egg = easter_egg(canvas, 'green')
balle = Balle(canvas, raquette, egg, 'red')


score_text = canvas.create_text(450, 10, text=('Score:' + balle.score_str), font=('Courier', 13), fill='green') 


while 1:
    if balle.score == 'ERREUR':
        break
    if raquette.inp_sourit == True :
        if balle.touche_bas == False:
            balle.dessiner()
            raquette.dessiner()
    if balle.touche_bas == True:
        time.sleep(0.1)
        game_over_text = canvas.create_text(250, 200, text='GAME OVER', font=('Courier', 30), fill='red')
        restart_text = canvas.create_text(250, 230, text='<press K for restart>', font=('Courier',15), fill='green')
        while 2 :
            if raquette.restart_var == True:
                balle.touche_bas = False
                raquette.restart_var = False
                raquette.inp_sourit = False
                canvas.itemconfig(game_over_text, text='')
                canvas.itemconfig(restart_text, text='')
                balle.score = 0
                #print(balle.pos[0]) #a utilisé si bugs
                balle.canvas.move(balle.id, 245 - balle.pos[0], -300)
                raquette.canvas.move(raquette.id, 200 - raquette.pos[0], 0)
                balle.y = -3
                raquette.x = 0
                tk.update()
                break
            canvas.itemconfig(restart_text, text='')
            tk.update()
            time.sleep(0.7)
            canvas.itemconfig(restart_text, text='<press k for restart>')
            tk.update()
            time.sleep(0.7)
    if raquette.easter_egg_var == True and balle.score != 6 :
        raquette.easter_egg_var = False
        
    if balle.score == 6 and raquette.easter_egg_var == True :
        print("Easter_egg enclenché")
        easter_egg_text = canvas.create_text(250, 200, text='EASTER EGG', font=('Courier', 30), fill='red')
        for x in range(0, 3):
            time.sleep(0.1)
            canvas.itemconfig(easter_egg_text, fill='blue')
            tk.update()
            time.sleep(0.1)
            canvas.itemconfig(easter_egg_text, fill='yellow')
            tk.update()
            time.sleep(0.1)
            canvas.itemconfig(easter_egg_text, fill='green')
            tk.update()
            time.sleep(0.1)
            canvas.itemconfig(easter_egg_text, fill='pink')
            tk.update()
            time.sleep(0.1)
            canvas.itemconfig(easter_egg_text, fill='orange')
            tk.update()
            time.sleep(0.1)
            canvas.itemconfig(easter_egg_text, fill='red')
            tk.update()
        canvas.itemconfig(easter_egg_text, text='')
        balle.canvas.move(balle.id, 245 - balle.pos[0], 100 - balle.pos[3])
        tk.update()
        time.sleep(0.2)
        canvas.itemconfig(raquette.id, stat='hidden')
        canvas.itemconfig(score_text, font=('Courier', 30))
        canvas.move(score_text, -450, 190)
        canvas.move(score_text, 220, 0)
        egg.dessiner()
        balle.y = -3
        raquette.easter_egg_var = False
        tk.update()
        while 3:
            if balle.score >= 11111111111111111111111111111111100:
                balle.score = "ERREUR"
                for x in range(0, 8):
                    time.sleep(0.2)
                    canvas.itemconfig(score_text, text=('Score: ' + balle.score))
                    tk.update()
                    time.sleep(0.5)
                    canvas.itemconfig(score_text, text='Score: ')
                    tk.update()
                canvas.itemconfig(score_text, text=('Score: ' + balle.score))
                canvas.move (score_text, 200, -190)
                canvas.itemconfig(score_text, font=('Courier', 13))
                balle.canvas.move(balle.id, 245 - balle.pos[0], 100 - balle.pos[3])
                y = 0.1
                t = 1
                tk.update()
                for x in range (0, 10):
                    time.sleep(t - y)
                    egg.canvas.itemconfig(egg.id, stat='hidden')
                    tk.update()
                    time.sleep(t - y)
                    egg.canvas.itemconfig(egg.id, stat='normal')
                    tk.update()
                    ty = t - y
                    t = ty
                egg.canvas.itemconfig(egg.id, stat='hidden')
                balle.canvas.itemconfig(balle.id, stat='hidden')
                canvas.itemconfig(score_text, stat='hidden')
                final_text = canvas.create_text(250, 200, text='YOU FIND THE EASTER EGG', font=('Courier', 20), fill='Yellow')
                tk.update()
                for x in range(0, 5):
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='blue')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='red')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='orange')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='pink')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='green')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='yellow')
                    tk.update()
                canvas.itemconfig(final_text, text='YOU ARE SATAN', fill='red', font=('Courier', 30))
                tk.update()
                time.sleep(2)
                canvas.itemconfig(final_text, text='THANK YOU')
                tk.update()
                time.sleep(2)
                canvas.itemconfig(final_text, text='SIGNED YAPOCK')
                tk.update()
                for x in range(0, 5):
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='blue')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='red')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='orange')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='pink')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='green')
                    tk.update()
                    time.sleep(0.1)
                    canvas.itemconfig(final_text, fill='yellow')
                    tk.update()
                
                canvas.itemconfig(final_text, state='disable', fill ='red')
                tk.update()
            if balle.score == 'ERREUR':
                break
            else:
                balle.dessiner()
                raquette.dessiner()
                canvas.itemconfig(score_text, text=('Score: ' + str(balle.score)))
                tk.update_idletasks()
                tk.update()
                
    canvas.itemconfig(score_text, text=('Score: ' + str(balle.score)))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
#scripted by Yapock
