import PySimpleGUI as sg
from numpy.random import choice
from numpy import random
def start():
    for i in range(31):
        simulation()
        #30 gün simülasyonu çalıştırıyor for döngüsü üstteki

#random gün simülasyonu fonksiyonu ve kişiye göre tamamen random olasılık
def simulation():
    for i in people:
        f = []
        p = random.rand()
        n = float(1-p)
        f.append(p)
        f.append(n)
        c = choice(sit, p=f)
        penalty(c,i)
        

#ceza puanlarının eklenmesi fonksiyonu
def penalty(name,person):
    pen = people[person]
    if name == "çöpe atıyor":
        punishment = 0
    elif name == "yere atıyor":
        punishment = 1
    pen +=punishment
    people[person] = pen


#ceza puanlarının yazdırılması fonksiyonu
def write(dicti):
    sort_dict = dict(sorted(dicti.items(), key=lambda item: item[1],reverse=True))
    for i in sort_dict:
        print("{name}'s penalty is {pen}".format(name=i,pen=sort_dict[i]))
#top 10 ceza
def write_10(dicti):
    sort_dict = dict(sorted(dicti.items(), key=lambda item: item[1],reverse=True))
    counter = 0
    for i in sort_dict:
        if counter ==10:
            break
        else:
            print("{name}'s penalty is {pen}".format(name=i,pen=sort_dict[i]))
            counter +=1


sit = ['çöpe atıyor','yere atıyor']

people = {'Emre':int(0),'Jack':int(0),'Azra':int(0),'Derrick':int(0),'Tarık':int(0),'Sıla':int(0),'Melisa':int(0),'Dilara':int(0),'Onur':int(0),'Çakır':int(0),'Büşra':int(0),'Duygu':int(0),'Selin':int(0),'Hasan':int(0),'Sultan':int(0),'Alperen':int(0),'Gamze':int(0),'Selim':int(0),'Özge':int(0),'Mustafa':int(0),'Ahmet': int(0),'Adem': int(0),'Süleyman': int(0),'Mehmet': int(0),'Alp': int(0),'Serdar': int(0),'Mert':int(0),'Burcu':int(0),'Elif':int(0),'Münevver':int(0)}
#first page after image
def make_window1():
    layout = [[sg.Text('This simulation program has the goal to detect smokers who do not throw their butts in trashboxes and prepare a score list based on repetetive actions.',justification="center",size=(40,5),font=12)],
              [sg.Button('Start')]]

    return sg.Window('Cigarette butt detection simulation', layout, finalize=True)
#second page 
def make_window3():
    
    layout = [[sg.Text('Monthly Penalty Scores(If you want to see a one more month you can use "Repeat" button.)',key = "pen")],
              [sg.Output(size=(60,10),key="output")],
               [sg.Button("Print"),sg.Button("Repeat"),sg.Button("Embarrasment List"),sg.Button('Exit')]]

    return sg.Window('Cigarette butt detection simulation', layout, finalize=True)
#emberassment list page
def make_window4():
    layout = [[sg.Text('Embarrassment List',key="Text")],
              [sg.Output(size=(60,10),key="top_10")],
              [sg.Button('Print'),sg.Button("Exit")]]
    return sg.Window('cigarette butt detection simulation', layout, finalize=True)
#opening page
sg.popup_no_buttons(auto_close_duration=3,auto_close=True,image="1.png")     
window1, window3, window4 = make_window1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event==sg.WIN_CLOSED:
        window1.close()
        break

    if window == window1:
        if event == 'Start':
            start()
            window1.hide()
            sg.popup_no_buttons("Simulation the program.....",auto_close_duration=1,auto_close=True)     
            window3=make_window3()

    if window == window3:
        window3.FindElement("output").Update("")
        if event == "Print":
            write(people)
        if event =="Repeat":
            window3.disappear()
            sg.popup_no_buttons("Repating the process.....",auto_close_duration=1,auto_close=True)     
            start()
            window3.reappear()
            write(people)
        if event == "Embarrasment List":
            window3.hide()
            window4 = make_window4()
        if event in (sg.WIN_CLOSED,"Exit"):
            window3.close()
            window1.close()
            break
    if window == window4:
        window4.FindElement("top_10").Update("")
        if event=="Exit":
            window4.close()
            window3.close()
            window1.close()
            sg.popup_no_buttons("""MAK 230E – CRN 12510
Serdar Güzlü
guzlu16@itu.edu.tr
Yunus Emre Sezen
sezeny17@itu.edu.tr
Emre Kasım
kasim18@itu.edu.tr
Mustafa Alperen Kılıç
kilicmu19@itu.edu.tr""",auto_close_duration=3,auto_close=True)
            break
        if event == "Print":
            write_10(people)

window.close()
