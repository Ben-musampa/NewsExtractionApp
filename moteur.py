#author : Ben Musampa
# i use tkinter and GoogleNews library to built this application
from cgitb import text
from turtle import width
from fpdf import FPDF
from tkinter import *
from GoogleNews import GoogleNews
import pandas as pd
from tkinter.filedialog import *
from threading import *
from tkinter import messagebox
from tkinter import ttk

# initialisation de fpdf
doc = FPDF()
doc.add_page()
doc.set_font("Arial", size=6)
#---------------------------------------------------- moteur de recherche -----

def recherche():
    
    actu = GoogleNews(period=period.get(), lang=lang.get())
    actu.search(sujet.get())
    resultat = actu.result()
    info = pd.DataFrame.from_dict(resultat)
    info = info.drop(columns = ["img"])
    info.head()

    for i in resultat:
        Titre=("Titre: "+i["title"])
        infos=("information :"+i["desc"])
        lien =("Lien :"+i["link"])

    #extraction des informations

    doc.cell(200, 10, txt=Titre, ln=1, align='C')
    doc.cell(200, 10, txt=infos, ln=2, align='C')
    doc.cell(200, 10, txt=lien, ln=3, align='C')

    # impression du fichier pdf avec nom de l'article
    doc.output(""+sujet.get()+".pdf")
    messagebox.showinfo("showinfo", "fichier enregistrer avec titre "+sujet.get()+"pdf")

def rafraichir():
    if sujet.get()=="":
        messagebox.showerror("showerror", "Aucune valeur inserer")
    else:
        sujet.set("")


#---------------------------------------------- programme ----------

cn = Tk()
cn.iconbitmap("search.ico")
cn.title("Congonews")
cn.minsize(900,600)
cn.maxsize(1000,800)

period = StringVar(cn)
period.set('1h')
lang = StringVar(cn)
lang.set('fr')

cnlogo = PhotoImage(file = "logo.png")
cnlogo2 = Label(image = cnlogo)
cnlogo2.place(x=235,y=20)

nom = Label(cn, text="Congonews", fg="black", font=("Montserrat",32))
nom.place(x=375,y=55)
#choix du sujet de l'information
sujet = Entry(cn, width=50, font=("Montserrat",15) ,borderwidth=2)
sujet.place(x=200,y=240)
Entrer_sujet = Label(cn, text="sujet ",fg="black", font=("Montserrat",15))
Entrer_sujet.place(x=90,y=240)
#choix de la periode de l'information
periode = OptionMenu(cn, period, '1h','10h', '1d','1w', '1m')
periode.pack()
periode.place(x=200, y=300)
Entrer_periode = Label(cn, text="Periode", fg="black", font=("Montserrat",15))
Entrer_periode.place(x=90, y=300)
#Choix de la langue de l'information
langue= OptionMenu(cn, lang, 'fr', 'en')
langue.pack()
langue.place(x=350, y=300)
Entrer_langue = Label(cn, text="langue", fg="black", font=("Montserrat",15))
Entrer_langue.place(x=280, y=300)
#Bouton de recherche
recherche_button = Button(cn,width=12 ,height=1 , text="recherche", font=("Montserrat",14) ,relief="groove", bg="green", fg="white", borderwidth=1, command=recherche)
recherche_button.place(x=360,y=350)

rafraichir_button = Button(cn, width=12 ,height=1 , text="rafraichir", font=("Montserrat",14) ,relief="groove", bg="red", fg="white", borderwidth=1, command=rafraichir)
rafraichir_button.place(x=360,y=400)

cn.mainloop()
