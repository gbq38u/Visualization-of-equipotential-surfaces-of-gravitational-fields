from tkinter import *
import random
from tkinter import PhotoImage
from time import *
from math import *
from tkinter import ttk
global b1, plan

okno = Tk()
okno.title('Зачетная работа')
okno.geometry('1920x1080')
holst = Canvas(okno, width=1920, height=1080, bg='white')
holst.pack()

def tl(e):
    holst.delete(ALL)

    holst.create_text(950, 50, text="Зачетная работа на тему ", font="Arial 35")
    holst.create_text(950, 100, text="Построение эквипотенциальных поверхностей гравитационных полей", font="Arial 40")
    holst.create_text(1000, 800, text="Кузина Глеба Андреевича из 10Г класса", font="Arial 30")
    holst.create_text(1000, 850, text="Май 2024 года", font="Arial 30")
    holst.create_text(1000, 900, text="Для перехода в меню нажмите 'Пробел'.", font="Arial 30")
    okno.unbind("<Button-1>")
    okno.unbind("<Escape>")
    okno.unbind('<KeyRelease>')
    okno.unbind("<space>")
    okno.bind("<space>", drawmenu)


def drawmenu(e):
    holst.delete(ALL)
    holst.create_text(960, 50, text="Меню", font="Arial 50")
    holst.create_rectangle(700, 300, 1220, 200)
    holst.create_text(960, 250, text="Условие", font="Arial 60")
    holst.create_rectangle(700, 410, 1220, 310)
    holst.create_text(960, 355, text="Построение", font="Arial 60")
    holst.create_rectangle(700, 520, 1220, 420)
    holst.create_text(960, 460, text="Помощь", font="Arial 60")
    holst.create_text(960, 600, text=" Если вам нужна помощь нажмите на кнопку ' Помощь'.", font="Arial 30")
    holst.create_text(960, 650, text=" Для входа в любое окно меню нажмите на него левой кнопкой мыши.",
                      font="Arial 30")
    holst.create_text(960, 700, text=" Для выхода на титульный лист нажмите на ' Escape'.", font="Arial 30")
    okno.unbind("<Escape>")
    okno.unbind('<KeyRelease>')
    okno.bind("<Escape>", tl)
    okno.bind("<Button-1>", clickmenu)
    okno.unbind("<space>")
    okno.unbind('<Return>')
    okno.unbind("<KeyPress>")
    okno.unbind("<BackSpace>")
def drawmenu1(e):
    holst.delete(ALL)
    b1.place(x=-400, y=-300)
    b2.place(x=-400, y=-300)
    b3.place(x=-400, y=-300)
    b4.place(x=-400, y=-300)
    e2.place(x=-400, y=-300)
    e1.place(x=-400, y=-300)

    holst.create_text(960, 50, text="Меню", font="Arial 50")
    holst.create_rectangle(700, 300, 1220, 200)
    holst.create_text(960, 250, text="Условие", font="Arial 60")
    holst.create_rectangle(700, 410, 1220, 310)
    holst.create_text(960, 355, text="Построение", font="Arial 60")
    holst.create_rectangle(700, 520, 1220, 420)
    holst.create_text(960, 460, text="Помощь", font="Arial 60")
    holst.create_text(960, 600, text=" Если вам нужна помощь нажмите на кнопку ' Помощь'.", font="Arial 30")
    holst.create_text(960, 650, text=" Для входа в любое окно меню нажмите на него левой кнопкой мыши.",
                      font="Arial 30")
    holst.create_text(960, 700, text=" Для выхода на титульный лист нажмите на ' Escape'.", font="Arial 30")
    okno.unbind("<Escape>")
    okno.unbind('<KeyRelease>')
    okno.bind("<Escape>", tl)
    okno.bind("<Button-1>", clickmenu)
    okno.unbind("<space>")
    okno.unbind('<Return>')
    okno.unbind("<KeyPress>")
    okno.unbind("<BackSpace>")







def backkkk(e):
            print("back")
            global nv,opp, akt
            holst.delete(opp)
            del(z[akt])
class zar:
             global nv,opp, akt
             def __init__(self,x,y):
                global rx, ry
                holst.delete(rx)
                holst.delete(ry)
                rx = holst.create_text(130, 275, text=x, font="Arial 25")
                ry = holst.create_text(130, 317, text=y, font="Arial 25")
                self.x=x
                self.y=y
                self.mas = e1.get()
                e1.delete(0,END)
                e1.insert(0,self.mas)
                self.img=holst.create_oval(x-10,y-10,x+10,y+10, fill="grey")
             def __del__(self):
                
                holst.delete(self.img)
                
                print('udalil')
                print(self.mas)
                holst.update()
