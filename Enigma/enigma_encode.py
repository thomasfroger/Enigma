# coding=utf-8
from tkinter import *
from enigma import *  # on importe tout enigma ici car on va se servir des fonctions pour tkinter
import time  # cela nous sert pour le mode slow


def update_rotors():  # on creer la fonction dans tkinter
    for j in range(0, 26):
        rotor1_labels[j]['text'] = rotor1[j]
        rotor2_labels[j]['text'] = rotor2[j]


# fonction qui permet de colorer les lettres
def color_letters(letter, rotor1_index, rotor2_index):
    if slow.get() == 1:  # case coché ou pas
        update_rotors()
        if rotor1_index >= 0 and rotor2_index >= 0:  # Si la lettre du rotor est dans l'alhabet
            bg = alpha[rotor1_index]['bg']  # bg = background

            alpha[rotor1_index]['bg'] = 'red'  # l'arrière plan est coloré
            rotor1_labels[rotor1_index]['bg'] = 'red'  # la lettre correspondante est colorée
            fenetre.update()
            time.sleep(1)  # commande pour slow qui permet d'attendre le temps entre parenthèse en seconde
            alpha[rotor1_index]['bg'] = bg
            rotor1_labels[rotor1_index]['bg'] = bg

            alpha[rotor2_index]['bg'] = 'green'  # on refait la meme manipulation en vert avec un autre
            rotor2_labels[rotor2_index]['bg'] = 'green'
            fenetre.update()
            time.sleep(1)
            alpha[rotor2_index]['bg'] = bg
            rotor2_labels[rotor2_index]['bg'] = bg

    encoded_message.insert('end', letter)


# bouton du code
def code_button_callback():
    encoded_message.delete('0.0', 'end')  # supression du message encodé
    coded_message = code(message.get('0.0', 'end').upper(), rotor1, rotor2,
                         color_letters)  # position du message (upper pour convertir en majuscule)


# le code du bouton enigma_code
def enigma_code_button_callback():
    encoded_message.delete('0.0', 'end')
    initial_position_r1 = entry_conf_r1.get().upper()  # definit la poistion initiale des rotors
    initial_position_r2 = entry_conf_r2.get().upper()
    if initial_position_r1 in alphabet and initial_position_r2 in alphabet:
        init_rotor(rotor1, initial_position_r1)
        init_rotor(rotor2, initial_position_r2)
        update_rotors()  # on rafraichit les rotrs
        coded_message = enigma_code(message.get('0.0', 'end').upper(), rotor1, rotor2, initial_position_r1,
                                    initial_position_r2,
                                    color_letters)  # message code prend la valeur de ce qui va se passer grâce a la fonction enigma code


# défition des rotors
rotor1 = []
rotor2 = []
(rotor1, rotor2) = load_rotors('rotors.txt')  # on cherche les rotors dans le fichier texte

# on definit la fenêtre tkinter
fenetre = Tk()  # on ouvre une nouvelle fenetre
fenetre.title('ENIGMA ENCODE')  # titre de la fenetre
fenetre.geometry('900x600')  # c'est la taille de la fenêtre
fenetre.rowconfigure(0, weight=2)  # on configure la position la taille etc de tout ce qu il y a dans sur cette fenêtre
fenetre.rowconfigure(1, weight=1, minsize=75)
fenetre.rowconfigure(2, weight=2)
fenetre.columnconfigure(0, weight=1)

# tkinter est un cadrillage a la base donc on doit donner la position de chaque élément
# definition de la frame donc du block
message_frame = LabelFrame(fenetre, text='Message a coder')  # la zone ou on va ecrire le message a coder
message_frame.grid(column=0, row=0, sticky="nsew")  # sticky nsex= nord sur est west / ca va positioner le bloque
message_frame.columnconfigure(0, weight=0)
message_frame.columnconfigure(1, weight=1)
message_frame.columnconfigure(2, weight=0)
message_frame.columnconfigure(3, weight=1)
message_frame.columnconfigure(4, weight=0)
message_frame.rowconfigure(0, weight=0)
message_frame.rowconfigure(1, weight=0)
message_frame.rowconfigure(2, weight=1)
message_frame.rowconfigure(3, weight=0)

# definition des boutton
code_button = Button(message_frame, text='Coder',
                     command=code_button_callback)  # on code le bouton et à quoi il sert à quoi il est lier
code_button.grid(column=0, row=0, sticky='new')  # NEW = Nord Est West

enigma_code__button = Button(message_frame, text='Enigma coder',
                             command=enigma_code_button_callback)  # pareil que au dessus mais pour enigma_code
enigma_code__button.grid(column=0, row=1, sticky='new')

# fonction Slow
slow = IntVar()
slow_check = Checkbutton(message_frame, text='Slow',
                         variable=slow)  # la case ou on peut cocher ou pas si on met le mode slow
slow_check.grid(column=0, row=2, sticky='new')  # position de cette case

message = Text(message_frame)  # la ou se trouve le message a coder
message.grid(column=1, row=0, rowspan=3, columnspan=4, sticky="nsew")  # Fenetre de texte

# Config des entrées pour les positions initiales des rotors
label_conf_r1 = Label(message_frame, text='Conf. rotor 1')  # ici on configure les positions initiales
label_conf_r2 = Label(message_frame, text='Conf. rotor 2')
label_conf_r1.grid(column=1, row=3, sticky='e')
label_conf_r2.grid(column=3, row=3, sticky='e')

entry_conf_r1 = Entry(message_frame)
entry_conf_r2 = Entry(message_frame)
entry_conf_r1.grid(column=2, row=3, sticky='nsew')
entry_conf_r2.grid(column=4, row=3, sticky='nsew')

# configuration affichage des rotors ( le tableau avec leur affichage etc
alpha = []
rotor1_labels = []
rotor2_labels = []

rotor_frame = LabelFrame(fenetre, text='Rotors')
rotor_frame.grid(column=0, row=1, sticky="nsew")
for i in range(0, 3):
    rotor_frame.rowconfigure(i, weight=1, pad=20)
    for j in range(0, 26):
        if i == 0:
            label = Label(rotor_frame, text=alphabet[j])
            alpha.append(label)
        elif i == 1:
            label = Label(rotor_frame, text=rotor1[j])
            rotor1_labels.append(label)
        elif i == 2:
            label = Label(rotor_frame, text=rotor2[j])
            rotor2_labels.append(label)
        label.grid(column=j, row=i)
        rotor_frame.columnconfigure(j, weight=1, pad=10)

encoded_mess = LabelFrame(fenetre, text='Message encode')  # position du message enode ou il est etc
encoded_mess.grid(column=0, row=2, sticky="nsew")
encoded_mess.rowconfigure(0, weight=1)
encoded_mess.columnconfigure(0, weight=1)
encoded_message = Text(encoded_mess)
encoded_message.grid(column=0, row=0, sticky="nsew")

fenetre.mainloop()  # ca englobe tout le enigma_encode dans la fenêtre
