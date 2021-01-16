from tkinter import *
from enigma import *
import time
#fonctionne presue de la même manière que pour le encode du moins pour la partie grpahique donc se referer a ses explications 
#fonction pour mettre jour les rotors comme pour le encode
def update_rotors():
    for j in range(0,26):
        rotor1_labels[j]['text'] = rotor1[j]
        rotor2_labels[j]['text'] = rotor2[j]
        

#fonction qui illumine les lettre des rotors quand on check le bouton slow       
def highlight_letters(letter,rotor1_index,rotor2_index):
    if slow.get() == 1:
        update_rotors()
        if rotor1_index >= 0 and rotor2_index >= 0:
            bg = alphabet_labels[rotor1_index]['bg']

            alphabet_labels[rotor1_index]['bg'] = 'yellow'
            rotor1_labels[rotor1_index]['bg'] = 'yellow'
            root.update()
            time.sleep(1) #vitesse en seconde du passage d une letter à l'autre
            alphabet_labels[rotor1_index]['bg'] = bg
            rotor1_labels[rotor1_index]['bg'] = bg

            alphabet_labels[rotor2_index]['bg'] = 'cyan'
            rotor2_labels[rotor2_index]['bg'] = 'cyan'
            root.update()
            time.sleep(1)
            alphabet_labels[rotor2_index]['bg'] = bg
            rotor2_labels[rotor2_index]['bg'] = bg

    decoded_message_widget.insert('end',letter)
    
def decode_button_callback():
    decoded_message_widget.delete('0.0','end')
    decoded_message = decode(message_widget.get('0.0','end').upper(),rotor1,rotor2,highlight_letters)
    #decoded_message_widget.insert('0.0',decoded_message)

#fonction pour le bouton decode enigma
def enigma_decode_button_callback():
    decoded_message_widget.delete('0.0','end')
    initial_position_r1 = entry_conf_r1.get().upper()
    initial_position_r2 = entry_conf_r2.get().upper()
    if initial_position_r1 in alphabet and initial_position_r2 in alphabet:
        init_rotor(rotor1,initial_position_r1)
        init_rotor(rotor2,initial_position_r2)
        update_rotors()
        decoded_message = enigma_decode(message_widget.get('0.0','end').upper(),rotor1,rotor2,initial_position_r1,initial_position_r2,highlight_letters)
        label_conf_r1_result_bis['text']=initial_position_r1
        label_conf_r2_result_bis['text']=initial_position_r2
        #decoded_message_widget.insert('0.0',decoded_message)

#fonction qui va utiliser la fonction turing du code enigma
def turing_enigma_decode_callback():
    decoded_message_widget.delete('0.0','end')
    possible_word = entry_mdp.get().upper() #possible mot ( le mot qu on connait )
    result=turing_decode(message_widget.get('0.0','end').upper(),rotor1,rotor2,possible_word,None) #resultat trouvé grâce a la fonction turing 
    if result:
        update_rotors() 
        decoded_message_widget.insert('0.0',result[0])
        label_conf_r1_result_bis['text']=result[1]
        label_conf_r2_result_bis['text']=result[2]
    else:
        decoded_message_widget.insert('0.0','Cannot decode message')
        
#fonction qui permet de d'effacer tout les configs
def reset_conf_callback():
    decoded_message_widget.delete('0.0','end')
    message_widget.delete('0.0','end')
    entry_mdp.delete('0','end')
    entry_conf_r1.delete('0','end')
    entry_conf_r2.delete('0','end')
    slow_check.deselect()
    label_conf_r1_result_bis.grid_forget()
    label_conf_r2_result_bis.grid_forget()

# affichage de la fenêtre principale
root=Tk()
root.title('ENIGMA DECODE')
root.geometry('900x500')
root.rowconfigure(0,weight=2)
root.rowconfigure(1,weight=1,minsize=75)
root.rowconfigure(2,weight=2)
root.columnconfigure(0,weight=1)

#configuration de l'affichage du premier 'frame' (sous fenêtre)
message_frame=LabelFrame(root,text='Message à décoder')
message_frame.grid(column=0,row=0,sticky="nsew")
message_frame.columnconfigure(0,weight=0)
message_frame.columnconfigure(1,weight=1)
message_frame.columnconfigure(2,weight=0)
message_frame.columnconfigure(3,weight=1)
message_frame.rowconfigure(0,weight=0)
message_frame.rowconfigure(1,weight=0)
message_frame.rowconfigure(2,weight=0)
message_frame.rowconfigure(3,weight=1)
message_frame.rowconfigure(4,weight=0)

