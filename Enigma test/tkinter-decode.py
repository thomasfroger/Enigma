from tkinter import*
from tkinter.messagebox import showerror # pour le message d'erreur si y a r d'ecrit
from Enigma import* #import enigma et ses fonctions dans tkinter

Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Rotor_1 = ['A', 'Q', 'W', 'Z', 'S', 'X', 'E', 'D', 'C', 'R', 'F', 'V', 'T', 'G', 'B', 'Y', 'H', 'N', 'U', 'J', 'I', 'K', 'O', 'L', 'P', 'M']

Rotor_2 = ['P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'Z', 'A', 'M', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'Q', 'N', 'B', 'V', 'C', 'X', 'W']


#-----Fonctions-----#

#pour update les rotors quand ca tourne
def update_rotors():
    for j in rangen(0,26):
        Rotor_1_labels[j]['text'] = Rotor_1[j]
        Rotor_2_labels[j]['text'] = rotor_2[j]

def Decode():
    Mot_a_decoder = message.get(1.0,'end').upper()
    if Mot_a_decoder == '\n' :
        showerror('ERROR', 'Rentrez quelque chosoe voyons !') #t as rien ecrit ehoh
        return ''
    mot_decode = decode(Rotor_1,Rotor_2,Mot_a_decoder) #j' utilise ce que j avais dans enigma_code arguments
    #nous devons faire une remise a 0 juste arrivant d'ecrire et on ecris a ce moment la sinon on ecrit plein de fois le codage d'affiler
    Mot_decode.delete(1.0,2.0)
    Mot_decode.insert (1.0, mot_decode)
    #cela ne marche que pour le codage je dois faire de même pour E_code
    
def E_Decode(): #le mot qu on va ecrire qui doit etre codé / Rotor mouvement
    Mot_a_decoder = message.get(1.0,'end').upper()
    if Mot_a_decoder == '\n': #cherche si il y a quleque chose d'ecrit 
        showerror('ERROR', 'Rentrez quelque chosoe voyons !') #t as rien ecrit ehoh
        return ''
    mot_decode = enigma_decode(Rotor_1,Rotor_2,Mot_a_decoder,) #j' utilise ce que j avais dans enigma_code arguments
    #nous devons faire une remise a 0 juste arrivant d'ecrire et on ecris a ce moment la sinon on ecrit plein de fois le codage d'affiler
    Mot_decode.delete(1.0,2.0)
    Mot_decode.insert (1.0, mot_decode)
    #cela ne marche que pour le codage je dois faire de même pour E_code

def Turing_decode():
    message_probable = entry_mdp.get().upper()
    result = turing_decode(message.get(1.0,'end').upper(),Rotor_1,Rotor_2,message_probable,None)
    if result :
        update_rotors()
        mot_decode.insert('0.0',result[0])
        label_conf_Rotor_1_result_bis['text']=result[1]
        label_conf_Rotor_1_result_bis['text']=result[1]
    else:
         Mot_decode = message.insert(1.0,'on peut pas te le decoder mon ami')

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
Label_Up = LabelFrame(Enigma, text = "Message à décoder", padx = 50)
Label_Up.pack(fill = "both", expand = 1, side = TOP)
message = Text(Label_Up, width = 60, height = 10)
message.pack()
Label(Label_Up).pack()

#-----Message codé-----#
Label_Bottom = LabelFrame(Enigma, text= "Message décodé", padx = 50)
Label_Bottom.pack(fill = "both", expand = 1, side = BOTTOM)
Mot_decode = Text(Label_Bottom, width = 60, height = 10) #elements de type texte dans l interface
Mot_decode.pack()
Label_Bottom.pack()

#------configuration des rotors pour poistion initiales ----#
label_conf_Rotor_1=Label(Label_Up, text='configuration rotor 1')
label_conf_Rotor_2=Label(Label_Up, text='configuration rotor 2')
label_conf_Rotor_1.pack()
label_conf_Rotor_2.pack()
entry_conf_Rotor_1=Entry(Label_Up)
entry_conf_Rotor_2=Entry(Label_Up)
entry_conf_Rotor_1.pack()
entry_conf_Rotor_2.pack()

#-------rotors pour si pas de poistion initiale, chercher mot probable---#
mdp_widget=Label(Label_Up, text='mot de passe')
mdp_widget.pack()
entry_mdp=Entry(Label_Up)
entry_mdp.pack()

        
#-----Boutons----#
Decoder = Button(Label_Up, text = "Decoder", width = 40, command=lambda: Decode())
Decoder.pack()

E_Decoder = Button(Label_Up, text = "E_Decoder", width = 40, command=lambda: E_Decode())
E_Decoder.pack()

Turing = Button(Label_Up, text = "Turing", width = 40, command=lambda : Turing_decode())
Turing.pack()
