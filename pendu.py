#Piles à capacité finie
def create_pile(capa):
    pile=(capa+1)*[None]
    pile[0]=0
    return pile

def nombre_elements(pile):
    return pile[0]

def empiler(element,pile):
    pile[pile[0]+1]=element
    pile[0]+=1
    return pile

def depiler(pile):
    element=pile[pile[0]]
    pile[0]-=1
    return pile,element

'''
pile=create_pile(5)
print(nombre_elements(pile))
pile=empiler("j",pile)
print(nombre_elements(pile))
pile,element=depiler(pile)
print(element)


#Tri de tableaux

def trier(liste):
    liste_triee=[]
    liste_triee+=[liste[0]]
    for index in range(1,(len(liste))):
        endroit_a_inserer=0
        for index2 in range(len(liste_triee)):
            if liste[index]>liste_triee[index2]:
                endroit_a_inserer=(index2+1)
        liste_triee=(liste_triee[:endroit_a_inserer]+[liste[index]]+liste_triee[endroit_a_inserer:])
    return liste_triee
print(trier([1,7,4,0,0,7,2,55,5,0,65]))

'''


def partie():
    mot=str(input("Quel est le mot : "))
    chances=8
    lettres_trouvées=(["*"]*len(mot))
    gagné=False
    echec=False
    afficher_partie(lettres_trouvées,chances)
    while (gagné==False and echec==False):
        lettre=input(str("Quelle est la lettre : "))

        if lettre in mot:
            for index in range(len(mot)):
                if mot[index]==lettre:
                    lettres_trouvées[index]=lettre
            afficher_partie(lettres_trouvées,chances)
        else:
            chances-=1
            if chances == 0:
                print ('\n' * 12)
                print ("Bouh vous avez perdu, c'est nul")
                echec=True
            else:
                afficher_partie(lettres_trouvées,chances)
        if lettres_trouvées==list(mot):
            gagné=True
            print ('\n' * 12)
            print ("Bravo vous avez gagné, c'est bien")

def afficher_partie(lettres_trouvées,chances):
    print ('\n' * 12)
    print("Vous avez trouvé : ",lettres_trouvées)
    print("Il vous reste ",chances," chances")

def transformer_casse(lettre):
    rt=None
    rg=0
    Lmaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Lmin=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for id in Lmaj:
        if lettre==id:
            rt=lettre
    for id in Lmin:
        if lettre==id:
            rt=Lmaj[rg]
        rg=rg+1
    return rt


partie()