#config de la zone de texte pour le message à decoder
message_widget=Text(message_frame)
message_widget.grid(column=1,columnspan=7,row=0,rowspan=4,sticky="nsew")

#configuration des boutons à gauche de la zone de texte (**)
code_button=Button(message_frame,text='Décoder',command=decode_button_callback)
code_button.grid(column=0,row=0,sticky='new')
#**
enigma_decode_button=Button(message_frame,text='Enigma décoder',command=enigma_decode_button_callback)
enigma_decode_button.grid(column=0,row=1,sticky='new')
#**
turing_decode_button=Button(message_frame,text='Turing',command=turing_enigma_decode_callback)
turing_decode_button.grid(column=0,row=2,sticky='new')
#**
slow = IntVar()
slow_check=Checkbutton(message_frame,text='Slow',variable=slow)
slow_check.grid(column=0,row=3,sticky='new')
#**
conf_reset_button=Button(message_frame,text='reset conf',command=reset_conf_callback)
conf_reset_button.grid(column=0,row=4,sticky='new')

#configuration des entrées pour decider des positions initiales des rotors
label_conf_r1=Label(message_frame,text='Conf. rotor 1')
label_conf_r2=Label(message_frame,text='Conf. rotor 2')
label_conf_r1.grid(column=1,row=4,sticky='e')
label_conf_r2.grid(column=3,row=4,sticky='e')
entry_conf_r1=Entry(message_frame)
entry_conf_r2=Entry(message_frame)
entry_conf_r1.grid(column=2,row=4,sticky='nsew')
entry_conf_r2.grid(column=4,row=4,sticky='nsew')

#configuration pour que si on a pas les positions initiales des rotors, on puisse chercher un mot qui est dans le message
mdp_widget=Label(message_frame,text='Mot de passe')
mdp_widget.grid(column=5,row=4,sticky='e')
entry_mdp=Entry(message_frame)
entry_mdp.grid(column=6,row=4)

#configuration de l'affichage des rotors
rotor1 = []
rotor2 = []
(rotor1, rotor2) = load_rotors('rotors.txt')

alphabet_labels = []
rotor1_labels = []
rotor2_labels = []

rotor_frame=LabelFrame(root,text='Rotors')
rotor_frame.grid(column=0,row=1,sticky="nsew")
for i in range(0,3):
    rotor_frame.rowconfigure(i,weight=1,pad=20)
    for j in range(0,26):
        if i == 0:
            label=Label(rotor_frame,text=alphabet[j])
            alphabet_labels.append(label)
        elif i == 1:
            label=Label(rotor_frame,text=rotor1[j])
            rotor1_labels.append(label)
        elif i == 2:
            label=Label(rotor_frame,text=rotor2[j])
            rotor2_labels.append(label)
        label.grid(column=j,row=i)
        rotor_frame.columnconfigure(j,weight=1,pad=10)
        
#configuration de la sous-fenêtre pour afficher le message décoder
decoded_message_frame=LabelFrame(root,text='Message décodé')
decoded_message_frame.grid(column=0,row=2,sticky="nsew")
decoded_message_frame.rowconfigure(0,weight=1)
decoded_message_frame.rowconfigure(1,weight=0)
decoded_message_frame.columnconfigure(0,weight=1)
decoded_message_frame.columnconfigure(1,weight=1)
decoded_message_frame.columnconfigure(2,weight=1)
decoded_message_frame.columnconfigure(3,weight=1)
decoded_message_widget=Text(decoded_message_frame)
decoded_message_widget.grid(column=0,row=0,columnspan=4,sticky="nsew")

label_conf_r1_result=Label(decoded_message_frame,text='Conf. rotor 1:')
label_conf_r2_result=Label(decoded_message_frame,text='Conf. rotor 2:')
label_conf_r1_result.grid(column=0,row=1,sticky='ne')
label_conf_r2_result.grid(column=2,row=1,sticky='ne')

label_conf_r1_result_bis=Label(decoded_message_frame,text=' ')
label_conf_r2_result_bis=Label(decoded_message_frame,text=' ')
label_conf_r1_result_bis.grid(column=1,row=1,sticky='nw')
label_conf_r2_result_bis.grid(column=3,row=1,sticky='nw')


root.mainloop()