def LKM(e):
           global nv,opp, akt
           holst.delete(opp)
           global akt
           popal=False
           if not(e.x<350 or e.y<100):
            print('LKM')
            x,y=e.x,e.y#координаты клика
            f=0
            global nv
            for i in range(0, len(z)):
                if 10**2>(x-z[i].x)**2+(y-z[i].y)**2:
                   f=1+i
                   popal=True
                   akt=i
                   print( "выбран", akt)
                   holst.delete(opp)
                   opp = holst.create_oval(z[akt].x-10,z[akt].y-10,z[akt].x+10,z[akt].y+10, fill="grey", outline = 'red')
                   okno.bind('<Return>',fe)
            if f==0 and (350<e.x<860 or 920<e.x  or  (100<e.y<420 and 860<e.x<920) or (480<e.y and 860<e.x<920)):#не попал по старому заряду
                holst.delete(opp)
                z.append(zar(x,y))
            else:#попал
                nv=f-1
                print("popal",nv,len(z))
                e1.delete(0,END)
                global rx, ry
                holst.delete(rx)
                holst.delete(ry)
                rx = holst.create_text(130, 275, text=z[nv].x, font="Arial 25")
                ry = holst.create_text(130, 317, text=z[nv].y, font="Arial 25")
                e1.insert(0,z[nv].mas)
                z[nv].mas = e1.get()
                e1.delete(0,END)
                e1.insert(0,z[nv].mas)
                print ('M=',z[nv].mas)
                okno.unbind("<Button-1>")
                okno.bind("<Motion>",LKMmotion)#подвинуть курсор
                okno.bind("<ButtonRelease-1>",LKMdrop)#отпускаю заряд

def fe(o):
    z[akt].mas = e1.get()
    
            
def LKMmotion(e):
            print('LKMmotion')
            holst.coords(z[nv].img,e.x-10,e.y-10,e.x+10,e.y+10)
            holst.coords(opp,e.x-10,e.y-10,e.x+10,e.y+10)
            
def LKMdrop(e):#как перемещение, толь с добавкой
            if 350<e.x<860 or 920<e.x  or  (100<e.y<420 and 860<e.x<920) or (480<e.y and 860<e.x<920):
                print('LKMdrop')
                global nv
                x,y=e.x,e.y#координаты курсора
                f=0
                for i in range(0, len(z)):
                    if 10**2>(x-z[i].x)**2+(y-z[i].y)**2:
                       f=1+i
                    
                if f==0 and (350<e.x<860 or 920<e.x  or  (100<e.y<420 and 860<e.x<920) or (480<e.y and 860<e.x<920)):#не попал по старому заряду
                    z[nv].x=x
                    z[nv].y=y
                    global rx, ry
                    holst.delete(rx)
                    holst.delete(ry)
                    rx = holst.create_text(130, 275, text=z[nv].x, font="Arial 25")
                    ry = holst.create_text(130, 317, text=z[nv].y, font="Arial 25")
                    z[nv].mas = e1.get()
                    e1.delete(0,END)
                    e1.insert(0,z[nv].mas)
                    print ('M=',z[nv].mas)
                    holst.coords(z[nv].img,x-10,y-10,x+10,y+10)
                    holst.coords(opp,x-10,y-10,x+10,y+10)
                    okno.bind("<Button-1>",LKM)
                    nv=-1
                    #ниже изменения 
                    okno.unbind("<Motion>")#подвинуть курсор
                    okno.unbind("<ButtonRelease-1>")#отпускаю заряд
                else:
                  if 350<e.x<860 or 920<e.x  or  (100<e.y<420 and 860<e.x<920) or (480<e.y and 860<e.x<920):
                    holst.coords(z[nv].img,z[nv].x-10,z[nv].y-10,z[nv].x+10,z[nv].y+10)
                    holst.coords(opp,z[nv].x-10,z[nv].y-10,z[nv].x+10,z[nv].y+10)
                    okno.bind("<Button-1>",LKM)
                    nv=-1
                    okno.unbind("<Motion>")#подвинуть курсор
                    okno.unbind("<ButtonRelease-1>")#отпускаю заряд
