from tkinter import *
import time


Fenetre=Tk()

zone_dessin=Canvas(Fenetre,width=750,height=500,bd=8)
zone_dessin.pack(padx=10,pady=10)

img=PhotoImage(file="bg.png")
zone_dessin.create_image(-500,-500, anchor=NW,image=img)
zone_dessin.place(x=0,y=0)


zone_dessin.pack()


img1=PhotoImage(file='perso1_1.png')
img1=img1.zoom(3)
perso1=zone_dessin.create_image(100,360,image=img1)
img2=PhotoImage(file='perso2_1.png')
img2=img2.zoom(3)
perso2=zone_dessin.create_image(650,375,image=img2)
img3=PhotoImage(file='perso1attaque_1.png')
img3=img3.zoom(3)
img4=PhotoImage(file='perso2attaque_1.png')
img4=img4.zoom(3)
img5=PhotoImage(file='perso1attente_1.png')
img5=img5.zoom(3)
img6=PhotoImage(file='perso2attente_1.png')
img6=img6.zoom(3)
img7=PhotoImage(file='perso1saut_1.png')
img7=img7.zoom(3)
img8=PhotoImage(file='perso2saut_1.png')
img8=img8.zoom(3)
img9=PhotoImage(file='win2.png')
img10=PhotoImage(file='win.png')
img11=PhotoImage(file='acceuilvfredim.png')
img12=PhotoImage(file='controltouche.png')
"""img13=PhotoImage(file='choix_perso1')
img14=PhotoImage(file='choix_perso2')
img15=PhotoImage(file='perso_3.png')
img16=PhotoImage(file='perso_4.png')"""


nbvie1=3
nbvie2=3
vie1=zone_dessin.create_rectangle(100,40,100+10*nbvie1,50,fill="red")
vie2=zone_dessin.create_rectangle(650,40,650-10*nbvie2,50,fill="red")
compteur1=0
compteur2=0

commande=zone_dessin.create_image(380,270,image=img12)
first=zone_dessin.create_image(380,270,image=img11)
"""choix_perso1=zone_dessin.create_image(380,270,image=img13)
choix_perso2=zone_dessin.create_image(380,270,image=img14)"""

def debut(event):
  zone_dessin.delete(first)
  zone_dessin.update()
zone_dessin.bind_all('<space>',debut)

def touche(event):
  zone_dessin.delete(commande)
  zone_dessin.update()
zone_dessin.bind_all('<Escape>',touche)

"""def choix1(event):
    if zone_dessin.bind_all('<&>',choix1):
        perso1=zone_dessin.create_image(100,360,image=img15)
    zone_dessin.delete(choix_perso1)
    zone_dessin.update()
zone_dessin.bind_all('<é>')

def choix2(event):
    if zone_dessin.bind_all('<(>',choix2):
        perso2=zone_dessin.create_image(650,375,image=img16)
    zone_dessin.delete(choix_perso2)
    zone_dessin.update()
zone_dessin.bind_all('<->')"""



def droite1(event):
  x=30
  y=0
  if zone_dessin.coords(perso1)[0]>795:
    x=0
  zone_dessin.move(perso1,x,y)
zone_dessin.bind_all('<d>', droite1)

def gauche1(event):
  x=-30
  y=0
  if zone_dessin.coords(perso1)[0]<190:
    x=0
  zone_dessin.move(perso1,x,y)
zone_dessin.bind_all('<q>', gauche1)

def droite2(event):
  x=30
  y=0
  if zone_dessin.coords(perso2)[0]>699:
    x=0
  zone_dessin.move(perso2,x,y)
zone_dessin.bind_all('<Right>', droite2)

def gauche2(event):
    x=-30
    y=0
    if zone_dessin.coords(perso2)[0]<100:
        x=0
    zone_dessin.move(perso2,x,y)
zone_dessin.bind_all('<Left>', gauche2)


liste=[-10,-20,-20,-20,-20,-20,-20,-20,-10,10,20,20,20,20,20,20,20,10]

def saut1(event):
  global perso1
  x=zone_dessin.coords(perso1)[0]
  y=zone_dessin.coords(perso1)[1]
  zone_dessin.delete(perso1)
  zone_dessin.update()
  x=x-6
  y=y+15
  perso1=zone_dessin.create_image(x,y,image=img7)
  zone_dessin.update()

  if zone_dessin.coords(perso1)[1]<100:
        y=0

  for i in range (len(liste)):
    zone_dessin.move(perso1,0,liste[i])
    time.sleep(0.05)
    zone_dessin.update()
  zone_dessin.delete(perso1)
  zone_dessin.update()
  x=x+6
  y=y-15
  perso1=zone_dessin.create_image(x,y,image=img1)
zone_dessin.bind_all('<z>',saut1)

def saut2(event):
  global perso2
  x=zone_dessin.coords(perso2)[0]
  y=zone_dessin.coords(perso2)[1]
  zone_dessin.delete(perso2)
  zone_dessin.update()
  x=x+5
  y=y-36
  perso2=zone_dessin.create_image(x,y,image=img8)
  zone_dessin.update()
  for i in range (len(liste)):
    zone_dessin.move(perso2,0,liste[i])
    time.sleep(0.05)
    zone_dessin.update()
  zone_dessin.delete(perso2)
  zone_dessin.update()
  x=x-5
  y=y+36
  perso2=zone_dessin.create_image(x,y,image=img2)
zone_dessin.bind_all('<Up>',saut2)

def invisible1(event):
    global perso1
    x=zone_dessin.coords(perso1)[0]
    y=zone_dessin.coords(perso1)[1]
    zone_dessin.delete(perso1)
    zone_dessin.update()
    time.sleep(0.5)
    x+=150
    perso1=zone_dessin.create_image(x,y,image=img1)
