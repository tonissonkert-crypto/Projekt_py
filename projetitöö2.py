import tkinter as tk
root = tk.Tk()
root.title("Mäng")
root.geometry("900x400")
võti = False
surmad = 0
 
 ### labürint ###
def labürint():
    page3.pack_forget()
    page4.pack()

def liigu_otse():
    labürint_label.config(text="seal ei olnud midagi")

def liigu_vasakule():
    page4.pack_forget()
    page5.pack()

def labürint_lõks():
    labürint_label2.config(text="Bozo, üle said")
    labürint_button.config(state=tk.DISABLED)
    nupp_tagasiLabürinti = tk.Button(page5, text="Tagasi labürinti", command=lambda: [page5.pack_forget(), page4.pack()])
    nupp_tagasiLabürinti.pack()
    labürint_label.config(text="ÄRA ENAM SINNA MINE!!!")

def liigu_paremale():
    global võit
    global surmad

    if võti:
        page4.pack_forget()
        page6.pack()
    else:
        labürint_label.config(text="HALLO, kus võti on, proovi surra")

def liigu_tagasi():
    page4.pack_forget()
    page3.pack()
    label2.config(text="MIKS SA TAGASI TULID?")

def voidetud():
    root.destroy()
    
### labürint läbi ###


def siin_sured():
    global võti
    global surmad

    surmad += 1
    if surmad >= 2:
        võti = True
        revi.config(text="tubli oled, said võtme", font=("Arial", 20))
    else:
        revi.config(text="MIKS SA VAJUTASID SEDA!!!")

    page1.pack_forget()
    page2.pack()
    
def algus():
    page2.pack_forget()
    page1.pack()

def monstrum():
    page1.pack_forget()
    page3.pack()

def tagasi_algusesse():
    page3.pack_forget()
    page1.pack()

def monster_sai_molli():
    label2.config(text="Tubli oled!")
    button2.config(text="Mine labürinti", command= labürint)
    monsterL.config(text="Laipa imetlema!")
    img2 = tk.PhotoImage(file="monster.pekstud.png")
    image_label.config(image=img2)
    image_label.image = img2  # Keep reference
    monster_sai_molli.pack()   
    
#### siin sured ####
page1 = tk.Frame(root)
sured=tk.Label(page1, text="saad surma kui vajutad")
surm = tk.Button(page1, text="Nupp", command= siin_sured)
sured.pack()
surm.pack()
page1.pack()

### monstriga ruumi minemine ###
monsterB = tk.Button(page1, text="Nupp", command= monstrum)
monsterL= tk.Label(page1, text="Vajuta siia, et teisse ruumi saada")
monsterL.pack()
monsterB.pack()

### monster ###
page3 = tk.Frame(root)
img1 = tk.PhotoImage(file="monster.png")
image_label = tk.Label(page3, image=img1)
image_label.image = img1
image_label.pack()

### monstri tapmine ###
button2=tk.Button(page3, text="Anna molli", command=monster_sai_molli)
label2=tk.Label(page3, text="Vajuta siia, et monstrile vastu molli anda")
label2.pack()
button2.pack()

### siit saame tagasi peale monstrit ###
monster_sai_molli = tk.Button(page3, text="Tagasi algusesse", command=tagasi_algusesse)



### miks sa vajutasid seda ###
page2 = tk.Frame(root)
revi=tk.Label(page2, text ="MIKS SA VAJUTASID SEDA!!!")
revive = tk.Button(page2, text="revive yourself", command= algus)
revi.pack()
revive.pack()


##################### labürint #######################
page4 = tk.Frame(root)
labürint_label = tk.Label(page4, text="Sa jõudsid labürinti")
labürint_label.grid(row=0, column=0, columnspan=3, pady=10) 

nupp_otse = tk.Button(page4, text="Liigu otse", command=liigu_otse)
nupp_vasakule = tk.Button(page4, text="Liigu vasakule", command=liigu_vasakule)
nupp_paremale = tk.Button(page4, text="Liigu paremale", command=liigu_paremale)
nupp_tagasi = tk.Button(page4, text="Liigu tagasi", command=liigu_tagasi)
# nuppude layout

nupp_otse.grid(row=1, column=1, pady=10)      # üleval
nupp_tagasi.grid(row=3, column=1, pady=10)    # all
nupp_vasakule.grid(row=2, column=0, padx=10)  # vasakul
nupp_paremale.grid(row=2, column=2, padx=10)  # paremal  

### siin said üle ###
page5 = tk.Frame(root)
labürint_label2 = tk.Label(page5, text="vajuta siia, et saada auhind")
labürint_label2.pack()
labürint_button = tk.Button(page5, text="🏆", command=labürint_lõks)
labürint_button.pack()

### siin võidad ###
page6 = tk.Frame(root)
võiduruum_label = tk.Label(page6, text="SA VÕITSID!!! Võta oma auhind")
võiduruum_label.pack()
võit_nupp = tk.Button(page6, text="🏆🏆🏆",font=("Arial", 20), command=voidetud)
võit_nupp.pack()


root.mainloop()