def LKMperemeshenie(e):
            print('LKMperemeshenie')
            global nv
            x,y=e.x,e.y#координаты клика
            f=0
            for i in range(0, len(z)):
                if 10**2>(x-z[i].x)**2+(y-z[i].y)**2:
                   f=1+i
            if f==0 and ((350<e.x<860 and 100<e.y<920) or (920<e.x and 100<e.y<920) or  (100<e.y<420 and 860<e.x<920) or (480<e.y and 860<e.x<920)):#не попал по старому заряду
                z[nv].x=x
                z[nv].y=y
                global rx, ry
                holst.delete(rx)
                holst.delete(ry)
                rx = holst.create_text(130, 275, text=z[nv].x, font="Arial 25")
                ry = holst.create_text(130, 317, text=z[nv].y, font="Arial 25")
                z[nv].mas = e1.get()
                e1.delete(0,END)
                e1.insert(0,z[nv].mas)
                print ('M=',z[nv].mas)
                holst.coords(z[nv].img,x-10,y-10,x+10,y+10)
                holst.coords(opp,x-10,y-10,x+10,y+10)
                okno.bind("<Button-1>",LKM)
                nv=-1

def creat():
            okno.unbind("<Button-1>")
            okno.bind("<Button-1>",LKM)
def make():
            md = []
            holst.create_text(155, 550, text="Подождите, идет построение ", font="Arial 20")
            xs =890
            ys=450
            global col, colo
            if col<4:
                col+=1
            else:
                col=0
            colo=['dark red','dark blue','dark green','purple','gold']




            k = 10
            ms = 20
            rs = 100
            vs = float(e2.get())
            с = 0
            d = 0.007

            print(z[0].x)
            print(z[0].y)
            print(z[0].mas)
            
            
            
            for x in range(350,1920):
                for y in range(100,1080):
                    r = sqrt((x-xs)**2+(ys-y)**2)
                    md=[]
                    for j in range(len(z)):
                        ri = sqrt((x-z[j].x)**2+(z[j].y-y)**2)
                        if ri==0:
                          md+=[1]
                        else:
                          md+=[ri]
                    if r==0:
                       r = 1
                    v = k*ms/r
                    for f in range(0,len(z)):
                        v+=k*float(z[f].mas)/float(md[f])
                    if vs-d<=v<=vs+d:

                        holst.create_oval(x+1, y+1, x-1,y-1, fill=colo[col], outline=colo[col])
def back():
        print('no')
        holst.delete(ALL)
        global opp
        opp = holst.create_oval(-100,-100,-101,-101, fill="grey", outline = 'red')
        holst.create_text(960, 50, text="Построение", font="Arial 40")
        global plan,z, rx, r,col
        plan = []
        col = 0
        colo=['dark red','dark blue','dark green','purple','gold']
        holst.create_text(155, 600, text="Для создания планет нажмите", font="Arial 20")
        holst.create_text(155, 625, text="кнопку 'Создать планеты.'      ", font="Arial 20")
        holst.create_text(155, 650, text="Для построения поверхности  ", font="Arial 20")
        holst.create_text(155, 675, text="нажмите кнопку 'Построить     ", font="Arial 20")
        holst.create_text(155, 700, text="поверхность'.                            ", font="Arial 20")
        holst.create_text(155, 725, text="Для удаления планет и          ", font="Arial 20")
        holst.create_text(155, 750, text="построениянажмите 'Удалить'  ", font="Arial 20")
        holst.create_text(155, 775, text="все'.                                           ", font="Arial 20")
        holst.create_text(155, 800, text="Для 'красивого' построения     ", font="Arial 20")
        holst.create_text(155, 825, text="нажмите 'Автозаполнение'       ", font="Arial 20")

        




        for o in range(0, 45):
           holst.create_line(350+o*40,100, 350+o*40, 1080, width=1, fill = 'lavender')
           #Сетка
        for p in range(0, 25):
           holst.create_line(350, 100+p*40, 1920, 100+p*40, width=1, fill = 'lavender')
        pom = holst.create_text(83, 160, text="Введите M < 20", font="Arial 15")
        holst.create_text(83, 235, text="Введите U < 3", font="Arial 15")

        

        
        global im, creat, make, back
        im = PhotoImage(file='5bbc1b403a8dc.gif') #солнце
        holst.create_image(890, 450, image=im)


        z=[]#массив зарядов


        nv=-1#номер того заряда, в который кликнули и "выделили" для работы
        def zachita(e):
                print("йа нажолось",e)
                
                def antidurak(m,p,o):
                        q=m.get()
                        r=""
                        for i in range(0,len(q)):
                            if (q[i].isdigit() or q[i]=="." and r.count(".")==0) and len(r)<4:
                                r+=q[i]
                        p.delete(0,END)
                        p.insert(0,r)
                antidurak(m,e1,e2)

        holst.create_text(55, 200, text="U = ", font="Arial 30")
        
        holst.create_text(55, 125, text="M = ", font="Arial 30")
        if (not str(e1.get()).isdigit()) and len(str(e1.get()))<5:
            e1.delete(0,END)





        global  rx, ry
        holst.create_text(55, 275, text="X = ", font="Arial 30")
        holst.create_rectangle(90, 253, 340, 295, fill = 'Light grey')
        rx = holst.create_text(130, 275, text=" ", font="Arial 25")
        




        holst.create_text(55, 325, text="Y = ", font="Arial 30")
        holst.create_rectangle(90, 300, 340, 342, fill = 'Light grey')
        ry = holst.create_text(130, 317, text=" ", font="Arial 25")



        okno.bind("<Escape>", drawmenu1)
        okno.bind("<KeyPress>",zachita)
        okno.unbind("<Button-1>")
        okno.unbind('<KeyRelease>')
        okno.unbind("<space>")
        okno.bind("<space>", backkkk)