zone_dessin.bind_all('<y>',invisible1)

def invisible2(event):
    global perso2
    x=zone_dessin.coords(perso2)[0]
    y=zone_dessin.coords(perso2)[1]
    zone_dessin.delete(perso2)
    zone_dessin.update()
    #print('ok')
    time.sleep(0.5)
    x-=150
    perso2=zone_dessin.create_image(x,y,image=img2)
zone_dessin.bind_all('<l>',invisible2)


def poing1(event):
  global perso1,perso2,vie2,nbvie2,vie1,compteur1,compteur2
  x=zone_dessin.coords(perso1)[0]
  y=zone_dessin.coords(perso1)[1]
  zone_dessin.delete(perso1)
  zone_dessin.update()
  perso1=zone_dessin.create_image(x+80,y+2,image=img5)
  zone_dessin.update()
  time.sleep(0.1)
  zone_dessin.delete(perso1)
  perso1=zone_dessin.create_image(x+98,y-37,image=img3)
  x1=zone_dessin.coords(perso1)[0]
  y1=zone_dessin.coords(perso1)[1]
  x1=x1+20
  y1=y1-10
  x2=zone_dessin.coords(perso2)[0]
  y2=zone_dessin.coords(perso2)[1]
  y2=y2-80
  x2=x2-20
  if x1+15>=x2 and x1<=x2+50 and y1+30>=y2 and y1<=y2+80:
    nbvie2=nbvie2-1
    zone_dessin.delete(vie2)
    zone_dessin.update()
    if nbvie2!=0:
      vie2=zone_dessin.create_rectangle(650,40,650-10*nbvie2,50,fill="red")
    zone_dessin.update()
  zone_dessin.update()
  time.sleep(1)
  zone_dessin.delete(perso1)
  perso1=zone_dessin.create_image(x+80,y+2,image=img5)
  zone_dessin.update()
  time.sleep(0.1)
  zone_dessin.delete(perso1)
  perso1=zone_dessin.create_image(x,y,image=img1)
  zone_dessin.update()
  if nbvie2==0:
    compteur1=compteur1+1
    fin=zone_dessin.create_rectangle(0,0,800,800,fill='black')
    zone_dessin.update()
    time.sleep(2)
    if compteur1==3:
      score=zone_dessin.create_image(350,250,image=img10)
      zone_dessin.update()
      time.sleep(6)
      Fenetre.destroy()
    else:
      zone_dessin.delete(fin)
      zone_dessin.delete(perso1)
      zone_dessin.delete(perso2)
      zone_dessin.delete(vie1)
      zone_dessin.delete(vie2)
      zone_dessin.update()
      perso1=zone_dessin.create_image(100,360,image=img1)
      perso2=zone_dessin.create_image(650,375,image=img2)
      nbvie1=3
      nbvie2=3
      vie1=zone_dessin.create_rectangle(100,40,100+10*nbvie1,50,fill="red")
      vie2=zone_dessin.create_rectangle(650,40,650-10*nbvie2,50,fill="red")
      zone_dessin.update()
zone_dessin.bind_all('<t>',poing1)

def poing2(event):
  global perso1,perso2,vie2,nbvie1,vie1,compteur2,compteur1
  x=zone_dessin.coords(perso2)[0]
  y=zone_dessin.coords(perso2)[1]
  zone_dessin.delete(perso2)
  zone_dessin.update()
  perso2=zone_dessin.create_image(x-24,y-6,image=img6)
  zone_dessin.update()
  time.sleep(0.1)
  zone_dessin.delete(perso2)
  perso2=zone_dessin.create_image(x-63,y-21,image=img4)
  x1=zone_dessin.coords(perso2)[0]
  y1=zone_dessin.coords(perso2)[1]
  x1=x1-95
  y1=y1-40
  x2=zone_dessin.coords(perso1)[0]
  y2=zone_dessin.coords(perso2)[1]
  y2=y2-55
  x2=x2-50
  if x1+15>=x2 and x1<=x2+50 and y1+30>=y2 and y1<=y2+80:
    nbvie1=nbvie1-1
    zone_dessin.delete(vie1)
    zone_dessin.update()
    if nbvie1!=0:
      vie1=zone_dessin.create_rectangle(100,40,100+10*nbvie1,50,fill="red")
    zone_dessin.update()
  zone_dessin.update()
  time.sleep(1)
  zone_dessin.delete(perso2)
  perso2=zone_dessin.create_image(x-24,y-6,image=img6)
  zone_dessin.update()
  time.sleep(0.1)
  zone_dessin.delete(perso2)
  perso2=zone_dessin.create_image(x,y,image=img2)
  zone_dessin.update()
  if nbvie1==0:
    compteur2=compteur2+1
    fin=zone_dessin.create_rectangle(0,0,800,800,fill='black')
    zone_dessin.update()
    time.sleep(2)
    if compteur2==3:
      score=zone_dessin.create_image(350,250,image=img9)
      zone_dessin.update()
      time.sleep(6)
      Fenetre.destroy()
    else:
      zone_dessin.delete(fin)
      zone_dessin.delete(perso1)
      zone_dessin.delete(perso2)
      zone_dessin.delete(vie1)
      zone_dessin.delete(vie2)
      zone_dessin.update()
      perso1=zone_dessin.create_image(100,360,image=img1)
      perso2=zone_dessin.create_image(650,375,image=img2)
      nbvie1=3
      nbvie2=3
      vie1=zone_dessin.create_rectangle(100,40,100+10*nbvie1,50,fill="red")
      vie2=zone_dessin.create_rectangle(650,40,650-10*nbvie2,50,fill="red")
      zone_dessin.update()
zone_dessin.bind_all('<m>',poing2)


Fenetre.mainloop()