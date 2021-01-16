from tkinter import*
from tkinter.messagebox import showerror # pour le message d'erreur si y a r d'ecrit
from Enigma import* #import enigma et ses fonctions dans tkinter
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Rotor_1 = ['A', 'Q', 'W', 'Z', 'S', 'X', 'E', 'D', 'C', 'R', 'F', 'V', 'T', 'G', 'B', 'Y', 'H', 'N', 'U', 'J', 'I', 'K', 'O', 'L', 'P', 'M']

Rotor_2 = ['P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'Z', 'A', 'M', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'Q', 'N', 'B', 'V', 'C', 'X', 'W']

#-----Fonctions-----#

#ROTORS QUI BOUGENT PAS

def Code(): #le mot qu on va ecrire qui doit etre codé / Rotor mouvement
    Mot_a_coder = message.get(1.0,'end').upper()
    if Mot_a_coder == '\n': #cherche si il y a quleque chose d'ecrit 
        showerror('ERROR', 'Veuillez entrer le message codé') #t as rien ecrit ehoh
        return ''
    mot_code = code(Rotor_1,Rotor_2,Mot_a_coder) #j' utilise ce que j avais dans enigma_code arguments
    #nous devons faire une remise a 0 juste arrivant d'ecrire et on ecris a ce moment la sinon on ecrit plein de fois le codage d'affiler
    Mot_code.delete(1.0,2.0)
    Mot_code.insert (1.0, mot_code)
    #cela ne marche que pour le codage je dois faire de même pour E_code

#ROTORS QUI BOUGENT 
    
def E_Code(): #le mot qu on va ecrire qui doit etre codé / Rotor mouvement
    Mot_a_coder = message.get(1.0,'end').upper()
    if Mot_a_coder == '\n': #cherche si il y a quleque chose d'ecrit 
        showerror('ERROR', 'Veuillez entrer le message codé') #t as rien ecrit ehoh
        return ''
    mot_code = enigma_code(Rotor_1,Rotor_2,Mot_a_coder) #j' utilise ce que j avais dans enigma_code arguments
    #nous devons faire une remise a 0 juste arrivant d'ecrire et on ecris a ce moment la sinon on ecrit plein de fois le codage d'affiler
    Mot_code.delete(1.0,2.0)
    Mot_code.insert (1.0, mot_code)
    

    

#-----Création du tableau comprenant les rotors-----#
    
def Rotor():   #faire apparaitre les rotors dans l'interface graphique 
    for row in range(3):
        for column in range(26):
            Alphabet = Text(Label_Rotor, height = 1, width = 2)
            Alphabet.grid(row = row, column = column)
            if row == 0 :
                Alphabet.replace(0.0, END, chr(column + 65))
            elif row == 1 :
                Alphabet.replace(0.0, END, Rotor_1[column])
            elif row == 2 :
                Alphabet.replace(0.0, END, Rotor_2[column])
                
#-----Création de la frame principale-----#

Enigma = Tk()
Enigma.geometry("600x800")
Enigma.title('Enigma')

#-----Message à coder-----#
Label_Up = LabelFrame(Enigma, text = "Message à coder", padx = 50)
Label_Up.pack(fill = "both", expand = 1, side = TOP)
message = Text(Label_Up, width = 60, height = 10)
message.pack()
Label(Label_Up).pack()

#-----Message codé-----#
Label_Bottom = LabelFrame(Enigma, text= "Message codé", padx = 50)
Label_Bottom.pack(fill = "both", expand = 1, side = BOTTOM)
Mot_code = Text(Label_Bottom, width = 60, height = 10) #elements de type texte dans l interface
Mot_code.pack()
Label_Bottom.pack()

#-----Rotors-----#
Label_Rotor = LabelFrame(Enigma, text = "Rotors", padx = 40)
Label_Rotor.pack(fill = "both", expand = 1)
Rotor()

#-----Boutons----#
Coder = Button(Label_Up, text = "Coder", width = 40, command=lambda: Code())
Coder.pack()

E_Coder = Button(Label_Up, text = "E_Coder", width = 40, command=lambda: E_Code())
E_Coder.pack()
Enigma.mainloop()