def auto():
            if z ==[]:


                z.append(zar(400,450))
                z[0].img = holst.create_oval(390,440,410,460, fill="grey")
                z.append(zar(450,450))
                z[1].img = holst.create_oval(440,440,460,460, fill="grey")
                z.append(zar(500,450))
                z[2].img = holst.create_oval(490,440,510,460, fill="grey")
                z.append(zar(550,450))
                z[3].img = holst.create_oval(540,440,560,460, fill="grey")
                z.append(zar(600,450))
                z[4].img = holst.create_oval(590,440,610,460, fill="grey")
                z.append(zar(650,450))
                z[5].img = holst.create_oval(640,440,660,460, fill="grey")
                z.append(zar(700,450))
                z[6].img = holst.create_oval(690,440,710,460, fill="grey")
                z.append(zar(750,450))
                z[7].img = holst.create_oval(740,440,760,460, fill="grey")
                z[7].mas =0.3
                z[6].mas =0.6
                z[5].mas =1
                z[4].mas =0.9
                z[3].mas =2.4
                z[2].mas =2.2
                z[1].mas =2.4
                z[0].mas =1.8


                

                k = 10
                md = []
                xs =890
                ys=450
                ms = 8
                rs = 100
                vs = 1
                с = 0
                d = 0.007
                
                for x in range(350,1920):
                    for y in range(100,1080):
                        r = sqrt((x-xs)**2+(ys-y)**2)
                        md=[]
                        for j in range(len(z)):
                            ri = sqrt((x-z[j].x)**2+(z[j].y-y)**2)
                            if ri==0:
                              md+=[1]
                            else:
                              md+=[ri]
                        if r==0:
                           r = 1
                        v = k*ms/r
                        for f in range(0,len(z)):
                            v+=k*float(z[f].mas)/float(md[f])
                        if vs-d<=v<=vs+d:

                            holst.create_oval(x+1, y+1, x-1,y-1, fill='red', outline='red')
            

