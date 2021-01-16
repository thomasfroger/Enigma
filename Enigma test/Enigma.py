#Pour commencer créons deux rotors, composées des 26 lettres de l'alphabet dans un ordre aléatoire.
import random
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor_1=['A','Q','W','Z','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','I','K','O','L','P','M']
rotor_2=['P','O','I','U','Y','T','R','E','Z','A','M','L','K','J','H','G','F','D','S','Q','N','B','V','C','X','W'] 

#Fonction qui simule une liste comportant toutes les lettres de l'alphabet dans un ordre aléatoire.
def shuffle_alphabet(rotor_1):
    random.shuffle(rotor_1)
    return rotor_1

#fonction qui donne l'index de la lettre dans l'alphabet
def get_alphabet_index(l): 
    if l in alphabet:
        return alphabet.index(l)
    else:
        return -1
    

#Pour créer le rotor
def create_rotor(line):
    rotor = []
    for l in line:
        lettre = l.upper()
        if lettre in alphabet and lettre not in rotor:
            rotor.append(lettre)
    if len(rotor) != len(alphabet):
        print('Rotor ' + line + ' not well defined, random one used instead\n')
        rotor = shuffle_alphabet()
    return rotor
    
#STEP 1: Enigma statique

#fonction qui permet de coder un message à l'aide de deux rotor sans mouvements.
def code(rotor_1,rotor_2,message):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mot_code=''
    for i in range(0,len(message)-1):
        if message[i] == ' ':
            mot_code+= ' '
        elif message[i] == '\n':
            mot_code+= '\n'
        else:
            lettre_1=rotor_1[alphabet.index(message[i])]#On apprend la position de la 1ère lettre du message via l'alphabet.
            place_alphabet=alphabet.index(lettre_1)
            lettre_2=rotor_2[place_alphabet]
            mot_code+= lettre_2
    return mot_code

#fonction qui decode un message à l'aide de deux rotors sans mouvements. 
def decode(rotor_1,rotor_2,message):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mot_decode=''
    for i in range(0,len(message)-1):
        if message[i] == ' ':
            mot_decode+= ' '
        elif message[i] == '\n':
            mot_decode+= '\n'
        else:
            lettre_1=alphabet[rotor_2.index(message[i])]
            lettre_2=rotor_1.index(lettre_1)
        mot_decode+= alphabet[lettre_2]
    return mot_decode

#STEP 2: Enigma en mouvement

#fonction qui simule un rotor mobile    
def rotor_mobile(tab):
    t=[]
    for i in range (1,len(tab)):
        t+=tab[i]
    t.append(tab[0])    
    return t

#fonction qui code un message à l'aide de deux rotors mobiles.    
def enigma_code(rotor_1,rotor_2,message):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mot_code=''
    for i in range(len(message)-1):
        if message[i] == ' ':
            mot_code+= ' '
        elif message[i] == '\n':
            mot_code+= '\n'
        else:
            lettre_1=rotor_1[alphabet.index(message[i])]#On apprend la position de la 1ère lettre du message via l'alphabet.
            place_alphabet=alphabet.index(lettre_1)
            lettre_2=rotor_2[place_alphabet]
            rotor_1= rotor_mobile(rotor_1)
            if i > len(rotor_1):
                rotor_2=rotor_mobile(rotor_2)
            mot_code+= lettre_2
    return mot_code

#fonction qui decode un message enigma à l'aide de deux rotors mobiles.
def enigma_decode(rotor_1,rotor_2,message):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mot_decode=''
    for i in range(len(message)-1):
        if message[i] == ' ':
            mot_decode+= ' '
        elif message[i] == '\n':
            mot_decode+= '\n'
        else:
            lettre_1=alphabet[rotor_2.index(message[i])]
            lettre_2=rotor_1.index(lettre_1)
            mot_decode+= alphabet[lettre_2]
            rotor_1=rotor_mobile(rotor_1)
            if i > len(rotor_1):
                rotor_2=rotor_mobile(rotor_2)
            
    return mot_decode
    

#STEP 3: Cracker le code

#Fonction qui permet de decode un code à partir d'un mot du code en lui même.
def turing_decode(encoded_message,rotor1,rotor2,known_word,display_function):
    for initial_position_r1 in alphabet:
        for initial_position_r2  in alphabet:
            possible_solution=enigma_decode(encoded_message,rotor1,rotor2,initial_position_r1,initial_position_r2,display_function)
            message = str.replace(possible_solution,' ','')
            if known_word in message:
                return (possible_solution, initial_position_r1, initial_position_r2)
    return None
    
def load_rotors(filename):
    rotor_file=open(filename, 'r') #chargement des rotors données dans l'énonce pour décripter les messages
    lines = rotor_file.readlines()
    if (len(lines) >= 2):
        rotor_1 = create_rotor(lines[0])
        rotor_2 = create_rotor(lines[1])
    else:
        rotor_1 = shuffle_alphabet()
        rotor_2 = shuffle_alphabet()
    rotor_file.close()
    return (rotor_1, rotor_2)





