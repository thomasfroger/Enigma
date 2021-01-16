import random #j importe une commande random qui me servira plus tard ainsi qu'une chiane de caractère qui me servira pour Turing
import string

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#cette fonction permet de mélanger l'alphabet pour les rotors ( demandé dans la consigne )
def shuffle_alphabet():  
    alpha=alphabet[:] #les deux points servent a prendre toute la liste 
    random.shuffle(alpha) #on utilise la fonction random pour tout melanger
    return alpha #on la retourne 

#fonction qui donne l'index de la lettre dans l'alphabet
def get_alphabet_index(l): #cette index sert a recuprer la position de chaque lettre 
    if l in alphabet: 
        return alphabet.index(l)
    else:
        return -1 #si on rentre autre chose qu'une lettre de l'alphabet il retourne -1

#fonctionne qui creer les rotors 
def create_rotor(line): 
    rotor = []
    for l in line:
        lettre = l.upper() #permette de traduire la lettre en majuscule
        if lettre in alphabet and lettre not in rotor: #si la lettre est dans l alphabet et pas dans le rotor 
            rotor.append(lettre) #on rajoute la lettre dans le rotor 
    if len(rotor) != len(alphabet): 
        print('Rotor ' + line + ' pas bien définit, aléatoire utilisé a la place\n')
        rotor = shuffle_alphabet()
    return rotor

#fonction qui permet de coder un message avec les rotors fixes
def code(message,rotor1,rotor2,display_function): #la fonction prend comme argument le message qu on ecrit les rotors et la fonction display qui garde en memoire pour le slow
    encoded_message='' #message encode rentre dans une chaine de caractère
    for lettre in message:
        alphabet_index=get_alphabet_index(lettre) #on cherche dans l index de l'alphabet la lettre
        if alphabet_index < 0:
            encoded_message+=' '
            if (display_function): #la fonction retiens en memoire a lettre pour le mode slow
                display_function(' ',-1,-1)
        else:
            rotor1_letter=rotor1[alphabet_index]
            rotor2_letter=rotor2[get_alphabet_index(rotor1_letter)]
            encoded_message+=rotor2_letter
            if display_function:
                display_function(rotor2_letter,alphabet_index,get_alphabet_index(rotor1_letter))
    return encoded_message

#fonction qui permet de décoder le message cripté avec les rotors toujours fixes
def decode(encoded_message,rotor1,rotor2,display_function):
    message=''#le message encode qu on veut a présent decoder 
    for lettre in encoded_message: #pour les lettres dans le message 
        if lettre in alphabet: #si elles sont dans l'alphabet
            lettre_rotor1=alphabet[rotor2.index(lettre)]
            lettre_alphabet=alphabet[rotor1.index(lettre_rotor1)]
            message+=lettre_alphabet
            if (display_function):
                display_function(lettre_alphabet,alphabet.index(lettre),rotor2.index(lettre))
        else:
            message+=' '
            if (display_function):
                display_function(' ',-1,-1)
    return message

#fonction qui permet de faire tourner les rotors d'un cran
def rotate_rotor(rotor): 
    first_letter=rotor[0] #le rotor prend comme première lettre dit 0 car de 0-25 lettre
    del rotor[0]  
    rotor.append(first_letter) #puis le rotor rajoute la première lettre donc avance d un cran 

#fonction qui fait tourner les rotors jusqu'a la position initiale demandée
def init_rotor(rotor,initial_position_r): #on definit la fontion initiales des rotors 
    while rotor[0] != initial_position_r: 
        rotate_rotor(rotor) #on fait tourner le rotor jusqu a la poistion initiale 

#permet de coder un message à la façon d'enigma, avec les deux rotors qui tournent
def enigma_code(message,rotor1,rotor2,initial_position_r1,initial_position_r2,display_function): 
    init_rotor(rotor1,initial_position_r1) #on initialise la position des rotors 1 et 2
    init_rotor(rotor2,initial_position_r2)
    encoded_message=''
    counter = 0 #on créer un compteur 
    for lettre in message:
        alphabet_index=get_alphabet_index(lettre) #il fait approximativement la meme chose que enigma code sauf que ...
        if alphabet_index < 0:
            encoded_message+=' '
            if (display_function):
                display_function(' ',-1,-1)
        else:
            rotor1_letter=rotor1[alphabet_index]
            rotor2_letter=rotor2[get_alphabet_index(rotor1_letter)]
            encoded_message += rotor2_letter 
            if (display_function):
                display_function(rotor2_letter,alphabet_index, get_alphabet_index(rotor1_letter))
            rotate_rotor(rotor1) #il fait tourner les rotors d un cran
            counter+=1 #counter avance aussi d un cran du coup
            if counter == len(alphabet): #quand il fait la taille de l'alphabet
                rotate_rotor(rotor2) #le rotor 2 tourne 
                counter = 0 #le compteur revient a 0
    return encoded_message

#fonction de décode du code avec toujours les rotors en action
def enigma_decode(encoded_message,rotor1,rotor2,initial_position_r1,initial_position_r2,display_function): 
    init_rotor(rotor1,initial_position_r1) #ce code fonctionne de la même manière que enigma_code il va juste par mirroir effectuer un decodage plutot qu un codage
    init_rotor(rotor2,initial_position_r2)
    message=''
    counter = 0
    for lettre in encoded_message:
        if lettre in alphabet:
            lettre_rotor1=alphabet[rotor2.index(lettre)]
            lettre_alphabet=alphabet[rotor1.index(lettre_rotor1)]
            if (display_function):
                display_function(lettre_alphabet,rotor1.index(lettre_rotor1), rotor2.index(lettre))
            message += lettre_alphabet
            rotate_rotor(rotor1) #meme pricipe pour la rotation des rotors 
            counter+=1
            if counter == len(alphabet):
                rotate_rotor(rotor2)
                counter = 0
        else:
            message += ' '
            if (display_function):
                display_function(' ',-1, -1)
    return message
    
#fonction turing qui permet de coder la "bombe"
def turing_decode(encoded_message,rotor1,rotor2,known_word,display_function):# on ajoute l argument du mot connu
    for initial_position_r1 in alphabet: #pour la position initiale du rotor 1 et 2 dans l alphabet
        for initial_position_r2  in alphabet:
            possible_solution=enigma_decode(encoded_message,rotor1,rotor2,initial_position_r1,initial_position_r2,display_function) #la solution possible va être trouvée grace a enigma decode en cherchant la poistion initiale des rotors
            message = str.replace(possible_solution,' ','') # on utilise la string placée en debut de code 
            if known_word in message: #si le mot connu est dans le message 
                return (possible_solution, initial_position_r1, initial_position_r2) #on retourne la solution possible
    return None #sinon rien c est none et ca affiche cannot decode 
    
def load_rotors(filename): #cette fonction sert uniquement a utiiliser le fichier text rotors dans lequel sont ecrit les 1 rotors 
    rotor_file=open(filename, 'r') #voila donc le fichier rotor
    lines = rotor_file.readlines() #on va lire les lignes du fichier
    if (len(lines) >= 2): #tant que la taille de la ligne est superieur ou egal a 2
        r1 = create_rotor(lines[0])
        r2 = create_rotor(lines[1])
    else:
        r1 = shuffle_alphabet()
        r2 = shuffle_alphabet()
    rotor_file.close() #on ferme le fichier texte
    return (r1, r2)

print ("hello world")