def clickmenu(e):

    if 700 < e.x < 1220 and 200 < e.y < 300:
        # попал в 1 пункт меню
        holst.delete(ALL)
        holst.create_text(960, 50, text="Условие", font="Arial 40")
        holst.create_text(660, 100, text="Составить программу, моделирующую потроение эквипотенциальных поверхностей          ",
                          font="Arial 30")
        holst.create_text(660, 150,
                          text="гравитационного поля. Гравитационное поле создается неподвижными телами. В центре ",
                          font="Arial 30")
        holst.create_text(660, 200, text="экрана звезда, на ее орбитах планеты до 10шт. Сделать заготовки с реальными                ",
                          font="Arial 30")   
        holst.create_text(660, 250, text="массами солнечной системы. Наличие объектов, орбиты, массы настраиваются.                       ", font="Areal 30")



        okno.unbind("<Escape>")
        okno.unbind("<Button-1>")
        okno.bind("<Escape>", drawmenu)
        okno.unbind('<KeyRelease>')

    if 700 < e.x < 1220 and 310 < e.y < 410:
        holst.delete(ALL)
        global opp
        opp = holst.create_oval(-100,-100,-101,-101, fill="grey", outline = 'red')
        holst.create_text(960, 50, text="Построение", font="Arial 40")
        global plan,z, rx, r,col
        plan = []
        col = 0
        colo=['dark red','dark blue','dark green','purple','gold']
        holst.create_text(155, 600, text="Для создания планет нажмите", font="Arial 20")
        holst.create_text(155, 625, text="кнопку 'Создать планеты.'      ", font="Arial 20")
        holst.create_text(155, 650, text="Для построения поверхности  ", font="Arial 20")
        holst.create_text(155, 675, text="нажмите кнопку 'Построить     ", font="Arial 20")
        holst.create_text(155, 700, text="поверхность'.                            ", font="Arial 20")
        holst.create_text(155, 725, text="Для удаления планет и          ", font="Arial 20")
        holst.create_text(155, 750, text="построениянажмите 'Удалить'  ", font="Arial 20")
        holst.create_text(155, 775, text="все'.                                           ", font="Arial 20")
        holst.create_text(155, 800, text="Для 'красивого' построения     ", font="Arial 20")
        holst.create_text(155, 825, text="нажмите 'Автозаполнение'       ", font="Arial 20")

        




        for o in range(0, 45):
           holst.create_line(350+o*40,100, 350+o*40, 1080, width=1, fill = 'lavender')
           #Сетка
        for p in range(0, 25):
           holst.create_line(350, 100+p*40, 1920, 100+p*40, width=1, fill = 'lavender')
        pom = holst.create_text(83, 160, text="Введите M < 20", font="Arial 15")
        holst.create_text(83, 235, text="Введите U < 3", font="Arial 15")

        

        
        global im, creat, make, back
        im = PhotoImage(file='5bbc1b403a8dc.gif') #солнце
        holst.create_image(890, 450, image=im)


        z=[]#массив зарядов


        nv=-1#номер того заряда, в который кликнули и "выделили" для работы
        def zachita(e):
                print("йа нажолось",e)
                
                def antidurak(m,p):
                        q=m.get()
                    
                        
                        r=""
                        for i in range(0,len(q)):
                            if (q[i].isdigit() or q[i]=="." and r.count(".")==0) and len(r)<4:
                                r+=q[i]
                        p.delete(0,END)
                        p.insert(0,r)
                antidurak(m,e1)
 

            
        global b1,b2,b3,b4, e1,e2
        b1 = Button(text = 'Создать планеты', command = creat, font = 'Arial 20' , width = 19)
        b1.pack()
        b1.place(x=25, y=350)

        b2 = Button(text = 'Постороить поверхность', command = make, font = 'Arial 20', width = 19)
        b2.pack()
        b2.place(x=25, y=400)
        

        b3 = Button(text = 'Удалить все', command = back, font = 'Arial 20', width = 19)
        b3.pack()
        b3.place(x=25, y=450)


        b4 = Button(text = 'Автозаполнение', command = auto, font = 'Arial 20', width = 19)
        b4.pack()
        b4.place(x=25, y=500)


        m = StringVar()
        e1 = Entry(width = 10, textvariable = m, font = 'Arial 30')
        e1.pack()
        e1.place(x=90,y= 100)

        holst.create_text(55, 125, text="M = ", font="Arial 30")
        m1 = StringVar()
        e2 = Entry(width = 10, textvariable = m1, font = 'Arial 30')
        e2.pack()
        e2.place(x=90,y= 175)

        holst.create_text(55, 200, text="U = ", font="Arial 30")
        if (not str(e1.get()).isdigit()) and len(str(e1.get()))<5:
            e1.delete(0,END)





        global  rx, ry
        holst.create_text(55, 275, text="X = ", font="Arial 30")
        holst.create_rectangle(90, 253, 340, 295, fill = 'Light grey')
        rx = holst.create_text(130, 275, text=" ", font="Arial 25")
        




        holst.create_text(55, 325, text="Y = ", font="Arial 30")
        holst.create_rectangle(90, 300, 340, 342, fill = 'Light grey')
        ry = holst.create_text(130, 317, text=" ", font="Arial 25")



        okno.bind("<Escape>", drawmenu1)
        okno.bind("<KeyPress>",zachita)
        okno.unbind("<Button-1>")
        okno.unbind('<KeyRelease>')
        okno.unbind("<space>")
        okno.bind("<space>", backkkk)
    if 700 < e.x < 1220 and 420 < e.y < 520:
        # попал в 3 пункт меню
        holst.delete(ALL)
        
        holst.create_text(960, 50, text="Помощь", font="Arial 40")
        holst.create_text(660, 100, text="Это страница помощи, здесь объясняется как пользоваться этой программой.            ",
                          font="Arial 30")
        holst.create_text(660, 150,
                          text="Для того чтобы выйти из любого пункта меню нажмите Escape, для того чтобы войти",
                          font="Arial 30")
        holst.create_text(660, 200, text=" в любое окно меню или запустить демонстрацию кликните правой клавишей мыши    ",
                          font="Arial 30")
        holst.create_text(660, 250, text="по надписи. Для ввода цифр введите цифры с клавиатуры.                                                            ", font="Areal 30")
        okno.unbind("<Button-1>")
        okno.bind("<Escape>", drawmenu)
        okno.unbind('<KeyRelease>')
        okno.unbind("<space>")








tl(1)

okno.mainloop()






