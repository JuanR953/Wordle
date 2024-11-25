from tkinter import *
from tkinter import messagebox
import random
from collections import Counter

raiz = Tk()
raiz.title("Historic Wordle")
raiz.geometry("400x300")
raiz.configure(bg="#f0f0f0") 

dicc={}

frames=[]

palabrasDisponibles=[
    list("HISTORY"),
    list("GRAINS"),
    list("FISHING"),
    list("PREHISTORY"),
    list("TRADE"),
    list("RIVER"),
    list("SURPLUS"),
    list("WRITING"),
    list("ARCHAEOLOGHY"),
    list("ARTIFACTS"),
    list("FOSSILS"),
    list("STONE"),
    list("PALEOLITHIC"),
    list("MESOLITHIC"),
    list("NEOLITHIC"),
    list("HUNTERS"),
    list("GATHERERS"),
    list("NOMADS"),
    list("SEDENTARIES"),
    list("CAVES"),
    list("FIRE"),
    list("FLINT"),
    list("DOMESTICATE"),
    list("FARMING"),
    list("AGRICULTURE"),
    list("SETTLEMENTS"),
    list("PAINTINGS"),
    list("VILLAGES"),
    list("POTTERY"),
    list("COPPER"),
    list("BRONZE"),
    list("SPECIALIZATION"),
    list("ARTIFACTS"),
    list("MIGRATION"),
    list("ARROWS"),
    list("EVOLUTION"),
    list("IVORY"),
    list("MESOPOTAMIA"),
    list("TRIBE"),
    list("CAVEWOMEN")
]


a=0
ops=6
voy=0

listaHoy=""
palabraHoy=""
lenght=""


# Funciones Globales .......................................................................................................

def jugar():
    global ops, listaHoy, lenght, palabraHoy, voy
    voy=0
    frameInicial.pack_forget()
    framePrincipal.pack(padx="200", pady="25", expand=True, fill="both")
    listaHoy=random.choice(palabrasDisponibles)
    lenght=len(listaHoy)
    palabraHoy="".join(listaHoy)
    ops=6
    labelLenght.config(text=f"The word has {lenght} letters")
    labelIntentos.config(text=f"Remaining attempts: {ops}")

def comprobar():
    global frameNuevo, lenght, ops, frameNuevo, voy
    voy+=1
    palabrasasa = entrada.get()
    palabra=palabrasasa.upper()
    lista=list(palabra)
    print(palabraHoy)
    print(palabra)
    


    if lenght==len(lista):
        pass
    else:
        messagebox.showwarning("Error", f"Your word has to have {lenght} letters.")
        entrada.delete(0, "end")
        return

    ops-=1

    
    
    
    frameNuevo=Frame(framePrincipal)
    frameNuevo.pack()
    frames.append(frameNuevo)

    contador_palabra=Counter(listaHoy)

    for i in range(lenght):

        letra=lista[i]
        if letra == listaHoy[i]:
           color="green"
           contador_palabra[letra]-=1
        elif letra in listaHoy and contador_palabra[letra] > 0:
            color="yellow"
            contador_palabra[letra]-=1
        else:
            color="grey"

        botonEnviar.pack_forget()

        letras = Label(
            frameNuevo, 
            text=letra, 
            font=("Roboto", 20, "bold"), 
            fg="#ffffff",  
            bg=color,  
            relief="flat",  
            highlightbackground="#cccccc",  
            highlightthickness=1,  
            width=2,  
            height=1,  
            justify="center"
        )
        letras.pack(side="left", padx=2, pady=2)

        botonEnviar.pack(pady=5)

    if lista==listaHoy:
        labelIntentos.pack_forget()
        messagebox.showinfo("Congratulations", f"Very Good! You found today's word in {voy} attempts.")
        framePrincipal.pack_forget()
        frameInicial.pack(padx="50", pady="50", expand=True, fill="both")
        for frame in frames:
            frame.destroy()

    labelIntentos.pack_forget()
    labelIntentos.config(text=f"Remaining attemps: {ops}")
    labelIntentos.pack()

    entrada.delete(0, "end")

    if ops == 0:
        messagebox.showwarning("You Lost!", f"You Lost! The word was {palabraHoy}")
        framePrincipal.pack_forget()
        frameInicial.pack(padx=50, pady=50, expand=True, fill="both")

# Ventana .............................................................................................................

frameInicial=Frame(raiz, bg="#ffffff", relief="groove", bd=3)
frameInicial.pack(anchor="center", padx="50", pady="50", expand=True, fill="both")

título=Label(frameInicial, text="HISTORIC WORDLE", font=("Lexend", 75, "bold"), bg="#ffffff", fg="#4a90e2")
título.pack(anchor="center", pady=("30", "0"))

emojis=Label(frameInicial, text="🏛️📜", font=("Lexend", 50), bg="#ffffff", fg="#4a90e2")
emojis.pack(anchor="center", pady=("0", "30"))

#\n

descripcion_texto = (
"The Historical Wordle the classic wordle of every day, but you will have to guess words related to the Stone Age,\n like tools, animals, and daily life. Each word  will test your knowldege on Early Humans and the\n Stone Age. It is a fun game to explore and learn new vocabulary about this period and to practise in class."
) 

descripcion = Label(frameInicial, text=descripcion_texto, font=("Lexend", 16), fg="grey", bg="#ffffff")
descripcion.pack(anchor="center", pady=("0", "30"))


descripcion.pack()

botonJugar=Button(frameInicial, text="Play", command=jugar, font=("Merriweather", 20, "bold"), bg="#4a90e2", fg="white")
botonJugar.pack(anchor="center")


# Juego .............................................................................................................


framePrincipal = Frame(
    raiz, 
    bg="#ffffff", 
    relief="groove",  
    bd=3  
)
#framePrincipal.pack(padx=25, pady=25, expand=True, fill="both")

textoWordle = Label(
    framePrincipal, 
    text="WORDLE", 
    font=("Roboto", 75, "bold"), 
    fg="#4a90e2", 
    bg="#ffffff"
)
textoWordle.pack(padx=15, pady=7)

labelLenght = Label(
    framePrincipal,
    text=f"The word has {lenght} letters.",
    font=("Roboto", 14),
    fg="#555555",  
    bg="#ffffff"
)
labelLenght.pack(padx=0, pady=5)

entrada = Entry(
    framePrincipal,
    font=("Roboto", 14),
    fg="#333333",
    bg="#f4f4f4",
    relief="flat",
    justify="center",
    highlightbackground="#cccccc",  
    highlightthickness=1
)
entrada.pack(padx=0, pady=5)

botonEnviar = Button(
    framePrincipal,
    text="Submit",
    font=("Roboto", 14, "bold"),
    fg="#ffffff",
    bg="#4a90e2",
    activebackground="#357ABD",
    activeforeground="#ffffff",
    relief="flat",  
    overrelief="raised",  
    command=comprobar,
    padx=5
)
botonEnviar.pack(padx=15, pady=7, ipady=8)

labelIntentos = Label(framePrincipal, text=f"Remaining attemps: {ops}", font=("Arial", 14), fg="grey", bg="#ffffff", padx=10, pady=5, borderwidth=0)
labelIntentos.pack()


raiz.mainloop()